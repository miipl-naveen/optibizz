from openerp import models, api, osv
from openerp.exceptions import Warning
from datetime import datetime
from openerp.osv import fields

class sale_order_limit(models.Model):
    _inherit = 'sale.order'

    @api.one
    def action_wait(self):
        result = self.check_limit()
        return result and super(sale_order_limit, self).action_wait()

    @api.one
    def check_limit(self):
        if self.order_policy == 'prepaid':
            return True

        domain = [
            ('order_id.partner_id', '=', self.partner_id.id),
            ('invoiced', '=', False),
            ('order_id.state', 'not in', ('draft', 'sent', 'cancel'))
        ]
        order_lines = self.env['sale.order.line'].search(domain)
        order_outstanding = sum([x.price_subtotal for x in order_lines])

        domain = [
            ('partner_id', '=', self.partner_id.id),
            ('state', '=', 'draft')
        ]
        draft_invoices = self.env['account.invoice'].search(domain)
        draft_invoice_outstanding = sum([x.amount_total for x in draft_invoices])

        available_credit = self.partner_id.credit_limit - self.partner_id.credit - order_outstanding - draft_invoice_outstanding
        if self.amount_total > available_credit:
            msg = "The Order total of this order is greater than the available credit limit of %s to %s. Please revise the quote" % (self.partner_id.credit_limit, self.partner_id.name)
            raise Warning(msg)
        # raise Warning("Hello...")
        self.date_order = fields.datetime.now()
        return True

# sale_order_line_empty_name()

