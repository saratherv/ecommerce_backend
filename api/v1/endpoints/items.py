import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null
from core.database import models
from core.database.database import db

class ItemsView(views.MethodView):

    def get() -> dict:
        return {}
    
    def post() -> dict:
        request_body = flask.request.get_json()
        for field in ("item_name", "price"):
            if not request_body.get(field, None):
                abort(400, f"Missing field: {field}")
        item = models.Items(
            item_name=request_body.get("item_name"),
            price=request_body.get("price"),
            description=request_body.get("description")
        )
        db.session.add(item)
        db.session.commit()
        return {"payload": {"result": item.dict()}, "status_code": 201}

class ItemsDetailedView(views.MethodView):

    def get(item_id: str) -> dict:
        return {}
    
    def put(item_id: str) -> dict:
        return {}
    
    def delete(item_id: str) -> dict:
        return {}