FROM redhat/ubi8

RUN yum install httpd -y

COPY src/ /var/www/html/

RUN ls -la /var/www/html/assets/img

ENTRYPOINT [ "/usr/sbin/httpd", "-D", "FOREGROUND" ]

EXPOSE 80

