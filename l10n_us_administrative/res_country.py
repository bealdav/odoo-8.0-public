from openerp import models, fields

class CountryStateCounty(models.Model):

    _description = 'State Counties'
    _name = 'res.country.state.county'
    _order = 'state_id,name'

    state_id = fields.Many2one('res.country.state', 'State', required=True)
    name = fields.Char('County', size=33, required=True, help='United States second level administrative boundaries.')
