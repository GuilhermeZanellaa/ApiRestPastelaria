from fastapi import APIRouter
from pydantic import BaseModel

# Imports de persistência
import db
from mod_funcionario.FuncionarioModel import FuncionarioDB


class Funcionario(BaseModel):
    id_funcionario: int = None
    nome: str
    matricula: str
    cpf: str
    telefone: str = None
    grupo: int
    senha: str = None


router = APIRouter()


@router.get("/funcionario/", tags=["funcionario"])
def get_funcionario():
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()

# buscar por id


@router.get("/funcionario/{id}", tags=["funcionario"])
def get_funcionario_id(id: int):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


# insere
@router.post("/funcionario/", tags=["funcionario"])
def post_funcionario(corpo: Funcionario):
    try:
        session = db.Session()

        dados = FuncionarioDB(None, corpo.nome, corpo.matricula,
                              corpo.cpf, corpo.telefone, corpo.grupo, corpo.senha)

        session.add(dados)

        session.commit()

        return {"msg": "Cadastrado com sucesso", "id": dados.id_funcionario}, 200

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao cadastrar", "erro": str(e)}, 406

    finally:
        session.close()


# edita
@router.put("/funcionario/{id}", tags=["funcionario"])
def put_funcionario(id: int, corpo: Funcionario):
    try:
        session = db.Session()
        dados = session.query(FuncionarioDB).filter(
            FuncionarioDB.id_funcionario == id).one()

        dados.nome = corpo.nome
        dados.cpf = corpo.cpf
        dados.telefone = corpo.telefone
        dados.senha = corpo.senha
        dados.matricula = corpo.matricula
        dados.grupo = corpo.grupo

        session.add(dados)
        session.commit()

        return {"msg": "Editado com sucesso", "id": dados.id_funcionario}, 201

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406

    finally:
        session.close()


# exclui
@router.delete("/funcionario/{id}", tags=["funcionario"])
def delete_funcionario(id: int):
    try:
        session = db.Session()

        dados = session.query(FuncionarioDB).filter(FuncionarioDB.id_funcionario).one()
        session.delete(dados)
        session.commit()

        return {"msg": "Excluído com sucesso", "id": dados.id_funcionario}, 201
    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406

    finally:
        session.close()
