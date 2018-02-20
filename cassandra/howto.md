# Cassandra howto

## starting a docker cassandra node

this command will create a docker image with name n1.

    docker run --name=n1 -d tobert/cassandra

verify that the docker image is up and running

    docker ps
    
check if cassandra is up and running

    docker exec -it n1 nodetool status

check token values

    docker exec -it n1 nodetool ring

view cassandra config file

    docker exec -it n1 /bin/bash

    cd /data/conf

    less cassandra.yaml

get the ip address of the first node

    docker inspect -f '{{ .NetworkSettings.IPAddress }}' n1
    
start a second node 

    docker run --name n2 -d tobert/cassandra -seeds <ip address of seed node>

start a cassandra image with dc and rac parameters

    docker run --name n1 -d tobert/cassandra -dc DC1 -rack RAC1

view cassandra config file

    docker exec -it n1 /bin/bash

    cd /data/conf

    less cassandra-rackdc.properties

stop and remove the containers

    docker stop n1 n2 n3
    docker rm n1 n2 n3
