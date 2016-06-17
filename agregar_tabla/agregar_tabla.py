# -*- encoding: utf-8 -*-
 
#importamos la clase osv del modulo osv y fields
from openerp.osv import fields
from openerp.osv import osv
import time
from datetime import datetime
from openerp.tools.translate import _
 
#Creamos una clase llamada product_product que hereda de la clase product_product padre que esta en /opt/openerp/server/openerp/addons/product
#En openobject hay varios tipos de herencia averiguar mas del tema
#Aqui las clases tienen un atributo _name que es el nombre de la tabla que existe o se creara cuando instalamos el modulo en postgresql
 
class mrp_operations_operation(osv.osv):
    _name = 'operations.operation' # Aqui va el mismo nombre de la clase que se hereda
    _inherit = 'operations.operation' # Permite la herencia propiamente dicho del modulo product 
 
    #Agregamos el campo categoria al formulario  Orden de produccion  
    _columns = {
                'Categoria': fields.char('Categoria',size=40),
        }
product_product()
