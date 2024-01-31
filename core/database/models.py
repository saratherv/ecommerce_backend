import json
import os
from datetime import datetime
from uuid import uuid4

# from sqlalchemy import func
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import aliased

from .database import db


class Items(db.Model, SerializerMixin):
    """
    Create an items table
    """

    __tablename__ = "items"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )

class Discount(db.Model, SerializerMixin):
    """
    Create Discount table
    """

    __tablename__ = "discounts"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )

class Cart(db.Model, SerializerMixin):
    """
    Create Cart table
    """

    __tablename__ = "cart"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )

class Orders(db.Model, SerializerMixin):
    """
    Create orders table
    """

    __tablename__ = "orders"

    id = db.Column(
        db.String(32), primary_key=True, nullable=False, default=uuid4().hex
    )
