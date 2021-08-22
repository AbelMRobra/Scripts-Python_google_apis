import gspread
from oauth2client.service_account import ServiceAccountCredentials


def conectar_hoja_calculo(email):

    ruta_clave = 'Tu_clave_de_cuenta_de_servicio'
    scope = ['https://spreadsheets.google.com/feeds', "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(ruta_clave, scope)
    client=gspread.authorize(creds)
    sheet = client.open("nombre_hoja_calculo").sheet1

    
