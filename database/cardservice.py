from database.models import UserCard

from datetime import datetime

from database import get_db


# Добавления карты
def add_card_db(user_id, card_number, card_name, balance, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number, card_name=card_name,
                        balance=balance, exp_date=exp_date)

    if new_card:
        db.add(new_card)
        db.commit()

        return 'Катра успешно добавлено!!!'
    else:
        return 'Ошибка брат('


# Вывести все карты определенного пользователя
def get_exact_user_card_db(user_id):
    db = next(get_db())

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()

    if exact_user_card:
        return exact_user_card
    else:
        return 'Ну нету такого пользователя('


# Вывести определенную карту определенного пользователя
def get_exact_card_user_db(user_id, card_id):
    db = next(get_db())

    exact = db.query(UserCard).filter_by(user_id=user_id, card_id=card_id).first()

    if exact:
        return exact
    else:
        return 'БРат нету такого карты или пользователя(('


# Проверка карты на наличие в БД
def check_card_db(card_number):
    db = next(get_db())

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    if checker:
        return checker
    else:
        return 'Нету такого карты в БД('


# Удаления карты
def delete_card_db(card_id):
    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete(delete_card)
        db.commit()

        return 'Карта успешно удалена!'
    else:
        return 'Карта не найдено(('

# Изменения информаций на карте(На ваше усмотрения)