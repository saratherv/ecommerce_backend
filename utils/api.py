from dataclasses import dataclass
import connexion
import uuid
from flask import (
    request, g
)

@dataclass
class APIEndpoint:
    name: str 
    description: str 
    specification: str 
    base_path: str 
    resolver: connexion.resolver.MethodViewResolver