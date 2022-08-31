from fastapi import APIRouter
router = APIRouter()
# Criar os endpoints de Cliente: GET, POST, PUT, DELETE
@router.get("/cliente/{id}", tags=["cliente"])
def get_cliente(id: int):
    return {"msg": "get executado"}, 200

@router.post("/cliente/{id}", tags=["cliente"])
def post_cliente(id: int):
    return {"msg": "post executado"}, 200

@router.put("/cliente/{id}", tags=["cliente"])
def put_cliente(id: int):
    return {"msg": "put executado"}, 201

@router.delete("/cliente/{id}", tags=["cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201