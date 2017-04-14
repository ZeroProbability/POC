FROM jenkins:2.46.1
# if we want to install via apt
USER root
RUN chown jenkins /var/jenkins_home && chgrp jenkins /var/jenkins_home 
RUN apt-get update && apt-get install -y python openssh-server
USER jenkins
