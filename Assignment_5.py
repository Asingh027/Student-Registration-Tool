# Imports
import mysql.connector
from datetime import date

# Connect to MySQL Server
sql = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='assignment6')

cursor = sql.cursor()

# FUNCTIONS


def get_courses(UCID):
    res = []
    query = "SELECT name from course where course_id in (select course_id from registration where student_id = " + str(
        UCID) + ");"
    for q in cursor.execute(query, multi=True):
        result = q.fetchall()
        for r in result:
            res.append(r[0])
        return res


def get_course_names(course_id):
    res = []
    query = "SELECT name from Course WHERE course_id = " + str(course_id)
    for q in cursor.execute(query, multi=True):
        result = q.fetchall()
        for r in result:
            res.append(list(r)[0])
            return res


def registration(UCID):
    query = "SELECT C.name, C.course_id, I.name, I.instructor_id, S.section_id, COUNT(R.student_id) as Count \
        FROM Course C, Section S, Instructor I, Registration R \
            WHERE C.course_id = S.course_id \
                AND S.instructor_id = I.instructor_id \
                    AND R.section_id = S.section_id \
                        GROUP BY S.section_id;"
    for q in cursor.execute(query, multi=True):
        result = q.fetchall()
        cnt = 1
        for r in result:
            r = list(r)
            print("(" + str(cnt) + ") " + str(r[1]) + " - " +
                  str(r[0]) + " - Professor " + str(r[2]) +
                  "\n\t Section ID - " + str(r[4]) + " - " + str(5-int(r[5])) + " out of 5 seats available.")
            cnt += 1

            # Appends
            c_name.append(r[0])
            c_id.append(r[1])
            i_name.append(r[2])
            i_id.append(r[3])
            s_id.append(r[4])
            all.append(r)

        choice = input(
            "Select the section you wish to register for by inputting the number next to the name of the course you wish to register for!\nENTRY: ")
        print("\nYou've selected: " +
              str(all[int(choice)-1][0]) + " - Section " + str(all[int(choice)-1][4]))
        register(all[int(choice)-1][4], all[int(choice)-1][1], UCID)
        print("\nYou're all set! Register for more courses by restarting the program, inputting your new UCID, and selecting another course!\nRemember! You can only register for a max of 3 courses.")
        exit()

        return all


def register(section_id, course_id, UCID):
    # CHECK IF THEY'RE ALREADY IN THE CLASS
    cursor.execute(
        "select student_id from registration where student_id = " + str(UCID) + " and course_id = " + str(course_id) + "", multi=True)
    if cursor.fetchall() != []:
        print("You're already registered for this course!")
        exit()
    # CHECK IF THEY'RE AT THE COURSE LIMIT
    cursor.execute(
        "select COUNT(course_id) from registration where student_id = " + str(UCID), multi=True)
    if cursor.fetchall()[0][0] == 3:
        print("You're at the course limit!")
        exit()
    # CHECK IF CLASS IS FULL
    cursor.execute(
        "select COUNT(student_id) from registration where section_id = " + str(section_id), multi=True)
    if cursor.fetchall()[0][0] >= 5:
        print("The course you've selected is full, try another one!")
        exit()
    else:
        cursor.execute("INSERT INTO Registration(section_id, course_id, student_id, registration_date) VALUES(" +
                       str(section_id) + ", " + str(course_id) + ", " + str(UCID) + ", '" + str(date.today()) + "');", multi=True)
        sql.commit()
        print("Successfully registered student " + str(UCID) +
              " for course number " + str(course_id) + " - section number " + str(section_id))


all = []
c_name = []
c_id = []
i_name = []
i_id = []
s_id = []

######################################################################################################

# SCRAP WORK

UCID = 11
#print("TEST: ", (register(53, 656, 49)))

# Query Database
# insert_stmt = (
#    "INSERT INTO instructor (instructor_id, name, office, phone) "
#    "VALUES (%s, %s, %s, %s)")
#data = (1, 'Vincent Oria', 'Computer Science', 7329969632)
#cursor.execute(insert_stmt, data)

t = 'Avneet Singh'
select_stmt = "SELECT student_id FROM student where name = '" + t + "';"
lis = []

# for q in cursor.execute(select_stmt, multi=True):
#    if q.with_rows:
#        print("Rows produced by statement '{}':".format(
#            q.statement))
#        lis = q.fetchall()
#    else:
#        print("Number of rows affected by statement '{}': {}".format(
#            q.statement, q.rowcount))

# cursor.execute(select_stmt, multi=True)
# print(cursor.fetchall()[0][0])

# for q in cursor.execute(select_stmt, multi=True):
#    result = q.fetchall()
#    for r in result:
#        print(r)

############################################################################################################

# Start
UCID = input("\nHello, welcome to NJIT's student registration tool!\n"
             "\nPlease enter your UCID if you are a returning student.\nIf you are a new student, press 0.\n\n ENTRY: ")

# Status for new or returning student
status = ''

# Check if returning student and provide basic info
try:
    if int(UCID) != 0:
        select_stmt = "SELECT name, address FROM student WHERE student_id = " + \
            str(UCID)
        for q in cursor.execute(select_stmt, multi=True):
            result = list(q.fetchone())
            s_name = result[0]
            s_address = result[1]
            status = 'Returning'

except:
    print("\nError! That is not a valid UCID. ")

else:
    if int(UCID) != 0:
        select_stmt = "SELECT name, address FROM student WHERE student_id = " + \
            str(UCID)
        for q in cursor.execute(select_stmt, multi=True):
            result = list(q.fetchone())
            s_name = result[0]
            s_address = result[1]
            status = 'Returning'

    else:
        # Get basic info if new student
        print("\nWelcome to NJIT! Please provide some basic information for so we can update our database!\n")
        s_name = input("FULL NAME: ")
        s_address = input("ADDRESS: ")
        status = 'New'

# If Returning student, print basic info from student and class info
if status == 'Returning':
    print("\nWelcome back, " + str(s_name) + "! " +
          "Your current address is " + str(s_address))

    # Get courses associated with this UCID
    res = get_courses(UCID)
    #print("RESULTS: ", res)

    # If num_courses = 0
    if (res == None) | (len(res) == 0):
        print("\nLooks like you aren't registered for any classes yet! You can register for a maximum of 3 courses per semester.")
        # RETURNING STUDENT COURSE REGISTRATION (0)
        print("\nNow let's get you registered! Here are the available courses, along with the professors, sections, and number of spots left\n")
        registration(UCID)
        choice = input(
            "Select the section you wish to register for by inputting the number next to the name of the course you wish to register for!\nENTRY: ")
        print("\nYou've selected: " +
              str(all[int(choice)-1][0]) + " - Section " + str(all[int(choice)-1][4]))
        register(all[int(choice)-1][4], all[int(choice)-1][1], UCID)
        print("\nYou're all set! Register for more courses by restarting the program, inputting your new UCID, and selecting another course!\nRemember! You can only register for a max of 3 courses.")
        exit()
        # REGISTRATION FUNCTION

    # If num_courses = 1
    elif len(res) == 1:
        print("\nYou are currently registered for 1 course. ")
        print("\nCourse: \n")
        print(res[0])
        # RETURNING STUDENT COURSE REGISTRATION (1)
        print("\nNow let's get you registered for more! Here are the available courses, along with the professors, sections, and number of spots left\n")
        registration(UCID)
        choice = input(
            "Select the section you wish to register for by inputting the number next to the name of the course you wish to register for!\nENTRY: ")
        print("\nYou've selected: " +
              str(all[int(choice)-1][0]) + " - Section " + str(all[int(choice)-1][4]))
        register(all[int(choice)-1][4], all[int(choice)-1][1], UCID)
        print("\nYou're all set! Register for more courses by restarting the program, inputting your new UCID, and selecting another course!\nRemember! You can only register for a max of 3 courses.")

    # If num_courses = 2+
    else:
        print("\nYou are currently registered for " +
              str(len(res)) + " courses. ")
        print("\nCourses: \n")
        # Gets names of courses student is taking
        for r in res:
            print(r)

        # CHECK IF REGISTERED FOR 3 COURSES
        if len(res) == 3:
            print("\nLooks like you're registered for 3 courses, which is the maximum allowed at NJIT. Have a great day!")
            exit()
        # RETURNING STUDENT COURSE REGISTRATION (0)
        print("\nNow let's get you registered! Here are the available courses, along with the professors, sections, and number of spots left\n")
        registration(UCID)
        choice = input(
            "Select the section you wish to register for by inputting the number next to the name of the course you wish to register for!\nENTRY: ")

        print("\nYou've selected: " +
              str(all[int(choice)-1][0]) + " - Section " + str(all[int(choice)-1][4]))
        register(all[int(choice)-1][4], all[int(choice)-1][1], UCID)
        print("\nYou're all set! Register for more courses by restarting the program, inputting your new UCID, and selecting another course!\nRemember! You can only register for a max of 3 courses.")

    # Show count of classes they have, along with limit.

if status == 'New':
    print("\nHi, " + str(s_name) + "! " +
          "Your current address is " + str(s_address) + ".")

    # ADD STUDENT TO STUDENT TABLE IN DB
    push = "INSERT INTO Student(name, address) VALUES('" + \
        str(s_name) + "', '" + str(s_address) + "');"
    cursor.execute(push, multi=True)
    sql.commit()

    # Get new UCID
    cursor.execute(
        "SELECT student_id FROM student where name = '" + s_name + "';", multi=True)
    UCID = cursor.fetchall()[0][0]

    print("\nThis information has been passed to our database! \n\n Your new UCID is:", str(UCID))

    # NEW STUDENT FIRST CLASS REGISTRATION
    print("\nNow let's get you registered! Here are the available courses, along with the professors, sections, and number of spots left\n")
    registration(UCID)
    choice = input(
        "Select the section you wish to register for by inputting the number next to the name of the course you wish to register for!\nENTRY: ")
    print("\nYou've selected: " +
          str(all[int(choice)-1][0]) + " - Section " + str(all[int(choice)-1][4]))
    register(all[int(choice)-1][4], all[int(choice)-1][1], UCID)
    print("\nYou're all set! Register for more courses by restarting the program, inputting your new UCID, and selecting another course!")

# Close Database
sql.close()
