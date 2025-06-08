FROM redhat/ubi8

RUN yum install httpd -y

COPY index.html /var/www/html

RUN mkdir -p /var/www/html/images

COPY images/*.jpg /var/www/html/images/

ENTRYPOINT [ "/usr/sbin/httpd", "-D", "FOREGROUND" ]

EXPOSE 80

