from fastapi import APIRouter, HTTPException
from ..model import ItemModel


router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not found'}}
)


fake_items_db = {'0001': {'name': 'Item1'}, '0002': {'name': 'Item2'}}


@router.get("", response_model=list[ItemModel])
def read_items():
    return [{'id': k, 'name': v['name']} for k, v in fake_items_db.items()]


@router.get("/{item_id}")
def read_item(item_id: str, response_model=ItemModel):
    if fake_items_db.get(item_id, None) == None:
        raise HTTPException(status_code=404, detail=f"Item with item_id: {item_id} not found")
    else:
        return {'id': item_id, 'name': fake_items_db[item_id]['name']}
