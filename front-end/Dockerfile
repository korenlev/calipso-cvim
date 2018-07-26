#FROM meteorhacks/meteord:onbuild
FROM jshimko/meteor-launchpad:latest
#FROM jshimko/meteor-launchpad:older
#FROM jshimko/meteor-launchpad:devbuild
#FROM korenlev/calipso:ui-w-node
EXPOSE 4000
ENV PORT 4000
RUN apt-get -y update
RUN apt-get -y install sudo
RUN apt-get -y install curl
RUN apt-get -y install vim
RUN apt-get -y install net-tools
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs
RUN cd /opt/meteor/dist/bundle/programs/server && npm uninstall fibers && npm install fibers
