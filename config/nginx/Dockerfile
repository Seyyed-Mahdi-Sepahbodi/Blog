FROM nginx:1.15
LABEL MAINTAINER="Seyyed Mahdi Sepahbodi | seyyedmahdisepahbodi@gmail.com"

COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]