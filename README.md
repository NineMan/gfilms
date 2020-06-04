Тестовое задание от **Expotestdrive** на позицию 

Программист Python (Junior)
---

Тестовая задача:

**Публичный апи и получение списка фильмов Гибли**

1. Сделать апи, возвращающее данные из стороннего сервиса, обогащенные данными из своей базы данных.
Примеры публичных сторонних сервисов откуда можно взять данные: https://github.com/public-apis/public-apis
2. Своя база данных может использовать MySQL, PostreSQL или MongoDB.
Один из вариантов: использовать публичный апи для получения списка фильмов Гибли или комиксов Марвел, а из локальной базы брать локализованные названия на русском языке.

По окончании поднять на тестовом сервере.
---

Результат:
==========

[Тестовый сервер](https://ninemantest.pythonanywhere.com/api/film/58611129-2dbc-4a81-a72f-77ddfc1b1b49)

Сервис возвращает данные из сервиса [фильмов Гибли](https://ghibliapi.herokuapp.com/), проверяет наличие в своей базе русского названия фильма и добавляет к выдаче русское название или null.

Сервис поддерживает работу только по оригинальным film ID (список фильмов не поддерживается).
Т.е. работают только такие ссылки:
<https://ninemantest.pythonanywhere.com/api/film/58611129-2dbc-4a81-a72f-77ddfc1b1b49>
<https://ninemantest.pythonanywhere.com/api/film/ebbb6b7c-945c-41ee-a792-de0e43191bd8>
<https://ninemantest.pythonanywhere.com/api/film/2baf70d1-42bb-4437-b551-e5fed5a87abe>




