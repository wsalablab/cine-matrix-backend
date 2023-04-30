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


movie : 1 5 7
genre : 1

-----------------------------------------------

authentication-service 

GET
http://localhost:8080/api/v1/authentication/1/

POST
http://localhost:8080/api/v1/authentication/
{
"name": "thomas"
}

POST
http://localhost:8080/api/v1/authentication/user/
{
"name":"Benoit",
"mail":"benoit@gmail.com",
"password":"1234",
"token": "monToken"
}

GET
http://localhost:8080/api/v1/authentication/user/12/

DELETE
http://localhost:8080/api/v1/authentication/user/13/



Movie[id, title, poster, synopsis] oui
Genre[id, name] oui
Movie_genre[id_movie, id_genre] oui
User[name, mail, password_hashed, token, token_exp] oui
Movie_watch[id_user, id_movie, id_appreciation]
Appreciation[id, name]
Group[name] oui
User_group[id_group, id_user] oui


POST 
http://localhost:8080/api/v1/usergroup/user-group/
{
"id_group": "1",
"id_user": "11"
}


