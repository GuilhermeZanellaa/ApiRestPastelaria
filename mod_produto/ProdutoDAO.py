from fastapi import APIRouter
from pydantic import BaseModel

# Imports de persistĂȘncia
from fastapi import Depends
import security
import db
from mod_produto.ProdutoModel import ProdutoDB


class Produto(BaseModel):
    codigo: int = None
    nome: str
    descricao: str
    foto: bytes
    valor_unitario: float


# dependĂȘncias de forma global para pedir usuario e senha para usar o swagger
router = APIRouter(dependencies=[Depends(
    security.verify_token), Depends(security.verify_key)])


@router.get("/produto/", tags=["produto"])
def get_produto():
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto).all()
        return dados, 200
    except Exception as e:
        return {"msg": "Erro ao listar", "erro": str(e)}, 404
    finally:
        session.close()


@router.post("/produto/", tags=["produto"])
def post_produto(corpo: Produto):
    try:
        session = db.Session()

        dados = ProdutoDB(None, corpo.nome, corpo.descricao,
                          corpo.foto, corpo.valor_unitario)

        session.add(dados)
        session.commit()

        return {"msg": "Cadastrado com sucesso", "id": dados.id_produto}, 200

    except Exception as e:
        session.rollback()

    finally:
        session.close()


@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, corpo: Produto):
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).filter(
            ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario

        session.add(dados)
        session.commit()

        return {"msg": "Editado com sucesso", "id": dados.id_produto}, 201

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao editar", "erro": str(e)}, 406
    finally:
        session.close()


@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto).one()
        session.delete(dados)
        session.commit()

        return {"msg": "ExcluĂ­do com sucesso", "id": dados.id_produto}, 201

    except Exception as e:
        session.rollback()
        return {"msg": "Erro ao excluir", "erro": str(e)}, 406
    finally:
        session.close()
