
import fileinput
print("Welcome to my simple program about files!")
x = open("input.txt", "a+")
x.close()

def menux():
    print("Choose the following options: ")
    print("[1] - Read the file")
    print("[2] - Add something in the file")
    print("[3] - Delete something in the file")
    print("[4] - End the program")
    print("[5] - Update ")
    )

def ask_for_input():
    answer = raw_input(">>> ")
    return answer

def read():
    print "The contents of the file are: "
    with open("info.txt", "r") as x:
        print x.read()
    x.close()

def add():
    #add something
    openf = open("info.txt", "a+")
    id_no = raw_input("Enter Id No: ")
    name = raw_input("Name of the Student: ")
    course = raw_input("Course of the student: ")
    student_info = id_no + name + course
    openf.write(student_info)
    openf.close()


def delete():
    x = open("info.txt", "a+")
    output=[]
    delete_student = raw_input("Enter the Id No. You want to delete: ")
    for line in x:
        cur = line.split()
        if(delete_student == cur[0]):
            print("Deleted")
        elif not (delete_student == cur[0]):
            output.append(line)
    x.close()
    x  = open("info.txt", "w")
    x.writelines(output)
    x.close()

def update():
    search_id = raw_input("Select the id no you want to modify/ change the name: ")
    id_update = raw_input("New Id No: ")
    name_update = raw_input("New Name: ")
    course_update = raw_input("New Course: ")
    new_info = id_update + name_update + course_update

menux()

while True:
    try:
        answer = int(ask_for_input())
    except ValueError:
        print "Sorry that's not a number!"
        menux()
        continue

    else:
        if answer in range(1,5):
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
                break
        else:
            print "Out of range! Make sure to type the correct number!"
            menux()







