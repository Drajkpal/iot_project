# Docker commands
1. To build docker image from docker file:
```docker build --tag image_name:tag .```

## Hello there
docker ps - for checking images
docker run -d container name -- for running a container in detached mode
docker stop/start container id ---to stop/start a container
docker ps -a --- all containers
docker exec -it container_id /bin/bash ---to go inside a container as a root user
docker netwrk ls --to check all docker networks
docker network create Mysql(network name)---create a new network
 docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql---to run mysql
 Docker run --name mysq_db -e MYSQL_ROOT_PASSWORD=root -p 3333:3306 -d mysql
docker exec -it 6f31cee7baae(mysql-id) /bin/bash---to run mysql image
mysql -u root -p--- to run mysql
use schema name ---3rd step
give commands and play





   
