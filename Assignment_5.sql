create database Assignment6; 
USE Assignment6;

/* Instructor Table */

Create table Instructor(
	instructor_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(20) NOT NULL,
    email VARCHAR(20),
    phone VARCHAR(20)
);

ALTER TABLE Instructor CHANGE office email VARCHAR(20);
insert into Instructor(instructor_id, name, email, phone) values(1, 'Vincent Oria', 'vincent@njit.edu','6092447555' );
insert into Instructor(instructor_id, name, email, phone) values(2, 'Jame Author', 'james@njit.edu','6092447553' );
insert into Instructor(instructor_id, name, email, phone) values(3, 'Mark Newton', 'Newton@njit.edu','6092447453' );
insert into Instructor(instructor_id, name, email, phone) values(4, 'Jack Shawn', 'shawn@njit.edu','6096947553' );
insert into Instructor(instructor_id, name, email, phone) values(5, 'Matt John', 'matt@njit.edu','604267553' );
insert into Instructor(instructor_id, name, email, phone) values(6, 'Sharon Austin', 'sharon@njit.edu','6092447444' );
insert into Instructor(instructor_id, name, email, phone) values(7, 'Ezra Boston', 'boston@njit.edu','6092447222' );
insert into Instructor(instructor_id, name, email, phone) values(8, 'Luke Johnson', 'luke@njit.edu','6092447134' );
insert into Instructor(instructor_id, name, email, phone) values(10, 'Denmark James', 'dens@njit.edu','6092447111' );

select * from Instructor;



#drop table Instructor;

/* Course Table */

Create table Course(
	course_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(40) NOT NULL,
    description VARCHAR(250)
);

insert into Course(course_id, name, description) values(631, 'Database Management', 'Computer Science');
insert into Course(course_id, name, description) values(656, 'Data Analytics with R', 'Computer Science');
insert into Course(course_id, name, description) values(601, 'Web Development System', 'Computer Science');
insert into Course(course_id, name, description) values(640, 'IT', 'Computer Science');
insert into Course(course_id, name, description) values(621, 'Artificial Intelligence', 'Computer Science');
insert into Course(course_id, name, description) values(600, 'Business Intelligence', 'Computer Science');
insert into Course(course_id, name, description) values(635, 'Data Analytics for info', 'Computer Science');
insert into Course(course_id, name, description) values(611, 'Applied Statistics', 'Mathematics');
insert into Course(course_id, name, description) values(664, 'Big Data', 'Computer Science');
insert into Course(course_id, name, description) values(658, 'Data Structure', 'Computer Science');
select * from Course;

#drop table Course;

/* Student Table */

Create table Student(
	student_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(20) NOT NULL,
    address VARCHAR(20)
);

insert into Student(student_id, name, address) values(11, 'Mike Tyson', 'Trenton, NJ');
insert into Student(student_id, name, address) values(12, 'Matt Bason', 'Princeton, NJ');
insert into Student(student_id, name, address) values(13, 'Duke Badwin', 'Langhorne, PA');
insert into Student(student_id, name, address) values(14, 'Michelle Cook', 'Ewing, NJ');
insert into Student(student_id, name, address) values(15, 'Elizabeth Taylor', 'Elizabeth, NY');
insert into Student(student_id, name, address) values(16, 'Morenike Johnson', 'Monmonth, NJ');
insert into Student(student_id, name, address) values(17, 'Ademi Tope', 'Ewing, NJ');
insert into Student(student_id, name, address) values(18, 'Luke Tyson', 'Trenton, NJ');
insert into Student(student_id, name, address) values(19, 'Nike Apples', 'Trenton, NJ');
insert into Student(student_id, name, address) values(20, 'James Brown', 'Ewing, NJ');
insert into Student(student_id, name, address) values(21, 'Lin Lin', 'Trenton, NJ');
insert into Student(student_id, name, address) values(22, 'Aretha James', 'Trenton, NJ');
insert into Student(student_id, name, address) values(23, 'Peter Braxson', 'Trenton, NJ');
insert into Student(student_id, name, address) values(24, 'Liz Stone', 'South Brunswick, NJ');
insert into Student(student_id, name, address) values(25, 'Peter Cat', 'South Brunswick, NJ');
insert into Student(student_id, name, address) values(26, 'Charles Taylor', 'Lancore, PA');
insert into Student(student_id, name, address) values(27, 'Elisha Prophet', 'Trenton, NJ');
insert into Student(student_id, name, address) values(28, 'Deacon John', 'Princeton, NJ');
insert into Student(student_id, name, address) values(29, 'Timothy happy', 'Princeton, NJ');
select * from Student;

select student_id from student where name = 'Thomas Cruise';

drop table Student;

/* Section Table */

Create table Section(
	section_id INT PRIMARY KEY AUTO_INCREMENT, 
    course_id INT,
    instructor_id INT,
    syllabus VARCHAR(250) NOT NULL,
    room VARCHAR(20), 
    day VARCHAR(20),
    hour VARCHAR(20),
    address VARCHAR(20),
    foreign key(course_id) references Course(course_id) on delete set null,
    foreign key(instructor_id) references Instructor(instructor_id) on delete set null
);

insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(50, 'CS600', 'B10', 'Monday','12:00','NJ',600,1);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(51, 'CS601', 'B5', 'Tuesday','16:00','NJ',601,2);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(52, 'CS631', 'B10', 'Friday','12:00','NJ',631,4);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(53, 'CS656', 'B12', 'Wednesday','18:00','NJ',656,5);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(54, 'CS621', 'B1', 'Monday','12:00','NJ',621,6);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(55, 'CS640', 'B10', 'Monday','12:00','NJ',640,3);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(56, 'CS611', 'B7', 'Saturday','12:00','NJ',611,7);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(57, 'CS664', 'B10', 'Monday','12:00','NJ',664,8);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(58, 'CS658', 'B5', 'Monday','12:00','NJ',658,1);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(59, 'CS635', 'B10', 'Monday','12:00','NJ',635,1);
insert into Section(section_id, syllabus, room, day, hour, address, course_id, instructor_id) values(60, 'CS600', 'B10', 'Monday','12:00','NJ',600,1);
select * from Section;

SELECT COUNT(R.student_id) as Count, C.name, C.course_id, I.name, I.instructor_id, S.section_id
FROM Course C, Section S, Instructor I, Registration R
WHERE C.course_id = S.course_id 
AND S.instructor_id = I.instructor_id
AND R.section_id = S.section_id
GROUP BY S.section_id;

select * from registration;
SELECT COUNT(student_id) as Count, section_id from registration group by section_id;

#drop table Section;

/* Registration Table */

Create table Registration(
	registration_id INT PRIMARY KEY AUTO_INCREMENT,
	section_id INT, 
    course_id INT,
    student_id INT,
    foreign key(section_id) references Section(section_id) on delete set null,
    foreign key(course_id) references Course(course_id) on delete set null,
    foreign key(student_id) references Student(student_id) on delete set null,
    registration_date DATE
);

insert into Registration(section_id, course_id, student_id, registration_date) values(50,600,11, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(51,601,12, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(52,631,14, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(53,656,25, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(54,621,16, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(55,640,23, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(56,611,17, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(57,664,28, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(58,658,11, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(59,631,21, '2022-05-01');
insert into Registration(section_id, course_id, student_id, registration_date) values(60,621,12, '2022-05-01');

select student_id from registration where student_id = 48 and section_id = 58;

select student_id, section_id from Registration where section_id = 53;

select * from registration;

insert into Registration(section_id, course_id, student_id, registration_date) values(60, 600, 32, '2022-08-10');

SELECT name from course where course_id in (select course_id from registration where student_id = 32);

drop table Registration;
