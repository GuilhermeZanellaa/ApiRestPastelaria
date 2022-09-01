from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()


class cliente(BaseModel):
    nome: str
    cpf: str
    telefone: str
    compra_fiado: int = None
    dia_fiado: str = None
    senha: str

# Criar os endpoints de cliente: GET, POST, PUT, DELETE


@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
    return {"msg": "get executado", "id": id}, 200


@router.post("/cliente/{id}", tags=["cliente"])
def post_cliente(id: int, f: cliente):
    return {"msg": "post executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone, "compra_fiado": f.compra_fiado, "dia_fiado": f.dia_fiado, "senha": f.senha}, 200


@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int, f: cliente):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone, "compra_fiado": f.compra_fiado, "dia_fiado": f.dia_fiado, "senha": f.senha}, 201


@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado", "id": id}, 201
