# **PROYECTO 1**

Este es un proyecto básico de Django con una aplicación proyecto 1, correspondiente a la prueba de SERVINFORMACION.

## Clonar Proyecto

Lo primero que se debe hacer es clonar el proyecto del repositorio fuente

## Configurar el entorno virtual

Para correr el proyecto es opcional configurar un entorno virtual, esta configuracion es a gusto del usuario de acuerdo al sistema operativo o entorno de su preferencia

## Aplicar migraciones

Una vez clonado el proyecto debemos instalar todos los requerimientos necesarios para la correcta ejecucion del proyecto por lo cual debemos ingresr desde la ruta principal el siguiente comando:

```python
pip install -r requirements.txt
```

## Aplicar migraciones

Antes de poner en ejecucion, debemos aplicar migraciones las cuales se aplican con la ejecucion del siguiente comando:

```python
python manage.py migrate
```

## Crear superusuario

Para poder acceder al proyecto y sus funcionalidades, es necesario de un usuario, por lo cual debe crearse mediante el siguiente comando: 

```python
python manage.py createsuperuser
```

De igual manera el usuario creado previamente es:

** Usuario: ** *admin*
** Contraseña: ** *admin2024*

## Correr el proyecto

Una vez instalados los requerimientos del proyecto, para ponerlo en ejecucion debemos ejecutar desde consola el siguiente comando:

```python
python manage.py runserver
```

Una vez este en ejecucion podremos acceder al sitio administrador o a los diferentes endpoints requeridos

** Los enlaces de acceso son los siguientes: **

- http://localhost:8000/admin/                          **Sitio de administracion** 
- http://localhost:8000/crear/                          **Endpoint para crear un usuario POST**
- http://localhost:8000/geocodificar_base               **Endpoint para ejecutar API Google GET**
- http://localhost:8000/eliminar/{id}/                  **Endpoint para eliminar un usuario DELETE**
- http://localhost:8000/usuario/{id}                    **Endpoint para consultar un usuario en especifico GET**
- http://localhost:8000/lista                           **Endpoint para listar todos los usuarios creados GET**
- http://localhost:8000/o/token/                        **Endpoint para solicitar token de autenticacion POST**

para poder obtener un token de autenticacion es necesario de un registro de aplicacion para la obtencion del token por lo cual debemos registrarla en el siguiente enlace:

- http://localhost:8000/o/applications/

debemos diligenciar la siguiente informacion necesaria para la correcta obtencion de token:

- Name       **Nombre de administracion**
- Client id  **Id de cliente**
- Client secret **Secret de cliente**
- Client type **Seleccionar confidential**
- Authorization grant type **Seleccionar Resource Ownner password-based**
- Dar click en SAVE

De igual manera ya se encuentra creado un registro y los valores necesarios para la obtencion del token son:

- Client id: *my-app*
- Client secret: *my-secret*


Dentro del repositorio se encuentra un fixture de la base de datos, se encuentra un exportado del repositorio en postman, y un archivo de texto con los requerimientos necesarios
