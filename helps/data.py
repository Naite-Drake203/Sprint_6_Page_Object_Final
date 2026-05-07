from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    surname: str
    address: str
    metro: str
    phone: str
    date: str
    comment: str


class Users:
    user = UserData(
        name='Максим',
        surname='Парамонов',
        address='Москва, ул. Льва Толстого, д. 16',
        metro='Парк культуры',
        phone='89190000001',
        date='21.03.2024',
        comment='Хочу быстрее кататься!'
    )

    user_2 = UserData(
        name='Иван',
        surname='Иванов',
        address='Москва, ул. Пресненская набережная, д. 20',
        metro='Парк культуры',
        phone='89994567000',
        date='20.03.2024',
        comment='Давайте поскорее!'
    )
