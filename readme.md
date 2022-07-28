Restaurant Menu Project

Steps to run the project:

 - create virtual environment
 - install dependencies using `pip install -r requirements\local.txt`
 - run `python manage.py migrate` to create database and tables
 - run `python manage.py runserver` to start the development server

Created 3 Models:
 - Section
 - Item
 - Modifier

Created 3 CRUD APIs for Section, Item and Modifier:

    - Section:
        - create    POST    `/api/section/`
        - readall   GET     `/api/section/`
        - read      GET     `/api/section/<id>`
        - update    PUT     `/api/section/<id>`
        - delete    DELETE  `/api/section/<id>`
    - Item:
        - create    POST    `/api/section/`
        - readall   GET     `/api/section/`
        - read      GET     `/api/section/<id>`
        - update    PUT     `/api/section/<id>`
        - delete    DELETE  `/api/section/<id>`
    - Modifier:
        - create    POST    `/api/section/`
        - readall   GET     `/api/section/`
        - read      GET     `/api/section/<id>`
        - update    PUT     `/api/section/<id>`
        - delete    DELETE  `/api/section/<id>`

Create API to get the whole menu:

    - GET     `/api/menu/`

Sample Response:

    [
        {
            "id": 1,
            "title": "Lunch Specials",
            "items": [
                {
                    "id": 1,
                    "title": "Soup Lunch",
                    "modifiers": [
                        {
                            "id": 1,
                            "title": "Raita"
                        },
                        {
                            "id": 2,
                            "title": "Ketchup"
                        }
                    ]
                },
                {
                    "id": 2,
                    "title": "Biryani",
                    "modifiers": [
                        {
                            "id": 1,
                            "title": "Raita"
                        }
                    ]
                }
            ]
        }
    ]
