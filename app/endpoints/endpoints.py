from fastapi import APIRouter

from app.db.db import db
from app.shemas.shemas import AddShemas, PutSHEMAS

router = APIRouter()


@router.get('/')
async def hello_func():
    return ('Дарова бандиты')


@router.get('/return_db')
async def return_db():
    return db


@router.get('/return_db/{pk}')
async def return_db_int(pk: int):
    for i in db:
        print(i)
        if pk == i:
            return db.get(i)
    return ("Сори такого айди нету")


@router.post('/add_db')
async def add_db(data: AddShemas):
    new_pk = max(db.keys()) + 1
    db[new_pk] = {
        "name": data.name,
        "firstname": data.firstname,
        "date": data.date
    }
    return (f"Записи успешно сохранены с id: {new_pk}")


@router.put('/put_db/{pk}')
async def put_db(pk: int, data: PutSHEMAS):
    for i in db.keys():
        if i == pk:
            db[pk] = {
                "name": data.name,
                "firstname": data.firstname,
                "date": data.date
            }
            return f" Запись с id {db[i]} успешно изменена"
    return f"Запись с id {pk} не найдена"


@router.delete('/del_db/{pk}')
async def del_db(pk: int):
    for i in db:
        if i == pk:
            db.pop(i)
            return f"Запись с id {pk} успешно удалена"
    return (f"Запись с id {pk} отсутствует")
