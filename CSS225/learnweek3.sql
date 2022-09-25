use sakila;
desc film;

select * from category;
SELECT * FROM actor;
SELECT first_name, last_name FROM actor;
SELECT payment_id, customer_id, amount+1 FROM payment;
SELECT payment_id, customer_id, round(amount) FROM payment; 

SELECT payment_id, customer_id, round(amount) rounding FROM
payment;
SELECT payment_id, customer_id, round(amount) AS 'rounding amount'
FROM payment; 

SELECT payment_id, customer_id, amount FROM payment WHERE
amount > 10.99;

select sum(amount) 'sum of amount' FROM payment where amount > 10.99;

select film_id, title, release_year from film where title < 'B';

select payment_id from payment where not payment_id = 1; 

SELECT * FROM film WHERE rating IN ('R', 'NC-17'); 


SELECT * FROM address WHERE not address2 IS NULL;

select title, length from film where length < 60 or length > 100;

SELECT * FROM film ORDER BY rating, title DESC;
