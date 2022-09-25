create schema lab01;
#drop database lab01;
use lab01;

create table themepark(
	Park_Code varchar(10) not null primary key,
    Park_Name varchar(35) not null,
    Park_City varchar(50) not null,
    Park_Country varchar(2) not null
);
#insert into themepark(Park_Name, Park_City, Park_Country)
#values('Saunthon', 'Bangmod', 'Thailand');
#desc themepark;
#select * from themepark;

create table ticket(
	Ticket_NO numeric(10) not null primary key,
    Ticket_Price numeric(4, 2),
    Ticket_Type varchar(10) not null,
    Park_Code varchar(10) not null,
    foreign key(Park_Code) references themepark(Park_Code)
);
#insert into ticket(Ticket_Price, Ticket_Type, Park_Code)
#values(99.99, 'First Class', 1);
#desc ticket;
#select * from ticket;

create table sales(
	Transaction_NO numeric not null primary key,
    Park_Code varchar(10) not null,
    Sale_DATE date not null,
    foreign key(Park_Code) references themepark(Park_Code)
);
#desc sales;
#insert into sales(Park_code, Sale_Date)
#values(1, now());
#select * from sales;

create table sales_line(
	Transaction_NO numeric not null,
    Line_NO numeric(2) not null,
    Ticket_NO numeric(10) not null,
    Line_QTY numeric(4) not null,
    Line_Price numeric(9, 2) not null,
	foreign key(Transaction_NO)references sales(Transaction_NO),
    foreign key(Ticket_NO)references ticket(Ticket_NO),
    primary key(Transaction_NO, Line_NO)
);
#insert into sales_line(Transaction_NO, Line_NO, Ticket_NO, Line_QTY, Line_Price)
#values(1, 1, 1, 3, 39.50);
#desc sales_line;

#select * from sales_line;
create table attraction(
	Attract_NO numeric(10) not null primary key,
    Park_Code varchar(10) not null,
    Attract_Name varchar(35) not null,
    Attract_Age numeric(3) not null default(0),
    Attract_Capacity numeric(3) not null,
    foreign key(Park_Code) references themepark(Park_Code)
);

create table employee(
	EMP_NUM numeric(4) not null primary key,
    EMP_Title varchar(4),
    EMP_LName varchar(15) not null,
    EMP_FName varchar(15) not null,
    EMP_DOB date not null,
    EMP_Hire_Date date not null,
    EMP_Areacode varchar(4) not null,
    EMP_Phone varchar(12) not null,
    Park_Code varchar(10) not null,
    foreign key(Park_Code) references themepark(Park_Code)
);

create table hours(
	EMP_NUM  numeric(4) not null,
    Attract_NO numeric(10) not null,
    Hours_per_Attract numeric(2) not null,
    Hour_Rate numeric(4, 2) not null,
    Date_Worked date,
    foreign key(EMP_NUM) references employee(EMP_NUM),
    foreign key(Attract_NO) references attraction(Attract_NO),
    primary key(EMP_NUM, Attract_NO)
);