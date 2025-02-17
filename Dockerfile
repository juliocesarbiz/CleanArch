# Utiliza a imagem oficial do MySQL na versão mais recente
FROM mysql:latest

# Define as variáveis de ambiente para configuração do MySQL
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_USER=martins
ENV MYSQL_PASSWORD=1234
ENV MYSQL_DATABASE=test_db

# Expõe a porta padrão do MySQL
EXPOSE 3306
