import random
import string

# iniciamos una variable usuarios con una lista vacia 
# donde se almacenaran los usuarios
usuarios = []

def crear_cuenta(*arg:str):
    # Recibe una lista de nombres de clientes y crea varias cuenta con
    # contraseña aleatoria y solicitando la introduccion manual
    # de su respectivo numero de telefono
    # se recorren todos los nombres recibidos como argumento (*arg)
    for nombre in arg:
        # se genera una contraseña aleatoria alfanumerica con un largo de 10 caracteres
        contraseña = generar_contraseña(10)
        # se solicita la introduccion manual del numero telefonico
        telefono = input_telefono(nombre)
        # se inserta el usuario en la base de datos
        usuarios.append({"nombre": nombre,"contraseña":contraseña,"telefono":telefono})

def generar_contraseña(largo:int=8):
    # Genera una contraseña con un largo por defecto de 8 caracteres
    # y puede ser modificado al invocar la funcion    
    # La contraseña contiene mayusculas, minusculas y numeros
    valores = string.ascii_letters + string.digits
    # la funcion random ayudada del ciclo for, va generando una lista
    # con los caracteres en la almacenados en la variable "valores"
    # el tamaño de la contraseña esta definida por la variable "largo"
    # luego con el metodo join convertimos la lista en una cadena de texto
    contraseña = "".join([random.choice(valores) for _ in range(largo)])
    # retornamos la contraseña para su respectivo uso
    return contraseña

def validar_telefono(telefono:str):
    # Funcion con las reglas para validar los numeros telefonicos
    # recibe una cadena de texto como argumento
    # validamos la cantidad de caracteres y si son numericos
    if(len(telefono) == 8 and telefono.isnumeric()):
        #retornamos True, significa que es apta
        return True
    else:
        # En caso de que no pase la validacion, enviamos un mensaje 
        # y retornamos False
        print("El telefono debe contener 8 digitos numericos")
        return False

def input_telefono(nombre):
    # Funcion para capturar el numero telefonico del cliente
    # se recibe el campo nombre como argumento para
    # mostrar que cliente se esta modificando
    # - solicitamos el numero telefonico por consola y lo almacenamos
    # en una variable para usar mas adelante
    telefono = input(f"Ingrese un numero telefonico para {nombre}: ")
    # se envia el telefono como argumento a la funcion validar_telefono
    # ellas nos dira si el numero telefonico cumple con los requisitos
    if not validar_telefono(telefono):
        # si el telefono no valida volvemos a ejecutar esta funcion para
        # que vuelva a digitar el telefono
        input_telefono(nombre)
    else:
        # el telefono paso la validacion y es retornado para su respectivo uso
        return telefono


def mostrar_usuarios():
    # Funcion que muestra los usuarios almacenados en la base de datos
    # recorremos los usuarios con un contador que comienza en 1 gracias a la funcion enumerate
    for contador,usuario in enumerate(usuarios,start=1):
        #mostramos el contador y los datos del usuario
        print(f"{contador} - Nombre: {usuario['nombre']} Contraseña: {usuario['contraseña']} Telefono: {usuario['telefono']}")


# clientes antiguos que necesitan ser agregados a la base de datos
clientes_viejos = "Carlos","Juan","Luis","Jaime","Joaquin","Marcelo","Santiago","Jimmy","Mario","Estefani"

# enviamos los clientes viejos como argumento a la funcion crear_cuenta para que proceda
# a crear las cuentas
crear_cuenta(clientes_viejos)

# ejecutamos la funcion mostrar_usuarios para revisar
# que todo funcione como corresponde
mostrar_usuarios()
