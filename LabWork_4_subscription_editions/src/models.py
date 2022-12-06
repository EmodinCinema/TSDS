from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"


class Recipient(BaseModel):
    __tablename__ = "recipient"

    id_Recipient = Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True)
    Surname = Column(String, index=True)
    Patronymic = Column(String, index=True)
    Recipient_code = Column(Integer, index=True)
    Outside = Column(String, index=True)
    House_number = Column(String, index=True)
    Apartment_number = Column(String, index=True)
    subscription = relationship("Subscription")


class Subscription(BaseModel):
    __tablename__ = "subscription"

    id_Subscription = Column(Integer, primary_key=True, index=True)
    Subscription_period = Column(Integer, index=True)
    Month_of_delivery_start = Column(Integer, index=True)
    Year_of_delivery_start = Column(Integer, index=True)
    recipient = relationship("Recipient")

    Recipient_FK = Column(Integer,  ForeignKey("recipient.id_Recipient"), nullable=False)
    Editions_FK = Column(Integer, ForeignKey("editions.id_Editions"), nullable=False)


class Editions(BaseModel):
    __tablename__ = "editions"

    id_Editions = Column(Integer, primary_key=True, index=True)
    Titles_of_the_publication = Column(String, index=True)
    Index_of_the_publication = Column(Integer, index=True)
    Type_of_publication = Column(String, index=True)
    The_cost_of_searches_in_months = Column(Integer, index=True)
    subscription = relationship("Subscription")