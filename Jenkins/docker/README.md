# README

## My setup

The default uid for the `jenkins` user in the official docker image is 1000. This usually conflicts with ubuntu's user id which is also 1000. 

To work around that problem, I've setup a user `jenkins` in the host machine. Then I've created a directory `/var/jenkins_home` with permissions 775. I've then added gid 1000 to `jenkins` user. 

## Build a local docker image 

    docker build -t myjenkins .

## Run jenkins

To run the docker image using

    docker run -u jenkins -d -v /var/jenkins_home:/var/jenkins_home -P myjenkins
