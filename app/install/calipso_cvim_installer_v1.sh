#!/bin/bash
my_ip=$(ip route get 8.8.8.8 | awk 'NR==1 {print $NF}')

useradd calipso
echo "calipso" | passwd --stdin calipso
usermod -aG wheel calipso
su calipso -
cd /home/calipso

sudo echo "server $my_ip" > calipso_mongo_access.conf
sudo echo "user calipso" >> calipso_mongo_access.conf
sudo echo "port 27017" >> calipso_mongo_access.conf
sudo echo "pwd calipso_default" >> calipso_mongo_access.conf
sudo echo "auth_db calipso" >> calipso_mongo_access.conf
sudo echo "user admin" > ldap.conf
sudo echo "password password" >> ldap.conf
sudo echo "url ldap://$my_ip:389" >> ldap.conf
sudo echo "user_id_attribute CN" >> ldap.conf
sudo echo "user_pass_attribute userpassword" >> ldap.conf
sudo echo "user_objectclass inetOrgPerson" >> ldap.conf
sudo echo "user_tree_dn OU=Users,DC=openstack,DC=org" >> ldap.conf
sudo echo "query_scope one" >> ldap.conf
sudo echo "tls_req_cert allow" >> ldap.conf
sudo echo "group_member_attribute member" >> ldap.conf

sudo chcon -Rt svirt_sandbox_file_t /home/calipso/

sudo docker run -d -v /home/calipso/db:/data/db -p $my_ip:27017:27017 -p $my_ip:28017:28017 --net=host --restart always --name calipso-mongo cloud-docker.cisco.com/calipso:mongo-v2

sudo docker run -d -v /home/calipso:/local_dir -e MONGO_CONFIG=/local_dir/calipso_mongo_access.conf -e PYTHONPATH=/home/scan/calipso_prod/app -p $my_ip:10022:22 --net=host  --restart always --name calipso-test cloud-docker.cisco.com/calipso:test-v2

sudo docker run -d -v /home/calipso:/local_dir -p $my_ip:389:389 --net=host  --restart always --name calipso-ldap cloud-docker.cisco.com/calipso:ldap-v2

sudo docker run -d -e MONGO_CONFIG=/local_dir/calipso_mongo_access.conf -e LDAP_CONFIG=/local_dir/ldap.conf -e LOG_LEVEL=DEBUG -e BIND=0.0.0.0:8000 -v /home/calipso:/local_dir -p $my_ip:8000:8000 -p $my_ip:40022:22 --net=host  --restart always --name calipso-api cloud-docker.cisco.com/calipso:api-v2

sudo docker run -d -v /home/calipso:/local_dir -e MONGO_CONFIG=/local_dir/calipso_mongo_access.conf -e PYTHONPATH=/home/scan/calipso_prod/app -p $my_ip:30022:22 --net=host  --restart always --name calipso-scan cloud-docker.cisco.com/calipso:scan-v2

sudo docker run -d -v /home/calipso:/local_dir -e MONGO_CONFIG=/local_dir/calipso_mongo_access.conf -e PYTHONPATH=/home/scan/calipso_prod/app -p $my_ip:50022:22 --net=host --restart always --name calipso-listen cloud-docker.cisco.com/calipso:listen-v2

sudo docker run -d -v /home/calipso:/local_dir -e PYTHONPATH=/home/scan/calipso_prod/app -p $my_ip:20022:22 -p $my_ip:4567:4567 -p $my_ip:5671:5671 -p $my_ip:15672:15672 --net=host --restart always --name calipso-monitor cloud-docker.cisco.com/calipso:monitor-v2

sudo docker run -d -e ROOT_URL=http://$my_ip:8080 -e MONGO_URL=mongodb://calipso:calipso_default@$my_ip:27017/calipso -p $my_ip:8080:4000 --net=host --restart always --name calipso-ui cloud-docker.cisco.com/calipso:ui-v2

sudo iptables -D INPUT 8

exit
