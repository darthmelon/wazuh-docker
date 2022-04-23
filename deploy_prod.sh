#!/bin/bash

wazuh_dir = /opt/wazuh/wazuh-docker

cd $wazuh_dir
docker-compose -f generate-opendistro-certs.yml run --rm generator
bash ./production_cluster/kibana_ssl/generate-self-signed-cert.sh
rm generate-self-signed-cert.sh
bash ./production_cluster/nginx/ssl/generate-self-signed-cert.sh
rm generate-self-signed-cert.sh
chmod 600 ./production_cluster/ssl_certs/admin.key ./production_cluster/ssl_certs/admin.pem
chmod 600 ./ssl_certs/*.key
chmod 600 ./production_cluster/kibana_ssl/*.key
chmod 600 ./production_cluster/nginx/ssl/*.key
# run the following command to generate a hash for each user in internal_users.yml
# paste the hash into internal_users.yml
# better idea would be to use Vault or similar secrets store instead of secrets in plaintext
# docker run --rm -ti amazon/opendistro-for-elasticsearch:1.13.2 bash /usr/share/elasticsearch/plugins/opendistro_security/tools/hash.sh

chmod 750 /data/wazuh/manager/*
#chown -R root:root $wazuh_dir/production_cluster/ssl-certs/
chown -R 1000:root /data/elastic
chown -R 101:root /data/wazuh
docker-compose -p wazuh-prod -f wazuh-prod.yml up -d 

