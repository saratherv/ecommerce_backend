import flask
from flask import views, abort, request, current_app
from sqlalchemy.sql import null
from core.database import models
from core.database.database import db

class DiscountView(views.MethodView):

    def get() -> dict:
        all_orders = db.session.query(models.Orders.order_number.distinct()).all()
        if (len(all_orders) + 1)%2 == 0:
            discount_percent = 10
        return {"payload": {"result":  {}, "discount" : f"You are eligible for {discount_percent}% discount, Use Code APPLY{10}"}, "status_code": 200}
