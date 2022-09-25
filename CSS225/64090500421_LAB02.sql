use sakila;

select distinct rental_duration from film;  # 1

select max(length), min(length), avg(length) from film where length between 60 and 100;   # 2

select city from city where city like 'g%' or '%z%';  # 3

select customer_id, sum(amount) from payment group by customer_id;  # 4

select * from film order by replacement_cost;  # 5