"""" This program should be able to do the following:
 > Be able to access a database
 > Update
 > Add
 > and Delete
"""

import psycopg2

def read():
    try:
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute("SELECT * FROM studentlist")
        rows = cur.fetchall()
        for row in rows:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "COURSE = ", row[2], "\n"
        print "Operation done successfully"
        conn.close()
    except Exception as e:
        print e.message
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()


def add():
    print("Please fill up the following: ")
    new_id = raw_input("What is the id No? ")
    new_name = raw_input("What is the name of the Student? ")
    new_course = raw_input("What is the course? ")
    new_info = "'" + new_id + "'," + "'" + new_name + "'," + "'" + new_course + "'"
    values = str(new_info)
    statement = 'INSERT INTO studentlist(ID,NAME, COURSE)' + ' VALUES (' + values + ')'
    try:
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute(statement)
        conn.commit()
        print "Records created successfully";
        conn.close()
    except Exception as e:
        print e.message
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()


def delete():
    del_id = raw_input("What is the id No you want to delete? ")
    del_statement = 'DELETE FROM studentlist WHERE id= ' + "'" + del_id + "'"

    try:
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()

        cur.execute(del_statement)
        conn.commit()
        cur.execute("SELECT * FROM studentlist")
        rows = cur.fetchall()
        for row in rows:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "COURSE = ", row[2], "\n"
        print "Operation done successfully"
        conn.close()
    except Exception as e:
        print e.message
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()


def update():
    old_id = raw_input("What is the Id No of the Student you want to Update? ")
    new_name = raw_input("New name: ")
    new_course = raw_input("New Course: ")

    try:
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute("UPDATE studentlist SET name=(%s), course = (%s) WHERE id = (%s)", (new_name, new_course, old_id,));
        conn.commit()
        print "Total number of rows updated :", cur.rowcount

        cur.execute("SELECT ID, NAME , COURSE from studentlist;")
        rows = cur.fetchall()
        for row in rows:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "COURSE = ", row[2], "\n"
        print "Operation done successfully";
        conn.close()
    except Exception as e:
        print e.message
        conn = psycopg2.connect(database="student", user="postgres", password="123456789", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()


def ask_for_input():
    answer = raw_input(">>> ")
    return answer


def menux():
    print("Choose the following options: ")
    print("[1] - Read the Database")
    print("[2] - Add something in the Database")
    print("[3] - Delete something in the Database")
    print("[4] - Update the database")
    print("[5] - End the Program")


menux()

while True:
    try:
        answer = int(ask_for_input())
    except ValueError:
        print "Sorry that's not a number!"
        menux()
        continue

    else:
        if answer in range(1, 6):
            if (answer == 1):
                read()
                menux()
            elif (answer == 2):
                add()
                menux()
            elif (answer == 3):
                delete()
                menux()
            elif (answer == 4):
                update()
                menux()
            elif (answer == 5):
                break
        else:
            print "Out of range! Make sure to type the correct number!"
            menux()
