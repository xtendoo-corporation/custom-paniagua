# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('price_unit', 'discount', 'product_id', 'product_uom_qty', 'purchase_price')
    def _check_minimum_margin(self):
        """Valida que no se venda por debajo del margen mínimo"""
        for line in self:
            if line.product_id and line.product_id.minimum_margin > 0:
                # Usar el margin_percent que ya calcula Odoo (está en decimal, multiplicamos por 100)
                current_margin = (line.margin_percent or 0.0) * 100

                if current_margin < line.product_id.minimum_margin:
                    price_reduce = line.price_unit * (1 - (line.discount or 0.0) / 100.0)

                    raise ValidationError(
                        f"⚠️ MARGEN INSUFICIENTE\n\n"
                        f"No se puede vender '{line.product_id.name}'\n"
                        f"Margen actual: {current_margin:.2f}%\n"
                        f"Margen mínimo requerido: {line.product_id.minimum_margin:.2f}%\n\n"
                        f"Precio venta unitario: {line.price_unit:.2f} €\n"
                        f"Coste unitario: {line.purchase_price:.2f} €\n"
                    )




