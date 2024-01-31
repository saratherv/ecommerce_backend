import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null
from core.database import models
from core.database.database import db

class CartView(views.MethodView):

    def get() -> dict:
        return {}
    
    def post() -> dict:
        request_body = flask.request.get_json()
        for field in ("item_id", "user_id"):
            if not request_body.get(field, None):
                abort(400, f"Missing field: {field}")
        item_id = request_body.get("item_id")
        existing_item = db.session.query(models.Items).filter(models.Items.id == item_id).first()
        if not existing_item:
            abort(400, f"Invalid Item ID: {item_id}")
        
        user_id = request_body.get("user_id")
        existing_user = db.session.query(models.User).filter(models.User.id == user_id).first()
        if not existing_user:
            abort(400, f"Invalid User ID: {user_id}")

        cart = models.Cart(
            item_id=request_body.get("item_id"),
            user_id=request_body.get("user_id")
        )
        db.session.add(cart)
        db.session.commit()
        discount = False
        discount_percent = 0
        all_orders = db.session.query(models.Orders.order_number.distinct()).all()
        if (len(all_orders) + 1)%2 == 0:
            discount_percent = 10
            discount = True
        return {"payload": {"result": {"cart" : cart.dict()}, "discount" : f"You are eligible for {discount_percent}% discount"}, "status_code": 201}

class CartDetailedView(views.MethodView):

    def get(cart_id: str) -> dict:
        return {}
    
    def put(cart_id: str) -> dict:
        return {}
    
    def delete(cart_id: str) -> dict:
        return {}