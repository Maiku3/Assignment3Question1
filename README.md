# COMP 3005 Assignment 3 Question 1

## My Demo Video

- [Demo](https://youtu.be/IBx9pB2eH8g?si=i6WayEXPJucqTLOg)

## Files

* `README.md` - readme.
* `setup_database.txt` - txt file with the provided queries to setup and insert new students in the database.
* `app.py` - Python file with all the functions

## How to set up and run the application: 
You need to first have a PostgreSQL database set up called A3Q1Database, and copy and paste the query in the setup_database.txt into the query tool to create the table and insert the students.

1. Clone the repository and make sure you are in that directory:
```
https://github.com/Maiku3/a3q1.git
```
2. Install psycopg2
```
$ pip install psycopg2
```
3. Edit app.py and put your PostgreSQL password in.

4. Run the app to execute the functions
```
$ python app.py
```