from fastapi import APIRouter

from database.transferservice import create_transaction_db, cancel_transaction_db, get_history_transactions

from transfers import CancelTransctionValidator, CreateTransctionValidator

trans_router = APIRouter(prefix='/transfers', tags=['Транзакции'])

# Запрос на создание транзакции
@trans_router.post('/create')
async def add_new_transaction(data:CreateTransctionValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка'}

# Запрос на историю перевода
@trans_router.get('/history')
async def history_trans(card_id: int):
    result = get_history_transactions(card_from_id=card)

    if result:
        return result
    else:
        return {'message': 'Ошибка'}

# Запрос на отмену транзакции
@trans_router.post('/cancel')
async def cancel_trans(data: CancelTransctionValidator):
    cancel_data = data.model_dump()
    result = cancel_transaction_db(**cancel_data)

    if result:
        return {'message': result}
    else:
        return {'messasge': 'Ошибка'}