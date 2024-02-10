<p align="center">
  <img src="https://github.com/amiroudiallo-dev/AirBnB_clone/blob/master/asset/AirBnb.png" alt="AirBnB logo">
</p>

<h1 align="center">AirBnB_clone</h1>
<p align="center">An AirBnB clone.</p>

---

# AirBnB Clone Project
## Part 1 - command interpreter
### Description:
AirBnB is a complete web application, integrating database storage(not yet implemented), a back-end API((not yet implemented), and front-end((not yet implemented) interfacing in a clone of AirBnB.

The project currently only implements the back-end console.
### This project will entail:
* Putting in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
* Creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Creating all classes used for AirBnB (`User`, `State`, `City`, `Place…`) that inherit from `BaseModel`
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine
### How to use it:
1. Start up the console by typing `./console`.
2. Type `help` to see what commands are available.
### Examples:
```
(hbnb)create BaseModel
22442c9d-2df8-4ad6-9877-fbebe5dc38eb
(hbnb)show BaseModel 22442c9d-2df8-4ad6-9877-fbebe5dc38eb
[BaseModel] (22442c9d-2df8-4ad6-9877-fbebe5dc38eb) {'updated_at': datetime.datetime(2018, 6, 13, 14, 39, 8, 949289), 'id': '22442c9d-2df8-4ad6-9877-fbebe5dc38eb', 'created_at': datetime.datetime(2018, 6, 13, 14, 39, 8, 949072)}
```
## Authors :black_nib:
* **DIALLO Amirou Yannick Wendpuire** <[amiroudiallo](https://github.com/amiroudiallo-dev)>
* **Chymezy Josh** <[Chymezy](https://github.com/chymezy)>
