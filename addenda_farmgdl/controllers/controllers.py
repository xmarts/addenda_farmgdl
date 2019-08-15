# -*- coding: utf-8 -*-
from odoo import http

# class AddendaFarmgdl(http.Controller):
#     @http.route('/addenda_farmgdl/addenda_farmgdl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_farmgdl/addenda_farmgdl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_farmgdl.listing', {
#             'root': '/addenda_farmgdl/addenda_farmgdl',
#             'objects': http.request.env['addenda_farmgdl.addenda_farmgdl'].search([]),
#         })

#     @http.route('/addenda_farmgdl/addenda_farmgdl/objects/<model("addenda_farmgdl.addenda_farmgdl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_farmgdl.object', {
#             'object': obj
#         })