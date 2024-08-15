from fastapi import APIRouter, HTTPException
from ..model import RecipeModel


ROUTER_PREFIX = 'recipes'


router = APIRouter(
    prefix=f"/{ROUTER_PREFIX}",
    tags=[ROUTER_PREFIX],
    responses={404: {'description': 'Not found'}}
)


fake_items_db = {'0001': {'name': 'Item1', 'description': "This is a recipe"}, '0002': {'name': 'Item2', 'description': "This is a recipe"}}


@router.get("", response_model=list[RecipeModel])
def read_items() -> list[RecipeModel]:
    return [{'id': k, 'name': v['name']} for k, v in fake_items_db.items()]


@router.get("/{item_id}")
def read_item(item_id: str) -> RecipeModel:
    if not fake_items_db.get(item_id, None):
        raise HTTPException(status_code=404, detail=f"Item with item_id: {item_id} not found")
    else:
        return {'id': item_id, 'name': fake_items_db[item_id]['name']}


@router.put("/{item_id}")
def put_item(item_id: str, item: RecipeModel):
    return {500, 'not implemented'}
    
    
@router.patch("/items/{item_id}", response_model=RecipeModel)
async def update_item(item_id: str, item: RecipeModel):
    return {500, 'not implemented'}
    #stored_item_data = items[item_id]
    #stored_item_model = Item(**stored_item_data)
    #update_data = item.dict(exclude_unset=True)
    #updated_item = stored_item_model.copy(update=update_data)
    #items[item_id] = jsonable_encoder(updated_item)
    #updated_item = stored_item_model.copy(update=update_data)
    #return updated_item