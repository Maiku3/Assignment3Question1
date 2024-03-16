import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="A3Q1Database",
    user="postgres",
    password="password", # put your password here
    host="localhost",
    port="5432"  # default port
)

# Create a cursor object
cur = conn.cursor()

# Retrieves and displays all records from the students table.
def getAllStudents():
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for s in students:
        print(s)

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()

# Test the functions
print("All students:")
getAllStudents()

addStudent("Mike", "Lin", "mikelin@cmail.carleton.ca", "2021-09-01")
print("\nAfter adding new student:")
getAllStudents()

updateStudentEmail(3, 'new.jim@example.com')
print("\nAfter updating Jim's email:")
getAllStudents()

deleteStudent(3)
print("\nAfter deleting Jim:")
getAllStudents()

# Close the cursor and connection
cur.close()
conn.close()