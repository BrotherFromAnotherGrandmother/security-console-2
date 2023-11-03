# Пульт охраны банка

## Проект позволяет отслеживать:

- Сколько сотрудников в данный момент находится в хранилище банка
- Время нахождения каждого сотрудника
- Длительность и дату всех посещений сотрудника
- Подозрительно ли посещение(алгоритм делает выводы на основании времени нахождения сотрудника в хранилище)


### Как установить

Переменные окружения:
* DEBUG - Логическое значение, которое включает/выключает режим отладки. Если приложение выдает исключение, 
когда DEBUG имеет значение True, Django отобразит подробную обратную трассировку, включая множество метаданных о вашей
среде, например все определенные на данный момент настройки Django (из settings.py).
* DB_HOST - адрес БД нашего конкретного банка
* USER_NAME - имя пользователя для подключения к БД
* USER_PASSWORD - пароль пользователя
* DB_NAME - указывает на имя базы данных, с которой наше Django-приложение будет взаимодействовать.
Это поле должно содержать имя базы данных, к которой мы хотим подключиться на сервере баз данных.
* SECRET_KEY - Секретный ключ для конкретной установки Django. Он используется для обеспечения
криптографической подписи и должен быть установлен на уникальное значение.

Python 3.9.6 должен быть уже установлен. 

Установите виртуальное окружение
```
python -m venv venv
```
Актвируйте виртуальное окружение. На macOS команда выглядит следующим образом:
```commandline
source venv/bin/activate 
```
Клонируйте репозиторий
```
git clone https://github.com/BrotherFromAnotherGrandmother/security-console-2
```
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте файл .env в корне проекта
```commandline
touch .env
```
Определите в нём переменные среды следующим образом:

DEBUG=```True``` or ```False```  
DB_HOST = название вашего БД хоста 
USER_NAME = имя пользователя для подключения к БД  
USER_PASSWORD = пароль пользователя    
DB_NAME = имя БД к которой мы хотим подключиться на сервере баз данных  
SECRET_KEY = Ваш секретный ключ    

Запустите проект командой
```
python manage.py runserver 0.0.0.0:8000
```
При успешном запуске откроется похожая страничка:  
![successful deployment](successful deployment.png)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).