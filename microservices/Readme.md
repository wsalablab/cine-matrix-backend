## docker avant 

dans le repertoire où il y a Dockerfile faire : 
docker-compose build

## docker

docker-compose up -d

docker ps

docker compose stop

docker-compose down

## debug
Le nom est défini dans docker-compose.yml

docker-compose logs authentication_service
docker-compose logs movie_service
docker-compose logs movie_db

## endpoints

POST
http://localhost:8080/api/v1/movie/

{
"name": "Matrix"
}
