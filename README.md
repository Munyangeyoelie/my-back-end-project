# Meta Back-End Developer Capstone

> Little Lemon API is a RESTful API built with Django that serves as the backend for the Little Lemon web application. The API provides endpoints for managing user accounts, reservations, and menu items.

## API Endpoints

### Menus

| Endpoint                | HTTP Method | CRUD Method | Result                 |
| ----------------------- | ----------- | ----------- | ---------------------- |
| `/restaurant/menu/`     | GET         | READ        | Get all menu items     |
| `/restaurant/menu/:id/` | GET         | READ        | Get a single menu item |
| `/restaurant/menu/`     | POST        | CREATE      | Create a new menu item |
| `/restaurant/menu/:id/` | PUT/PATCH   | UPDATE      | Update a menu item     |
| `/restaurant/menu/:id/` | DELETE      | DELETE      | Delete a menu item     |

### Bookings

| Endpoint                          | HTTP Method | CRUD Method | Result               |
| --------------------------------- | ----------- | ----------- | -------------------- |
| `/restaurant/booking/tables`      | GET         | READ        | Get all bookings     |
| `/restaurant/booking/tables/:id/` | GET         | READ        | Get a single booking |
| `/restaurant/booking/tables`      | POST        | CREATE      | Create a new booking |
| `/restaurant/booking/tables/:id/` | PUT/PATCH   | UPDATE      | Update a booking     |
| `/restaurant/booking/tables/:id/` | DELETE      | DELETE      | Delete a booking     |

## License

Little Lemon API is licensed under the Apache License, Version 2.0. See the LICENSE file for details.

## Author

Created by [Mehdi Ait Ouchrif](https://github.com/mehdiaitouchrif).
