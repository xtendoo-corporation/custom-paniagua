# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    tax_id_readonly = fields.Boolean(
        string="Tax Readonly",
        compute="_compute_tax_readonly",
        store=False
    )

    @api.depends('product_id')
    def _compute_tax_readonly(self):
        """Determina si el campo tax_id debe ser readonly según permisos"""
        for line in self:
            # Si es administrador, nunca es readonly
            if self.env.user.has_group('base.group_system'):
                line.tax_id_readonly = False
                continue

            # Si tiene permiso especial, nunca es readonly
            if self.env.user.has_group('paniagua_sale_tax_readonly.group_edit_additional_taxes'):
                line.tax_id_readonly = False
                continue

            # Si no tiene permisos, es readonly
            line.tax_id_readonly = True

    @api.onchange('product_id')
    def _onchange_product_id_set_taxes(self):
        """Rellena automáticamente los impuestos del producto SOLO cuando se cambia el producto"""
        # NO llamar al super para evitar que Odoo sobrescriba con su lógica

        if self.product_id:
            # Solo asignar impuestos si el campo tax_id está vacío o es una línea nueva
            # Esto evita sobrescribir impuestos que ya fueron configurados
            if not self.tax_id:
                # Obtener los impuestos desde product.template (via product.product)
                product_taxes = self.product_id.taxes_id

                if product_taxes:
                    # Filtrar por compañía si es necesario
                    if self.order_id.company_id:
                        product_taxes = product_taxes.filtered(
                            lambda t: t.company_id == self.order_id.company_id
                        )

                    # Asignar los impuestos del producto
                    self.tax_id = product_taxes
                    _logger.info(
                        f"Impuestos asignados desde producto {self.product_id.display_name}: "
                        f"{', '.join(product_taxes.mapped('name'))}"
                    )
                else:
                    _logger.info(
                        f"Producto {self.product_id.display_name} no tiene impuestos configurados"
                    )













