from .utils import create_blueprint_version


allocation_route = create_blueprint_version(
    name="allocations",
    prefix="allocations",
    version="v1"
)


@allocation_route.route("/")
def get_allocations():
    return []


@allocation_route.route("/<allocation_id>")
def get_allocation(allocation_id: str):
    return {"not implemented", 500}