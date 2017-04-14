FROM jenkins:2.46.1
# if we want to install via apt
USER root
RUN apt-get update && apt-get install -y python
USER jenkins
RUN jenkins
