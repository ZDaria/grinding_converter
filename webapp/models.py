from sqlalchemy import Column, Integer, String, Float
from grinding_converter.webapp.create_db import Base, engine



class GrinderName(Base):
    __tablename__ = "grinder_name"

    id = Column(Integer, primary_key=True)
    name = Column(String)


    def __repr__(self):
        return f"{self.id}, {self.name}"


class CoffeeGriendFraction(Base):

    __tablename__ = "coffee_grind_fraction"

    id = Column(Integer, primary_key=True)
    grinder_name_id = Column(Integer)
    grind_size = Column(Float)
    range_factions_more_900 = Column(Float)
    range_factions_900_600 = Column(Float)
    range_factions_600_300 = Column(Float)
    range_factions_less_300 = Column(Float)

    def __repr__(self):
        return f"{self.id}, {self.grinder_name}, " \
               f"{self.range_factions_more_900}, {self.range_factions_900_600}, " \
               f"{self.range_factions_600_300}, {self.range_factions_less_300}"
