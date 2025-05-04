#Importar Shodan
from shodan import Shodan 

#Usar la clave API de Shodan
api_key = input("Introduce tu clave API de Shodan: ")
#Inicio de la API
api = Shodan(api_key)

#Función para buscar dispositivos
def BuscarDispositivo():
    #Realizar la búsqueda
    busquedas = api.search('apache')
    for busquedas in busquedas['matches']:
        #Imprime la IP y el puerto
        print(f"IP: {busquedas['ip_str']}\nPuerto: {busquedas['port']}")

BuscarDispositivo()