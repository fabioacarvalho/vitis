# Use a imagem oficial do Nginx como base
FROM nginx:latest

# Copie os arquivos de configuração personalizados para o contêiner
COPY nginx.conf /etc/nginx/nginx.conf

# Copie os arquivos do site para o diretório padrão do Nginx
COPY html /usr/share/nginx/html

# Exponha a porta 80 para acesso HTTP
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]