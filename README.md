<div align="center">
    <img src="frontend/static/img/logo-extenso.png">
</div>

# Descrição
Sistema de batepapo online onde é possível criar salas e interagir com outros usuários ao vivo através de websockets.<br>

# Rodando a aplicação
O projeto tem o docker implementado, para dar um build na aplicação é necessário ter o Docker e o docker-compose instalados em sua maquina.<br> 
Basta rodar os seguinte comando:

<br>

>$ `docker-compose up --build`
<br>

# Visualizando o site
Depois de rodar o sistema, ele estará disponível no <a target="_blank" href="http:127.0.0.1:8000">localhost</a>

![image](https://user-images.githubusercontent.com/90570370/170877319-96d52713-c7d1-474f-9748-d653ce9050e3.png)<br>
![image](https://user-images.githubusercontent.com/90570370/170877367-bf814c03-2308-4597-9223-6de67406efea.png)<br>
![image](https://user-images.githubusercontent.com/90570370/170877448-791ae593-c8cd-4e10-bbbd-e03d8f2d32a7.png)<br>



# Visualizando o banco de dados
O banco de dados é o PostgreSQL e fica disponível na porta 5432, é necessário algum gerenciador para poder visualizar os dados.<br>

Usuário: postgres<br>
Senha: postgres

<br>

# Tecnologias utilizadas
#### Back-End:
 - Python
 - Flask
 - Flask-Socketio

#### Front-End:
 - HTML5
 - JavaScript
 - JQuery
 - Requisições AJAX
 - SocketIO.js
 - CSS3
 - Bootstrap

#### Banco de Dados:
 -  PostgreSQL
