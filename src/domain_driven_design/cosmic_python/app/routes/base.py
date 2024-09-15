from .utils import create_blueprint_version


base_route = create_blueprint_version(name="base", prefix="", version="v1")


@base_route.route("/")
def get_base():
    return "Cosmic Python DDD."