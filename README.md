# PYTHON con Google

Scripts para interactuar con las API de Google, sin autenticar por OAuth, utilizando cuentas de servicio

* Crear una cuenta de servicio
* Crear eventos con google calendar
* Vincular y modificar una hoja de calculo

## Crear una cuenta de servicio:

* Primero debes crear un proyecto en Google Cloud
* Luego debes habilitar dentro de "Api y servicios" la api: "Google Calendar Api"
* Crea una credencial de cuenta de servicio, habilita la cuenta para delegación en todo dominio y genera una calve, al generar la calve se guardara un archivo .JSON, guardalo para su uso en los scripts

## Crear eventos en un calendario:

* En la cuenta de servicio que acabas de crear tendras un correo electronico, invita este correo al calendario donde quieres crear eventos con el script, otorgandole los permisos de propietario
* Instala la libreria que aparece en la documentación de google :
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

    https://developers.google.com/calendar/api/quickstart/python?hl=es_419

* Ejecuta el script crear_evento.py (Recuerda armar una linea donde se ejecute la función y colocar los parametros necesarios para que funcione)

Si todo fue realizado correctamente, deberias ver el evento creado en el calendario

### Detalles a tener en cuenta:

* Al utilizar una cuenta de servicio no sera necesario autenticar con OAuth, pero no podras realizar acciones como agregar invitados a los eventos

