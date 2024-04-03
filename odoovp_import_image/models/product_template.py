

from odoo import api, fields, models, _
import base64
import os
import gdown
import re

class ProductTemplate(models.Model):
    """Inherit the model to add fields and function"""
    _inherit = 'product.template'

    image_url = fields.Char(string='Image URL', help='Image URL or Path')

    def extract_file_id(self,file_url):
        pattern = re.compile(r"/d/([a-zA-Z0-9_-]+)")
        match = pattern.search(file_url)
        if match:
            return match.group(1)
        else:
            return None
    @api.onchange('image_url')
    def onchange_image_url(self):
        if self.image_url:
            image_file_id = self.extract_file_id(self.image_url.strip())
            image = False
            output_file_path = self.env['ir.config_parameter'].sudo().get_param('output_file_path')
            url = False
            if id and id != '':
                url = 'https://drive.google.com/uc?id=' + image_file_id
            if not url:
                return
            output_file = gdown.download(url, output_file_path, quiet=False)
            if output_file:
                with open(output_file, 'rb') as image_file:
                    image = base64.b64encode(image_file.read())
                if image:
                    self.image_1920 = image
                os.remove(output_file)
            if image:
                self.image_1920 = image
