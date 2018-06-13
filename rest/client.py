import requests as r
import json
import time
URL='http://127.0.0.1:8001/api/studios'
def bodrder():
	print("\n-----------------------")


print('Просмотр всех записей;')
print(r.get(URL).text)
bodrder()

print('Просмотр конкретной записи(успешно)')
print(r.get(URL+'/7').text)
bodrder()

print('Просмотр конкретной записи(неуспешно-такого пользователя нет)')
print(r.get(URL+'100500').text)
bodrder()

print('Сортировка по имени  по убываню')
print(r.get(URL,params={'order':'d'}).text)
bodrder()

print('Сортировка по имени  по возрастанию')
print(r.get(URL,params={'order':'a'}).text)
bodrder()

print('Фильтрация по всем полям')
print(r.get(URL,params={'filter':'Дубай'}).text)
bodrder()

print('Пагинация ')
print(r.get(URL,params={'pagination':'5'}).text)
bodrder()

print('Средняя оценка фильмов студий ')
print(r.get(URL+'/avg_rate').text)
bodrder()

print('Добавление студии-ошибка(ничего не передаем же)')
print(r.post(URL).text)
bodrder()

print('Добавление студии(всё хорошо)')
print(r.post(URL, json={'name':'5','country':'5','city':'5'}).text)
bodrder()

print('Обновление записи')
print(r.put(URL+'/1',json={'name':'6','country':'5','city':'5'}).text)
bodrder()

print('Удаление студии(Таблицы связаны,поэтому 406)')
print(r.delete(URL+'/1').text)
bodrder()




