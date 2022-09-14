from fastapi import FastAPI
import db

# importe das classes
from mod_funcionario import FuncionarioDAO
from mod_cliente import ClienteDAO
from mod_produto import ProdutoDAO

# importe das classes de modelo de persistência(DB)
from mod_funcionario.FuncionarioModel import FuncionarioDB

# importe das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO

app = FastAPI()

#rotas
app.include_router(FuncionarioDAO.router)
app.include_router(ClienteDAO.router)
app.include_router(ProdutoDAO.router)

# cria, caso não existam, as tabelas de todos os modelos importados
db.criaTabelas()