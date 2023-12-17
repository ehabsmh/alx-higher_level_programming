# Python - Object-relational mapping

### **This directory contains eighteen programs. The programs were written in Python programming language.**

## [0. Get all states](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/0-select_states.py)

Lists all states from the database hbtn_0e_0_usa:

- The program takes 3 arguments: mysql username, mysql password and database name.

---

## [1. Filter states](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/1-filter_states.py)

Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

- The program takes 3 arguments: mysql username, mysql password and database name.

---

## [2. Filter states by user input](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/2-my_filter_states.py)

Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

- The program take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed).

---

## [3. SQL Injection...](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)

Takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time it is safe from MySQL injections!

---

## [4. Cities by states](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/4-cities_by_state.py)

Lists all cities from the database hbtn_0e_4_usa.

---

## [5. All cities by state](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/5-filter_cities.py)

Takes in the name of a state as an argument and lists all cities of that state.

---

## [6. First state model](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/model_state.py)

Contains the class definition of a State and an instance Base = declarative_base():
State class:

- inherits from Base Tips.
- links to the MySQL table states.
- class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key.
- class attribute name that represents a column of a string with maximum 128 characters and can’t be null.

---

## [7. All states via SQLAlchemy](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)

Lists all State objects.

- The program takes 3 arguments: mysql username, mysql password and database name.

---

## [8. First state](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)

Prints the first State object.

---

## [9. Contains `a`](https://github.com/ehabsmh/alx-higher_level_programming/blob/main/0x0F-python-object_relational_mapping/9-model_state_filter_a.py)

Lists all State objects that contain the letter a from the database hbtn_0e_6_usa

- The program takes 3 arguments: mysql username, mysql password and database name.
- Results must be sorted in ascending order by states.id.
