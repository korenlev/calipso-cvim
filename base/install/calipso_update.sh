#!/bin/bash

# script to initiate after manual update of the 5 calipso containers

my_ip=$(ip route get 8.8.8.8 | head -1 | cut -d' ' -f7)
echo "running from ip:" $my_ip

# update local calipso code
cd /home/calipso/Calipso
git pull

# run old calipso containers using new calipso installer
# python3 /home/calipso/Calipso/base/install/calipso-installer.py --command start-all --copy q

# commit code changes to new images
echo "commiting code changes..."
docker commit calipso-test korenlev/calipso:test-v2
docker commit calipso-monitor korenlev/calipso:monitor-v2
docker commit calipso-scan korenlev/calipso:scan-v2
docker commit calipso-api korenlev/calipso:api-v2
docker commit calipso-listen korenlev/calipso:listen-v2

# push new images to dockerhub
echo "pushing to dockerhub..."
docker push korenlev/calipso:test-v2
docker push korenlev/calipso:monitor-v2
docker push korenlev/calipso:scan-v2
docker push korenlev/calipso:api-v2
docker push korenlev/calipso:listen-v2

# kill and remove running containers using new calipso-installer
echo "killing running containers..."
python3 /home/calipso/Calipso/base/install/calipso-installer.py --command stop-all

# remove new and old local images
echo "removing local new and old images..."
docker rmi -f korenlev/calipso:test-v2
docker rmi -f korenlev/calipso:monitor-v2
docker rmi -f korenlev/calipso:scan-v2
docker rmi -f korenlev/calipso:api-v2
docker rmi -f korenlev/calipso:listen-v2
docker rmi -f $(docker images | grep '<none>')

# pull for new images from dockerhub
echo "pulling new images from dockerhub..."
docker pull korenlev/calipso:test-v2
docker pull korenlev/calipso:monitor-v2
docker pull korenlev/calipso:scan-v2
docker pull korenlev/calipso:api-v2
docker pull korenlev/calipso:listen-v2

# tag new images for cisco docker repo
echo "tagging for cisco docker repo..."
docker tag korenlev/calipso:test-v2 cloud-docker.cisco.com/calipso:test-v2
docker tag korenlev/calipso:monitor-v2 cloud-docker.cisco.com/calipso:monitor-v2
docker tag korenlev/calipso:scan-v2 cloud-docker.cisco.com/calipso:scan-v2
docker tag korenlev/calipso:api-v2 cloud-docker.cisco.com/calipso:api-v2
docker tag korenlev/calipso:listen-v2 cloud-docker.cisco.com/calipso:listen-v2

# push new images to cisco docker repo
echo "pushing to cisco docker repo..."
docker push cloud-docker.cisco.com/calipso:test-v2
docker push cloud-docker.cisco.com/calipso:monitor-v2
docker push cloud-docker.cisco.com/calipso:scan-v2
docker push cloud-docker.cisco.com/calipso:api-v2
docker push cloud-docker.cisco.com/calipso:listen-v2

exit
