#!/usr/bin/env bash
# This script sets up web servers for deployment of web static

apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'Holberton School Project' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

new_config="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/^}/ i $new_config" /etc/nginx/sites-enabled/default

service nginx restart
