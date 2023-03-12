from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    Conexion = ConexionDB()

    sql = ''' 
        CREATE TABLE registros(
        id_registro INTEGER, 
        nombre VARCHAR(100),
        genero VARCHAR(10),
        raza VARCHAR(20),
        propietario VARCHAR(100),
        telefono INTEGER,
        PRIMARY KEY(id_registro AUTOINCREMENT)
    ) '''
    try:
        Conexion.cursor.execute(sql)
        Conexion.cerrar()
        titulo = 'Creando Registro'
        mensaje = 'Se creo la tabla en la base datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Se detecto un error'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
          

def borrar_tabla():
    
    Conexion = ConexionDB()

    sql = 'DROP TABLE registros'
    try:
        Conexion.cursor.execute(sql)
        Conexion.cerrar()
        titulo = 'Borrando registro'
        mensaje = 'la tabla en la base datos se borro con exito'
        messagebox.showinfo(titulo, mensaje)
    except:   
        titulo = 'Se detecto un error'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)


class Registro:
    def __init__(self, nombre, genero, raza, propietario, telefono):

        self.id_registro = None
        self.nombre = nombre
        self.genero = genero
        self.raza = raza
        self.propietario = propietario
        self.telefono = telefono

    def __str__(self):
        return f'Registro[{self.nombre}, {self.genero}, {self.raza}, {self.propietario}, {self.telefono}]'
    
def guardar(registro):
    conexion = ConexionDB()

    sql = f""" INSERT INTO registros (nombre, genero, raza, propietario, telefono)
    VALUES('{registro.nombre}', '{registro.genero}', '{registro.raza}', '{registro.propietario}', '{registro.telefono}')"""    

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla registro no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()

    lista_registros = []

    sql = 'SELECT * FROM registros'

    try:

        conexion.cursor.execute(sql)
        lista_registros = conexion.cursor.fetchall()
        conexion.cerrar()

    except:

        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla a la base datos'
        messagebox.showwarning(titulo, mensaje)

    return lista_registros    

def editar(registro, id_registro):

    conexion = ConexionDB()

    sql = f""" UPDATE registros

    SET nombre = '{registro.nombre}', genero = '{registro.genero}', raza = '{registro.raza}', propietario = '{registro.propietario}', telefono = '{registro.telefono}'
    WHERE id_registro = {id_registro} """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edicion de datos' 
        mensaje = 'Error en la edicion de datos'   

        messagebox.showerror(titulo,mensaje)

def eliminar(id_registro):
    conexion = ConexionDB()
    sql = f'DELETE FROM registros WHERE id_registro = {id_registro}'    

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:

        titulo = 'Eliminar registro'
        mensaje = 'Seleccione un registro'
        messagebox.showerror(titulo, mensaje)
            


        