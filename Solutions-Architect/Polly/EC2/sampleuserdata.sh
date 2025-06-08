#!/bin/bash
yum install httpd -y
echo "<html><body><h1>Hola chavales Arq 122</h1></body></html>" > /var/www/html/index.html
systemctl enable httpd
service httpd start

