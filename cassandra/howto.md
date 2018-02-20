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


