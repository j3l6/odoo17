# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Colaborador(models.Model):
    _name = 'colaboradores.colaborador'
    _description = 'Registro de Colaboradores'

    name = fields.Char(string='Nombre Completo', required=True)
    fecha_ingreso = fields.Date(string='Fecha de Ingreso', default=fields.Date.context_today)
    email = fields.Char(string='Correo Electrónico')
    puesto = fields.Selection([
        ('dev', 'Desarrollador'),
        ('analista', 'Analista'),
        ('gerente', 'Gerente'),
    ], string='Puesto', default='dev')

    @api.model
    def create(self, vals):
        """Ejemplo de sobreescritura de create para marcar la fecha."""
        record = super().create(vals)
        # podrías enviar un email o log algo aquí
        return record
