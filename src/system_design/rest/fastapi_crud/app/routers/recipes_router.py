from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from ..model import RecipeModel
from .fake_recipes_db import RECIPES_DB, get_recipe_from_db, RecipeSearchType


ROUTER_PREFIX = 'recipes'


router = APIRouter(
    prefix=f"/{ROUTER_PREFIX}",
    tags=[ROUTER_PREFIX],
    responses={404: {'description': 'Not found'}}
)


@router.get("", response_model=list[RecipeModel])
def read_items() -> list[RecipeModel]:
    return RECIPES_DB


@router.get("/{recipe_id}")
def read_item(recipe_id: str) -> RecipeModel:
    found_recipe = get_recipe_from_db(recipe_id, RECIPES_DB)

    if found_recipe:
        return found_recipe
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Recipe with recipe_id: {recipe_id} not found"
        )


@router.post("", response_model=RecipeModel, status_code=201)
def create_item(recipe: RecipeModel):
    new_recipe_id = str(recipe.id)
    found_recipe = get_recipe_from_db(new_recipe_id, RECIPES_DB)

    if found_recipe:
        raise HTTPException(
            status_code=409,
            detail=f"Recipe with recipe_id: {new_recipe_id} already exists"
        )

    new_recipe_name = recipe.name
    found_recipe2 = get_recipe_from_db(new_recipe_name, RECIPES_DB, search_type=RecipeSearchType.name)

    if found_recipe2:
        raise HTTPException(
            status_code=409,
            detail=f"Recipe with name: {new_recipe_name} already exists"
        )

    return recipe


@router.put("/{recipe_id}")
def put_item(recipe_id: str, recipe: RecipeModel):
    found_recipe = get_recipe_from_db(recipe_id, RECIPES_DB)

    if not found_recipe:
        return {404, f"Recipe with recipe_id: {recipe_id} not found"}

    update_recipe_encoded = jsonable_encoder(recipe)
    return update_recipe_encoded


@router.patch("/recipes/{recipe_id}", response_model=RecipeModel)
async def update_item(item_id: str, item: RecipeModel):
    return {500, 'not implemented'}
    # stored_item_data = items[item_id]
    # stored_item_model = Item(**stored_item_data)
    # update_data = item.dict(exclude_unset=True)
    # updated_item = stored_item_model.copy(update=update_data)
    # items[item_id] = jsonable_encoder(updated_item)
    # updated_item = stored_item_model.copy(update=update_data)
    # return updated_item
