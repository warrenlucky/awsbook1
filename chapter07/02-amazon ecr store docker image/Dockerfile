FROM public.ecr.aws/amazonlinux/amazonlinux:latest
# Install apache webserver
RUN yum update -y && \
    yum install -y httpd
# write hello world message
RUN echo 'Hello World!' > /var/www/html/index.html
# create shell script to Configure apache
RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
    echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
    echo 'ServerName localhost' >> /etc/httpd/conf/httpd.conf && \
    chmod 755 /root/run_apache.sh
EXPOSE 80
# run script
CMD /root/run_apache.sh