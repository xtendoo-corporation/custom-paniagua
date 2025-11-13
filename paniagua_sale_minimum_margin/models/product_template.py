# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_margin = fields.Float(
        string='Margen Mínimo (%)',
        default=0.0,
        help='Porcentaje de margen mínimo permitido para vender este producto',
    )

    current_margin = fields.Float(
        string='Margen Actual (%)',
        compute='_compute_current_margin',
        store=False,
        help='Margen de beneficio actual: ((Precio Venta - Coste) / Precio Venta) * 100',
    )

    @api.depends('list_price', 'standard_price')
    def _compute_current_margin(self):
        """Calcula el margen actual basado en precio de venta y coste"""
        for product in self:
            if product.list_price > 0:
                # Margen = ((Precio Venta - Coste) / Precio Venta) * 100
                margin = ((product.list_price - product.standard_price) / product.list_price) * 100
                product.current_margin = margin
            else:
                product.current_margin = 0.0



