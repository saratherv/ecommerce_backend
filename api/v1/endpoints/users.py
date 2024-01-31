import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null
from core.database import models
from core.database.database import db

class UsersView(views.MethodView):

    def get() -> dict:
        return {}
    
    def post() -> dict:
        request_body = flask.request.get_json()
        for field in ("name", "email"):
            if not request_body.get(field, None):
                abort(400, f"Missing field: {field}")
        user = models.User(
            name=request_body.get("name"),
            email=request_body.get("email")
        )
        db.session.add(user)
        db.session.commit()
        return {"payload": {"result": user.dict()}, "status_code": 201}

class UsersDetailedView(views.MethodView):

    def get(user_id: int) -> dict:
        return {}
    
    def put(user_id: int) -> dict:
        return {}
    
    def delete(user_id: int) -> dict:
        return {}