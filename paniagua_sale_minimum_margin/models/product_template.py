# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_margin = fields.Float(
        string='Margen Mínimo (%)',
        default=0.0,
        help='Porcentaje de margen mínimo permitido para vender este producto',
    )

