from fastapi import APIRouter, HTTPException
from ..model import ItemModel


router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not found'}}
)


fake_items_db = {'0001': {'name': 'Item1'}, '0002': {'name': 'Item2'}}


@router.get("", response_model=list[ItemModel])
def read_items() -> list[ItemModel]:
    return [{'id': k, 'name': v['name']} for k, v in fake_items_db.items()]


@router.get("/{item_id}")
def read_item(item_id: str) -> ItemModel:
    if not fake_items_db.get(item_id, None):
        raise HTTPException(status_code=404, detail=f"Item with item_id: {item_id} not found")
    else:
        return {'id': item_id, 'name': fake_items_db[item_id]['name']}


@router.put("/{item_id}")
def put_item(item_id: str, item: ItemModel):
    ...
    
    
@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item