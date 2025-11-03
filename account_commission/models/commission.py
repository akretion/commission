# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Commission(models.Model):
    _inherit = "commission"

    invoice_state = fields.Selection(
        selection=[
            ("open", "Invoice Based"),
            ("partial", "Partial Payment Based"),
            ("paid", "Full Payment Based"),
        ],
        string="Invoice Status",
        default="open",
        help="Select the invoice status for settling the commissions:\n"
        "* 'Invoice Based': Commissions are settled when the invoice is issued.\n"
        "* 'Payment Based': Commissions are settled when the invoice is paid (or refunded).",
    )
