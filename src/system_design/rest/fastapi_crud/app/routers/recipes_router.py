from fastapi import APIRouter, HTTPException
from ..model import RecipeModel
from .fake_recipes_db import RECIPES_DB, get_recipe_with_id


ROUTER_PREFIX = 'recipes'


router = APIRouter(
    prefix=f"/{ROUTER_PREFIX}",
    tags=[ROUTER_PREFIX],
    responses={404: {'description': 'Not found'}}
)


@router.get("", response_model=list[RecipeModel])
def read_items() -> list[RecipeModel]:
    return [{'id': k, 'name': v['name']} for k, v in RECIPES_DB.items()]


@router.get("/{recipe_id}")
def read_item(recipe_id: str) -> RecipeModel:
    found_recipe = get_recipe_with_id(recipe_id)

    if found_recipe:
        return found_recipe
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with recipe_id: {recipe_id} not found"
        )


@router.put("/{recipe_id}")
def put_item(recipe_id: str, item: RecipeModel):
    return {500, 'not implemented'}
    
    
@router.patch("/recipes/{recipe_id}", response_model=RecipeModel)
async def update_item(item_id: str, item: RecipeModel):
    return {500, 'not implemented'}
    #stored_item_data = items[item_id]
    #stored_item_model = Item(**stored_item_data)
    #update_data = item.dict(exclude_unset=True)
    #updated_item = stored_item_model.copy(update=update_data)
    #items[item_id] = jsonable_encoder(updated_item)
    #updated_item = stored_item_model.copy(update=update_data)
    #return updated_item
