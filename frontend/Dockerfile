FROM nginx:alpine

# On supprime le contenu par défaut de Nginx
RUN rm -rf /usr/share/nginx/html/*

# On copie ton code frontend (index.html, etc.) vers le dossier Nginx
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]