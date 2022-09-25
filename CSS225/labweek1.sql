create schema shop;
drop database shop;
use shop;

create table customer(
	customerID int not null auto_increment primary key,
    custFirstName varchar(25),
    custMidName varchar(10),
    custLastName varchar(25)
    );
desc Customer;

insert into customer(custFirstName, custLastName)
values('John', 'Doe');

insert into customer(custFirstName, custMidName, custLastName)
values('Hiw', 'Khaw', 'Khab');

select * from customer;

create table SalesOrder(
	OrderID int not null auto_increment primary key,
    OderDate date,
    CustomerID int,
    foreign key(CustomerID)references customer(customerID)
    );
desc SalesOrder;
insert into SalesOrder(OrderDate, CustomerID)
values(date, 1);
select * from SalesOrder;

insert into OrderLine(OrderLineID, OrderID, ProductID, QuantityOrdered)
values(1, 1, 1, '3kg');

create table Product(
	ProductID int not null auto_increment primary key,
    ProductName varchar(25),
    UnitPrice decimal,
    NumberInStock int
);
insert into Product(ProductID, ProductName, UnitPrice, NumberInStock)
values(1, 'Strawberry', 4.99, 16);

Alter table Product modify UnitPrice decimal(5, 2);
Update Product Set UnitPrice = 4.99 where ProductID = 1;

select * from Product;

create table OrderLine(
	OrderLineID int not null auto_increment primary key,
    ProductID int,
    foreign key(ProductID)references Product(ProductID),
    QuantityOrdered varchar(15),
    OrderID int,
    foreign key(OrderID)references SalesOrder(OrderID)
);
desc OrderLine;

show databases;
show tables;


