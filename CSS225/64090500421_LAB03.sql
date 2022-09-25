use university;
SELECT * FROM student;

SELECT * FROM student natural left join takes;

SELECT * FROM student natural right join takes;

select ID, name, sec_id from instructor natural join teaches;

select course_id, sec_id, name from instructor natural join teaches where semester = 'Spring' and year = '2010' ;

select dept_name, count(dept_name) number_of_instructor from instructor group by dept_name having number_of_instructor >= 0;