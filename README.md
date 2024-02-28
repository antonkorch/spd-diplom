# Дипломный проект по курсу Основы Django "Мини социальная сеть"

## Описание 

Необходимо разработать небольшое API для загрузки публикаций и их фото 
с возможностью комментировать и ставить лайки.


## Реализация 

Посты должны состоять из текста и фотографии, также должно сохраняться время создания поста.

Публикации могут создаваться только авторизованными пользователями, редактировать же публикацию может только её автор.

Комментарии могут быть написаны к определённой публикации, оставлять их могут только авторизованные пользователи. 
Сам комментарий состоит из текста и даты его публикации.

Помимо комментариев, пользователи также могут оставлять реакцию на публикацию в виде лайка.

При получении деталей публикации помимо полей самой публикации должен отображаться список комментариев и количество 
лайков к публикации. Например:

```json
{
  "id": 1,
  "text": "Новый прекрасный день",
  "image": "/posts/image1.jpg",
  "created_at": "2024-02-23T02:24:29.338414",
  "comments": [
    {
      "author": 2,
      "text": "Круто",
      "created_at": "2024-02-23T05:12:31.054234"
    }
  ],
  "likes_count": 20
}
```

## Чеклист готовности к работе над проектом
1. У вас установлен Python 3.x и любая IDE. Мы рекомендуем работать с Pycharm.
2. Установлена и настроена СУБД PostgreSQL
3. Установлен git и создан аккаунт на Github
4. Скачан проект, создано виртуальное окружение и установлены сторонние модули
5. Создана БД и внесены настройки БД в settings.py


## Подсказки
* для создания пользователей и получения токенов авторизации Вы можете воспользоваться админ панелью

* чтобы правильно работали загрузка и отображение фото, не забудьте настроить media и 
static пути, а также [привязать их в urls](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development)

* для получения связанных объектов пользуйтесь [related_name](https://django.fun/docs/django/5.0/topics/db/queries/#backwards-related-objects), 
а для подсчёта количества используйте метод [count()](https://django.fun/docs/django/5.0/ref/models/querysets/#django.db.models.query.QuerySet.count)

* для сериализации связанных объектов используйте [вложенную сериализацию](https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/relations#vlozhennye-otnosheniya)

## Критерии оценки

* Система должна быть реализована на Django версии 3 и выше.
* Интерфейс администратора должен быть создан стандартными средствами Django admin.
* В качестве СУБД использовать postgresql.
* Реализованы все необходимые модели и сериализаторы
* Система при работе не должна вызывать исключений и ошибок.
* Описана небольшая документация по запуску проекта

## Что необходимо предоставить по проекту

* Исходный код программы, загруженный на Github


## Дополнительные задачи

* Реализовать возможность загрузки нескольких фотографий к одной публикации. 
* Реализовать получение и сохранение геоданных публикации. При создании публикации пользователь может ввести необходимую
локацию: страна, город, улица, достопримечательность или здание. По указанному объекту необходимо получить географические
координаты (широта и долгота), для этого Вы можете воспользоваться модулем [geopy](https://geopy.readthedocs.io/en/latest/#installation)
, метод geocode(). При отображении, наоборот, по координатам отобразить название объекта, используя метод reverse()
