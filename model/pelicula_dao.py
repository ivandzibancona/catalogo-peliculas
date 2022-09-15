from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Crear Catálogo'
        mensaje ='Se creo un catálogo de películas'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Catálogo'
        mensaje ='La tabla ya está creada'
        messagebox.showwarning(titulo, mensaje)

    
def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Borrar Catálogo'
        mensaje = 'El catálogo de películas se borro con éxito'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Borrar Catálogo'
        mensaje = 'No hay catálogo para borrar'
        messagebox.showerror(titulo, mensaje)


class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

def guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero) VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Registro de Películas'
        mensaje = 'El catalálogo de películas no está creado'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    lista_peliculas = []

    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar
    except:
        titulo = 'Catálogo de Películas'
        mensaje = 'Crea el catálogo de películas'
        messagebox.showwarning(titulo, mensaje)
    
    return lista_peliculas

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}' WHERE id_pelicula = {id_pelicula}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Edición de Datos'
        mensaje = 'Se ha editado un registro correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Edición de Datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Eliminar Datos'
        mensaje = 'Se ha eliminado un registro correctamente'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Eliminar Datos'
        mensaje = 'No se pudo eliminar el registro'
        messagebox.showerror(titulo, mensaje)