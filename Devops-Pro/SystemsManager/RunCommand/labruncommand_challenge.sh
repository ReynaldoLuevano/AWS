#!/bin/bash
mkdir /var/www/html/images
curl https://d0.awsstatic.com/logos/powered-by-aws.png -o /var/www/html/images/aws2.png
echo "<html><body><br><br><br><h4 align="Center">INSTANCE ID: $INSTANCE_ID</h4><br><h1 align="Center">Hello, from AWS!</h1><h1 align="Center"><img src=\"/images/aws2.png\"/></h1></body></html>" > /var/www/html/index.html

# Enable and start Apache
systemctl stop httpd
systemctl start httpd
