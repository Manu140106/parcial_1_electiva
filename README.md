"# Parcial 1 Electiva" 
Este proyecto utiliza Docker Compose para configurar un contenedor con una base de datos PostgreSQL, exponiendo el puerto 4500.

Requisitos

Tener instalado Docker y Docker Compose en tu sistema.

Pasos para levantar el contenedor

Clona el repositorio (si aún no lo has hecho):

git clone <URL_DEL_REPOSITORIO>
cd parcial_1_electiva/Docker

Levanta el contenedor con el siguiente comando:

docker-compose up -d

Esto descargará la imagen de PostgreSQL y creará el contenedor en segundo plano.

Verifica que el contenedor esté corriendo:

docker ps

Deberías ver un contenedor con el nombre postgres_container en la lista.

Conectar a la base de datos

Para acceder a la base de datos dentro del contenedor:

 docker exec -it postgres_container psql -U admin -d mydatabase

Para salir de psql, escribe:
