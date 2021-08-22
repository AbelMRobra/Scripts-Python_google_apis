from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

# Inicio -> Tipo datetime formato ISO -> Inicio del evento
# Final -> Tipo datetime formato ISO -> Final del evento
# Nombre -> Tipo datetime formato ISO -> Nombre del evento
# Descripción -> Tipo datetime formato ISO -> Descripción del vento

def crear_evento(inicio, final, nombre, descripcion):

    service_account_email = "email_cuenta_de_servicio"
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    ruta_clave = 'Tu_clave_de_cuenta_de_servicio'
    credentials = service_account.Credentials.from_service_account_file(ruta_clave)
    scoped_credentials = credentials.with_scopes(SCOPES)


    def build_service():
        service = build("calendar", "v3", credentials=scoped_credentials)
        return service

    def create_event():

        service = build_service()
        start_datetime = datetime.now(tz=pytz.utc)
        event = (
            service.events()
            .insert(
                calendarId="msuv5umh0njmqt1o543iu319fc@group.calendar.google.com",
                body={

                    "summary": "{}".format(nombre),
                    "description": "{}".format(descripcion),
                    "start": {"dateTime": inicio},
                    "end": {"dateTime": final},
                },
            )
            .execute()
        )

    create_event()