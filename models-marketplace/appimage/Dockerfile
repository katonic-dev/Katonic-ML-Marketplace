FROM marketplace.gcr.io/google/nginx1:1.15
COPY html /usr/share/nginx/html
COPY license /usr/share/doc/nginx/license
RUN chmod -R a+r /usr/share/nginx
RUN chmod -R 755 /usr/share/nginx/html