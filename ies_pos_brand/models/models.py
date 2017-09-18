# -*- coding: utf-8 -*-
# Part of Inceptus ERP Solutions Pvt.ltd.
# See LICENSE file for copyright and licensing details.

from odoo import models, fields, api, _
from odoo import http
from PIL import Image
import os

class POSConfig(models.Model):

    _inherit = 'pos.config'

    @api.model
    def _set_image(self):
        return self.env.user.company_id.logo

    image = fields.Binary(
        "Image", attachment=True,
        help="Image of the to be set of POS",
        default=_set_image)
    
    @api.multi
    def store_logo(self):
        module_name = 'ies_pos_brand'
        addons_path = http.addons_manifest[module_name]['addons_path']
        images_path = "%s/%s/%s"%(addons_path, module_name, 'static/src/img')
        for rec in self:
            if not os.path.exists(images_path) or not rec.image:
                continue
            image_base64 = str(rec.image).decode('base64')
            fp = open(images_path + '/%d_pos_logo.png'%(rec.id), 'wb')
            fp.write(image_base64)
            fp.close()
            img = Image.open('%s/%d_%s'%(images_path, rec.id, 'pos_logo.png')).convert('LA')
            img.save('%s/%d_%s'%(images_path, rec.id, 'pos_logo_bw.png'))
        
    @api.model
    def create(self, vals):
        res = super(POSConfig, self).create(vals)
        res.store_logo()
        return res
    @api.multi
    def write(self, vals):
        res = super(POSConfig, self).write(vals)
        for rec in self:
            rec.store_logo()
        return res
        