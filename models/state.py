#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """Getter for list of City instances related to State"""
            citys = models.storage.all(City)
            return [c for c in citys.values() if c.state_id == self.id]
