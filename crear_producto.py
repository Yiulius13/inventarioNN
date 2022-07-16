import sqlite3
import os
from peewee import *


def cls():
    os.system('cls')



db = SqliteDatabase('productos.db')
# Creo base de datos
class Articulos(Model):
    codigo = TextField(unique = True)
    tipo = TextField()
    modelo = TextField()
    color = TextField()
    # nombre = TextField()
    cantidad = IntegerField()
    class Meta:
        database = db
db.connect()
db.create_tables([Articulos])













def crear_producto(tipos_dict):
    x=1
    cls()
    for i in tipos_dict.keys():
        print(x," ",i)
        x=x+1
    tipo_num=int(input("Tipo:"))-1
    tipo=list(tipos_dict.keys())[tipo_num]

    modelo_dict=list(tipos_dict.values())[tipo_num]
    
    x=1
    cls()
    for i in modelo_dict.keys():
        print(x,"  ",i)
        x=x+1
    modelo_num=int(input("Modelo "))-1
    modelo=list(modelo_dict.keys())[modelo_num]

    color_list=modelo_dict[modelo]
    
    x=1
    cls()
    for i in color_list:
        print(x,"  ",i)
        x=x+1
    color_num=int(input("Color: "))-1
    color=color_list[color_num]

    return ["{}-{}-{}".format(tipo_num,modelo_num,color_num),tipo,modelo,color]



def obtener_diccionarios():
    con=sqlite3.connect("tipos.db")
    cur=con.cursor()
    
    tablas=[]
    for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        tablas.append(row[0])
    
    tipos={}
    for tabla in tablas:
        tipo={}
        cur.execute("SELECT * FROM {}".format(tabla))
        for key in cur.description[1:]:
            values=[]
            for value in cur.execute("SELECT {} FROM {};".format(key[0],tabla)):
                if value[0]=="":
                    pass
                else:
                    values.append(value[0])
            tipo[key[0]]=values
        tipos[tabla]=tipo
    cur.close()
    con.close()
    return tipos


info=crear_producto(obtener_diccionarios())

data = Articulos(codigo = info[0], tipo = info[1], modelo = info[2], color = info[3], cantidad = 0)
data.save()