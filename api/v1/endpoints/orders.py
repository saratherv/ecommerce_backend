import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null
from core.database import models
from core.database.database import db
import random

class OrdersView(views.MethodView):

    def get() -> dict:
        return {}
    
    def post() -> dict:
        request_body = flask.request.get_json()

        #Discount calculkation Here
        discount_percent, discount_amount = 0, 0
        all_orders = db.session.query(models.Orders.order_number.distinct()).all()
        if (len(all_orders) + 1)%2 == 0:
            discount_percent = 10
        response_object = {"user"  : {}, "items" : [], "Total" : 0}
        order_number = "Ecom" + ''.join(random.choice('0123456789') for _ in range(6))
        user_id = request_body.get("user_id", None)
        existing_user = db.session.query(models.User).filter(models.User.id == user_id).first()
        response_object["user"] = existing_user.dict()
        if not existing_user:
            abort(400, f"Invalid User ID: {user_id}")

        if "item_id" in request_body:
            item_id = request_body.get("item_id")
            existing_item = db.session.query(models.Items).filter(models.Items.id == item_id).first()
            response_object["items"].append(existing_item.dict())
            if not existing_item:
                abort(400, f"Invalid Item ID: {item_id}")
            if discount_percent > 0:
                discount_amount = (existing_item.price)/10
            
            order = models.Orders(
                item_id=request_body.get("item_id"),
                user_id=request_body.get("user_id"),
                discount=discount_amount,
                order_number=order_number
            )
            response_object["Total"] = response_object["Total"] + existing_item.price - discount_amount
            db.session.add(order)
        else:
            existing_cart_items = db.session.query(models.Cart).filter(models.Cart.user_id == user_id).all()
            if len(existing_cart_items) == 0:
                abort(400, f"Invalid Cart Details")
            for cart_items in existing_cart_items:
                item_data = db.session.query(models.Items).filter(models.Items.id == cart_items.item_id).first()
                response_object["items"].append(item_data.dict())
                if discount_percent > 0:
                    discount_amount = (item_data.price)/10
                order = models.Orders(
                    item_id=cart_items.item_id,
                    user_id=cart_items.user_id,
                    discount=discount_amount,
                    order_number=order_number
                )
                response_object["Total"] = response_object["Total"] + item_data.price - discount_amount
                db.session.add(order)
                # cart_items.delete()
                db.session.delete(cart_items)
        db.session.commit()
        

        #Make Order Response
        return {"payload": {"result": response_object}, "status_code": 201}

class OrdersDetailedView(views.MethodView):

    def get(item_id: str) -> dict:
        return {}
    
    def put(item_id: str) -> dict:
        return {}
    
    def delete(item_id: str) -> dict:
        return {}