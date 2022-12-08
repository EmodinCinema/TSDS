from pydantic import BaseModel


class RecipientBase(BaseModel):
    """
    Базовый класс для Item
    """
    recipient_code: int

    title: str
    description: str | None = None


class RecipientCreate(RecipientBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Recipient(RecipientBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    name: str
    Surname = str
    Patronymic = str

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


class SubscriptionBase(BaseModel):
    """
    Базовый класс для Item
    """
    title: str
    description: str | None = None


class SubscriptionCreate(SubscriptionBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Subscription(SubscriptionBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    owner_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True


class EditionBase(BaseModel):
    """
    Базовый класс для Item
    """
    title: str
    description: str | None = None


class EditionCreate(EditionBase):
    """
    Класс для создания Item, наследуется от базового ItemBase, но не содержит
    дополнительных полей, пока что
    """
    pass


class Edition(EditionBase):
    """
    Класс для отображения Item, наследуется от базового ItemBase
    поля значения для полей id и owner_id будем получать из БД
    """
    id: int
    owner_id: int

    class Config:
        """
        Задание настройки для возможности работать с объектами ORM
        """
        orm_mode = True
