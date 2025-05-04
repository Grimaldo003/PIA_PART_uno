import requests

#Colocar clave API
apikey = input("Coloca tu clave API de Abuse IPDB:\n")
URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip():
    ip = input("Coloca la IP a comprobar:\n")
    headers = {
        'Accept': 'application/json',
        'Key': apikey
    }
    params = {
        'ipAddress' : ip,    
    }

    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status() #Error si ocurre un problema HTTP
        data = response.json()

        #Imprime información de la IP
        print(f"IP: {data['data']['ipAddress']}")
        print(f"Abusos Reportados: {data['data']['totalReports']}")
        print(f"Ultimo Reporte: {data['data']['lastReportedAt']}")
        print(f"Pais: {data['data']['countryCode']}")
        print(f"Puntaje de Confidencialidad: {data['data']['AbuseConfidenceScore']}%")
    except requests.exceptions.HTTPError as err:
        print(f"Error al consultar la API: {err}")