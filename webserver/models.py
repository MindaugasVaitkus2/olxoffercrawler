from webserver.database import Base
from sqlalchemy import(
    Column,
    Integer,
    String
)


class OfferModel(Base):
    __tablename__ = "Offers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(250))
    title = Column(String(250), unique=False, nullable=False)
    image = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    location = Column(String(250), nullable=False)

    def __init__(self, url, title, image, price, location):
        self.url = url
        self.title = title
        self.image = image
        self.price = price
        self.location = location
    
    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self):
        return hash((
            self.id,
            self.url,
            self.title,
            self.image,
            self.price,
            self.location
        ))
