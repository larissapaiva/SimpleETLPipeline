# ETLPipeline

## Visão Geral

ETLPipeline é um projeto Python que implementa um processo ETL para manipulação e transferência de dados utilizando Flask, SQLAlchemy e Marshmallow. O projeto inclui endpoints para operações CRUD em uma entidade de livro, além de configuração básica de servidor e banco de dados.

### Descrição dos Arquivos e Pastas

- **controllers/**: Contém os controladores que definem as rotas e a lógica de manipulação de requisições.
  - `book.py`: Define os endpoints para operações CRUD na entidade de livro.
- **models/**: Define os modelos de dados e as interações com o banco de dados.
  - `book.py`: Modelo de dados para a entidade de livro.
- **schemas/**: Define os esquemas de serialização/deserialização usando Marshmallow.
  - `book.py`: Esquema de serialização para a entidade de livro.
- **server/**: Configuração do servidor Flask.
  - `instance.py`: Inicializa o servidor Flask e a API Flask-RESTPlus.
- **app.py**: Ponto de entrada principal da aplicação Flask. Configura o servidor, inicializa os recursos e define as rotas.
- **db.py**: Configuração do SQLAlchemy para a manipulação do banco de dados.
- **ma.py**: Configuração do Marshmallow para serialização/deserialização de dados.
- **main.py**: Script separado para configuração e manipulação direta do banco de dados usando SQLAlchemy ORM.

## Como Usar

### Pré-requisitos

- Python 3.6 ou superior
- Flask
- Flask-RESTPlus
- Flask-SQLAlchemy
- Flask-Marshmallow
- Marshmallow

Você pode instalar as dependências utilizando `pip`:

```bash
pip install flask flask-restplus flask-sqlalchemy flask-marshmallow marshmallow
```

### Executando o Projeto

1. **Configuração do Banco de Dados**:
   
   Antes de iniciar o servidor, certifique-se de configurar e criar as tabelas no banco de dados. Execute o script `main.py` para configurar a base de dados e adicionar registros iniciais:

   ```bash
   python main.py
   ```

2. **Iniciando o Servidor**:
   
   Execute `app.py` para iniciar o servidor Flask:

   ```bash
   python app.py
   ```

   O servidor estará disponível em `http://0.0.0.0:5000/` e a documentação da API pode ser acessada em `http://0.0.0.0:5000/api/doc`.

### Endpoints da API

- **/books** [GET]: Retorna a lista de todos os livros.
- **/books** [POST]: Adiciona um novo livro.
- **/books/<int:id>** [GET]: Retorna os detalhes de um livro específico pelo ID.
- **/books/<int:id>** [PUT]: Atualiza os detalhes de um livro específico pelo ID.
- **/books/<int:id>** [DELETE]: Remove um livro específico pelo ID.

### Exemplo de Uso

#### GET /books

```bash
curl -X GET "http://0.0.0.0:5000/books"
```

#### POST /books

```bash
curl -X POST "http://0.0.0.0:5000/books" -H "Content-Type: application/json" -d '{
    "title": "New Book",
    "pages": 100
}'
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório para sugestões de melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
