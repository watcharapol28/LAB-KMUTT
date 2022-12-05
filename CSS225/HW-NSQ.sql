use university;

select * from advisor;
select * from classroom;
select * from course;
select * from department;
select * from instructor;
select * from prereq;
select * from section;
select * from student;
select * from takes;
select * from teaches;
select * from time_slot;

-- 1
select title from course where credits = 3;

-- 2
select distinct ID from takes 
where course_id in (select course_id from instructor, teaches 
where instructor.ID = teaches.ID and name = 'Einstein');

-- 3 
select max(salary) from instructor ;

-- 4
select name from instructor 
where salary in (select max(salary) from instructor);

-- 5
select * from takes 
where year = 2017 and semester = 'Autumn'; 

-- 6 
select count(*) from takes 
where year = 2017 and semester = 'Autumn'; 

-- 7 
select sec_id, count(*) from takes
where year = 2017 and semester = 'Autumn' group by sec_id ;

-- 8 
insert into course(course_id, title, dept_name, credits)
values ('CS-001', 'Weekly Seminar', null , 0);

-- 9 
insert into section(course_id, sec_id, semester, year)
values ('CS-001', 1, 'Autumn', 2017);

-- 10
insert into takes select ID, "CS-001", 1, 'Autumn', 2017, null from student 
where dept_name = 'Comp. Sci.';

-- 11 
delete from takes where ID in (select ID from student where name = 'Chavez');

-- 12
delete from course where course_id = 'CS-001';

-- 13
delete from takes where course_id in 
(select course_id from course where title like '%database%');
