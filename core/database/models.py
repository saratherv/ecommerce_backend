import json
import os
from datetime import datetime
from uuid import uuid4

# from sqlalchemy import func
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import aliased

from .database import db

class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), index=True, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow())

    @staticmethod
    def join_criterion() -> dict:
        return {}

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name})"

    @staticmethod
    def dict_keys() -> tuple:
        return ("id", "name", "email", "created_at", "last_updated")


class Items(db.Model, SerializerMixin):
    """
    Create an items table
    """

    __tablename__ = "items"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )
    item_name = db.Column(db.String(256), unique=True, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    description = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow())

    @staticmethod
    def join_criterion() -> dict:
        return {}

    def __repr__(self) -> str:
        return f"Items(id={self.id}, name={self.item_name})"

    @staticmethod
    def dict_keys() -> tuple:
        return ("id", "item_name", "price", "description", "created_at", "last_updated")


# class Discount(db.Model, SerializerMixin):
#     """
#     Create Discount table
#     """

#     __tablename__ = "discounts"

#     id = db.Column(
#         db.String(32), primary_key=True, nullable=False, default=uuid4().hex
#     )

class Cart(db.Model, SerializerMixin):
    """
    Create Cart table
    """

    __tablename__ = "cart"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.String(32), db.ForeignKey("items.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow())

    @staticmethod
    def join_criterion() -> dict:
        return {
            "User" : (User, User.id == Cart.user_id),
            "Items" : (Items, Items.id == Cart.item_id)
        }

    def __repr__(self) -> str:
        return f"Cart(id={self.id})"

    @staticmethod
    def dict_keys() -> tuple:
        return ("id", "user_id", "item_id", "created_at", "last_updated")

class Orders(db.Model, SerializerMixin):
    """
    Create orders table
    """

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    order_number = db.Column(
        db.String(32), nullable=False, default=uuid4().hex
    )
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    item_id = db.Column(db.String(32), db.ForeignKey("items.id"))
    discount = db.Column(db.Numeric(precision=10, scale=2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated = db.Column(db.DateTime, onupdate=datetime.utcnow())


    @staticmethod
    def join_criterion() -> dict:
        return {
            "User" : (User, User.id == Orders.user_id),
            "Items" : (Items, Items.id == Orders.item_id)
        }

    def __repr__(self) -> str:
        return f"Order(id={self.id})"

    @staticmethod
    def dict_keys() -> tuple:
        return ("id", "order_number", "user_id", "item_id", "discount", "created_at", "last_updated")