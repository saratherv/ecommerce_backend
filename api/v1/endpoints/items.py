import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null


class ItemsView(views.MethodView):

    def get(self) -> dict:
        return {}
    
    def post(self) -> dict:
        return {}

class ItemsDetailedView(views.MethodView):

    def get(self, item_id: str) -> dict:
        return {}
    
    def put(self, item_id: str) -> dict:
        return {}
    
    def delete(self, item_id: str) -> dict:
        return {}