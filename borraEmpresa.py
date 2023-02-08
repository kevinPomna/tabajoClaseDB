from pymongo import MongoClient

cliente = MongoClient('localhost:27017')
db = empresa.db_tienda_informatica
def delete():
    try:
    
        criterio = input("\n Ingresa el id del registro a eliminar \n ")
        db.cliente.delete_many(
            {'id':float(criterio)}
        )
        print("Registro",criterio,"Eliminado correctamente")
        print(f"Registro{criterio} Eliminado correctamente")

    except ImportError:
         platform_specific_module = None
         print(str(e))