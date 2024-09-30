<h1 align="center">Lista Telefônica - CRUD</h1>

<div align="center">
  <img alt="Logo" src="https://github.com/user-attachments/assets/a3825788-0199-431a-bb87-b4f493ee0828">
</div>

## About 📝

Este projeto é uma aplicação de lista telefônica simples que permite gerenciar contatos usando o banco de dados NoSQL MongoDB. Através de um menu interativo, o usuário pode criar, listar, atualizar e deletar contatos diretamente na coleção MongoDB.

## Funcionalidades ⚙️

O projeto permite as seguintes operações:

1. **Criar Contato**: Adiciona um novo contato à lista com nome e telefone.
2. **Listar Contatos**: Exibe todos os contatos armazenados, mostrando o `ID`, nome e telefone.
3. **Atualizar Contato**: Permite a atualização de um contato existente com base no seu `ID`.
4. **Deletar Contato**: Remove um contato com base no seu `ID`.
5. **Sair**: Encerra a aplicação.

## Tecnologias Utilizadas 💻

- **Python**
- **MongoDB** como banco de dados NoSQL
- **Biblioteca pymongo** para interação com o MongoDB
- **bson** para trabalhar com `ObjectId`

## Como Executar o Projeto ▶️

### Pré-requisitos

1. **Python 3.x** instalado.
2. **MongoDB Atlas**: Necessário ter uma conta e uma coleção criada para armazenar os contatos.
3. **Bibliotecas pymongo e bson**:
   - Instale o `pymongo` usando o seguinte comando:

```bash
pip install pymongo
```
