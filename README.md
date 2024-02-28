# Дипломная работа профессии «Python-разработчик с нуля»

## Backend приложения для социальной сети для обмена фотографиями

## Цель дипломной работы

Разработка API для загрузки публикаций и их фото с возможностью комментировать и ставить лайки.

В результате выполнения этого задания вы:

* закрепите навыки работы с моделями,
* научитесь правильно работать с сериализацией/десериализацией данных,
* получите навыки правильного проектирования API: создание эндпоинтов, использование нужных методов,
* примените полученные знания в реальном проекте для портфолио.

------

## Чек-лист готовности к работе над проектом

1. Установите Python 3.x и любую IDE. Рекомендуем работать с Pycharm.
2. Установите и настройте СУБД PostgreSQL.
3. Установите Git и создайте аккаунт на GitHub.
4. Скачайте проект, создайте виртуальное окружение и установите сторонние модули.
5. Создайте БД и внесите настройки БД в settings.py.

-----

## Реализация

Посты должны состоять из текста и фотографии, также должно сохраняться время создания поста.

Публикации могут создаваться только авторизованными пользователями, редактировать же публикацию может только её автор.

Комментарии могут быть написаны к определённой публикации, оставлять их могут только авторизованные пользователи. 
Сам комментарий состоит из текста и даты его публикации.

Помимо комментариев, пользователи также могут оставлять реакцию на публикацию в виде лайка.

При получении деталей публикации помимо полей самой публикации должен отображаться список комментариев и количество 
лайков к публикации, например:

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

<details>
  <summary>Подсказки</summary>
  
* для создания пользователей и получения токенов авторизации можете воспользоваться административной панелью,

* чтобы правильно работали загрузка и отображение фото, не забудьте настроить media и 
static пути, а также [привязать их в urls](https://docs.djangoproject.com/en/5.0/howto/static-files/#serving-static-files-during-development),
* для получения связанных объектов пользуйтесь [related_name](https://django.fun/docs/django/5.0/topics/db/queries/#backwards-related-objects), 
а для подсчёта количества - используйте метод [count()](https://django.fun/docs/django/5.0/ref/models/querysets/#django.db.models.query.QuerySet.count),
* для сериализации связанных объектов используйте [вложенную сериализацию](https://ilyachch.gitbook.io/django-rest-framework-russian-documentation/overview/navigaciya-po-api/relations#vlozhennye-otnosheniya)

</details>

## Дополнительные задачи

_(необязательные к выполнению, не влияют на получение зачёта)_

* Реализуйте возможность загрузки нескольких фотографий к одной публикации. 
* Реализуйте получение и сохранение геоданных публикации. При создании публикации пользователь может ввести необходимую локацию: страна, город, улица, достопримечательность или здание. По указанному объекту необходимо получить географические координаты (широта и долгота). Для этого вы можете воспользоваться модулем [geopy](https://geopy.readthedocs.io/en/latest/#installation), методом `geocode()`. При отображении, наоборот, по координатам отобразить название объекта, используя метод `reverse()`.

-----

### Правила сдачи работы

Исходный код программы загружен на GitHub.

-----

## Критерии оценки

Зачёт по дипломной работе можно получить, если работа соответствует критериям:

* система реализована на Django версии 3 и выше,
* интерфейс администратора создан стандартными средствами Django admin,
* в качестве СУБД использован postgresql,
* реализованы все необходимые модели и сериализаторы,
* система при работе не должна вызывать исключения и ошибки,
* описана документация по запуску проекта.

Работа направляется на доработку при несоответствии одному и более критериям.
