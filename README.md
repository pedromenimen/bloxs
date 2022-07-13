# Teste técnico bloxs

Para usar localmente a aplicação são necessários os seguintes passos:
- Setar algumas váriaveis de ambiente importantes no arquivo .env que pode ser criado com o que estiver no .env.example.
- A única informação que julguei ser sensível é SECRET, que é a chave de segurança a ser usada no jwt.
- O CLEARDB_DATABASE_URL é a url que o flask utilizará para acessar o banco, as informações entre chaves devem ser alteradas para que funcione da maneira correta localmente.
- Criar e entrar no ambiente virtual.
- Instalar as dependências (pip install -r requirements.txt).
- Gerar migrações iniciais (flask db migrate).
- Aplicar as migrações no banco (flask db upgrade).
- Rodar a aplicação localmente (flask db run).

O teste consiste em uma aplicação backend capaz de realizar criação de usuário conta e transações.

Para testar as funcionalidades de cada endpoint da api, há uma [documentação interativa](https://bloxs-flask-mysql.herokuapp.com) na url base da aplicação, que está hospedada na nuvem, utilizando os serviços do heroku.

Para testar rotas autenticadas na documentação, basta usar a rota de registro para criar um usuário, fazer o login e copiar o token para o input escrito api-token e clicar em set, como na imagem.

![Alt text](/app/assets/auth.png?raw=true "Optional Title")