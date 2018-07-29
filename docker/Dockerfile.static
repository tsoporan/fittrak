# Dockerfile for fittrak static assets

FROM nginx:alpine

COPY fittrak/static /usr/share/nginx/html/static
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
