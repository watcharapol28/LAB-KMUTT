SELECT CONCAT('CSS225 ', 'IS ', 'EASY') AS ConcatenationResult;
SELECT SUBSTR('CSS225 is easy', -4) AS Result;
SELECT TRIM(' CSS225 is easy ') AS Result;
SELECT LTRIM(' CSS225 is easy ') AS Result;
SELECT length(' CSS225 is easy ') AS Result;

use sakila;
select lpad('css225 is easy', 25,'.') as result;
select ascii('css225 is easy') as result;
SELECT DISTINCT(DATE_FORMAT(RENTAL_DATE, '%D %b %Y')) FROM
RENTAL;

-- 1 
select * from film;
select replace(rental_duration, rental_duration, 7) as retal_duration from film;

-- 2
select upper(substr(title, 1, 3)) from film;

-- 3 
select (date_format(curdate(), '%Y') - date_format('2003-04-04', '%Y')); 

-- 4
select (date_format(curdate(), '%j'));

-- 5 
select (date_format(curdate(), '%d-%m-%Y'));
select (date_format(curdate(), '%D %M %X'));
select (date_format(current_timestamp(), '%r  ' '%d-%c-%Y'));
select (date_format(curdate(), '%u weeks'));
select (date_format(current_timestamp(), '%h:%i %p  %Y-%m-%d'));

