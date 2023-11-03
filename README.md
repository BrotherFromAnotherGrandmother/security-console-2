# Пульт охраны банка

## Проект позволяет отслеживать:

- Сколько сотрудников в данный момент находится в хранилище банка
- Время нахождения каждого сотрудника
- Длительность и дату всех посещений сотрудника
- Подозрительно ли посещение(алгоритм делает выводы на основании времени нахождения сотрудника в хранилище)


### Как установить

Переменные окружения:
* DEBUG - показывает, в состоянии ли дебага находится наш сайт
* DB_HOST - адрес БД
* USER_NAME - имя пользователя
* USER_PASSWORD - пароль пользователя
* DB_NAME - имя БД
* SECRET_KEY - секретный ключ

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).