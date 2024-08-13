from fastapi import APIRouter
from ..model import ItemModel


router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not found'}}
)


fake_items_db : list[ItemModel] = {'id': '0001', 'name': 'Item1'}, {'id': '0002', 'name': 'Item2'}


@router.get("/", response_model=[list[ItemModel]])
def read_items():
    return []