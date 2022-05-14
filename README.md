# kamailio_autenticacao_usuarios_api_rest
Kamailio - Autenticação de usuários baseada em API REST. 

<h3>Build</h3>

```bash
make build
```

<h3>Start up</h3>

```bash
make up
```

<h3>Stop</h3>

```bash
make stop
```

<h3>Step-by-ste</h3>

1. Configurar as variáveis de ambiente do projeto
2. Antes de realizar o start up, descomente as linhas abaixo no arquivo kamailio_autenticacao_usuarios_api_rest/mongodb/collections/initdb.js para que a API possa utilizar o banco de dados com as credenciais escolhidas por você.

```nodejs
/*
use kamailio;
db.createUser({ user: "root",
          pwd: "root_password",
          roles: [ "dbOwner"]});
*/
```
3. Inicialize o projeto
```bash
make up
```

<h3>Serviços</h3>

| Serviço | Descrição |
|---|---|
|Kamailio| SIP proxy utilizado para realizar a autenticação de ramais e intermediar as chamadas entre os usuários.|
|API| API baseada no framework FastAPI para consultar os usuários cadastrados na base de dados.|
|MongoDB| Base de dados onde os usuários serão armazenados.|
|MongoExpress| Frontend para gerenciamento do MongoDB.|
