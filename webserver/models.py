from webserver.database import Base
from sqlalchemy import(
    Column,
    Integer,
    String,
    Float
)


class OfferModel(Base):
	__tablename__ = "Offers"

	id = Column(Integer, primary_key=True, autoincrement=True)
	url = Column(String(160))
	title = Column(String(60), unique=False, nullable=False)
	image = Column(String(120), nullable=False)
	price = Column(String(60), nullable=False)
	location = Column(String(60), nullable=False)
    
	def __init__(self, url, title, image, price, location):
		self.url = url
		self.title = title
		self.image = image
		self.price = price
		self.location = location
