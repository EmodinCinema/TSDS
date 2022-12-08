from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
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
    __tablename__ = "recipients"
    """
        Класс Получателя, описаны его поля и методы 
    """
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    patronymic = Column(String, index=True)
    recipient_code = Column(Integer, index=True, unique=True)
    outside = Column(String, index=True, nullable=False)
    house_number = Column(String, index=True, nullable=False)
    apartment_number = Column(String, index=True, nullable=False)
    subscription = relationship("Subscription",  back_populates="recipient")


class Subscription(BaseModel):
    __tablename__ = "subscriptions"
    """
        Класс Подписка, описаны его поля и методы 
    """
    subscription_period = Column(Integer, index=True, unique=True)
    month_of_delivery_start = Column(Integer, index=True, unique=True)
    year_of_delivery_start = Column(Integer, index=True, unique=True)
    recipient = relationship("Recipient", back_populates="subscription")
    edition = relationship("Edition", back_populates="subscriptions")

    recipient_id = Column(Integer,  ForeignKey("recipients.id"), nullable=False)
    edition_id = Column(Integer, ForeignKey("editions.id"), nullable=False)


class Edition(BaseModel):
    __tablename__ = "editions"
    """
        Класс Издание, описаны его поля и методы 
    """
    titles_of_the_publication = Column(String, index=True, nullable=False)
    index_of_the_publication = Column(Integer, index=True, unique=True)
    type_of_publication = Column(String, index=True)
    the_cost_of_searches_in_months = Column(Float, index=True)
    subscription = relationship("Subscription", back_populates="edition")
