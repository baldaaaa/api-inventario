# api-inventario


`Hello World!` 

:warning: We are under construction.

**Pasos para activar el framework:**

1. Tener la version de python de preferencia instalada
1. Hacer pull al repo o descargar el zip
1. Una vez descargado, creamos un entorno virtual para instalar los paquetes necesarios (puedes saltar al paso 4 si no quieres un entorno virtual, pero es recomendado)

Correr en la shell o en cmd `python -m venv my_virtual_environment`, esto creará un directorio en la ubicación actual. Para entrar en el entorno apenas creado debemos correr `my_virtual_environment\Scripts\activate` y en la shell aparecerá `(my_virtual_environment)` al inicio de cada linea. Esto indica que estamos dentro.
  
4. Una vez dentro del entorno (si lo creaste) hay que instalar los paquetes corriendo `pip install -r requirements.txt` haciendo referencia al txt ubicado en el repo.
5. Servir los archivo estáticos con `python manage.py collectstatic` (correrlo cada vez que se agreguen archivos estáticos)
6. Todo listo. Nada más necesitas correr `python manage.py runserver` y para visualizar todo tienes que entrar en el browser al servidor creado en 127.0.0.1:8000.

Ahora puedes ver tu trabajo en vivo en el browser simulando un servidor

Roberto Balda @baldaaaa
