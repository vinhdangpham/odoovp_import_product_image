# -*- coding: utf-8 -*-
import base64
from odoo.exceptions import ValidationError
from odoo import models, fields, _


class ProductImport(models.Model):

    _name = 'product.import'
    _description = 'Product Import'

    file = fields.Binary(string="Upload File")
    file_name = fields.Char(string="File Name")
    key_imports =  fields.Selection([('name','Name'),('default_code','Default Code'),('barcode','Barcode')], string='Key Import', default='name')
    def import_file(self):
        """Function to import product image from csv"""
        if not self.file:
            raise ValidationError(_("Please choose the file!"))
        try:
            file = base64.b64decode(self.file)
            file_string = file.decode('utf-8')
            file_string = file_string.split('\n')
        except Exception:
            raise ValidationError(_("Please choose the correct file!"))
        firstline = True
        for file_item in file_string:
            if firstline:
                firstline = False
                continue
            domain = []
            value_search =  file_item.split(",")[0].strip()
            if self.key_imports == 'name':
                domain = [('name','=',value_search)]
            elif self.key_imports == 'default_code':
                domain = [('default_code','=',value_search)]
            else:
                domain = [('barcode','=',value_search)]
            product_temp = self.env['product.template'].search(domain)
            if product_temp:
                file_parts = file_item.split(",")
                if len(file_parts) >= 2:
                    image_url = file_parts[1]
                    if image_url:
                        product_temp.image_url = image_url
                        product_temp.onchange_image_url()