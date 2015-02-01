from openerp import models, fields, api

class res_partner(models.Model):

    _inherit = 'res.partner'

    county_id = fields.Many2one('res.country.state.county', 'County')

    @api.model
    def _address_fields(self):
        address_fields = set(super(res_partner, self)._address_fields())
        address_fields.add('county_id')
        return list(address_fields)
