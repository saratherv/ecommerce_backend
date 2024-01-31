import connexion 
import os 
from utils.api import APIEndpoint

api_endpoint = APIEndpoint(
    name = "api-v1",
    description = "API V1 Endpoints",
    specification = os.path.join(os.path.dirname(__file__), "documentation.yaml"),
    base_path = "/api/v1",
    resolver = connexion.resolver.MethodViewResolver("api.v1"),
)


from . import endpoints