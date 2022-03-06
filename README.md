# AirBnB clone

<p align="center">
    <video src="https://www.youtube.com/watch?v=p00ES-5K4C8&t=4s">
</p>

## Presentation

This project is the first step towards building an AirBnB clone.
Consists of a custom command-line interface for data management and the base classes for the storage of this data.

## Operation an examples

The console works both in interactive mode and non-interactive mode. Its usage is like a Linux shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run  | ```./console.py```
Quit | ```(hbnb) quit```
Help for a command | ```(hbnb) help <command>```
Create object | ```(hbnb) create <class>```
Update an attribute | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```
Show object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Show all of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Destroy object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```


## Models folder

The folder [models](./models/) has the classes used in this project.

File | Description | Attributes
---- | ----------- | ----------
[base_model.py](./models/base_model.py) | BaseModel class. It is the parent calss | id, created_at, updated_at
[user.py](./models/user.py) | User class for user information | first_name, last_name, email, password
[amenity.py](./models/amenity.py) | Amenity class information | name
[city.py](./models/city.py) | City class information | state_id, name
[state.py](./models/state.py) | State information | name
[place.py](./models/place.py) | Place accomodation information | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[review.py](./models/review.py) | Review class for user review information | place_id, user_id, text

## Storage

The folder [engine](./models/engine/) is incharge of the serialization and deserialization of all the data. It follows a JSON format.

The class is defined in [file_storage.py](./models/engine/file_storage.py) and has the following structure:
```<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>```

The [__init__.py](./models/__init__.py) file contains the instantiation of the FileStorage class. This allows the storage to be reloaded automatically and recovers the serialized data.

## Testing

The code is tested with the **unittest** module.
The tests are in the [test_models](./tests/test_models/) folder.

## Authors
- **Matías López** [matias.lopez@holbertonschool.com](https://github.com/Matilop15)
- **Raymundo Barrera Flores** - [raymundo.barrera-flores@holbertonschool.com](https://github.com/RayBar72)
