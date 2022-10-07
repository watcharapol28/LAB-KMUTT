create schema project;
use project;


create table Users(
	user_id varchar(255) primary key,
    user_email varchar(255) ,
    user_password varchar(255) ,
    create_at varchar(255) ,
    update_at varchar(255) ,
    user_role varchar(20)
);

create table ColorTheme(
	hex_code varchar(255) primary key ,
    color_meaning varchar(255) ,
    create_at varchar(255) ,
    update_at varchar(255)
);

create table event(
	event_id varchar(255) primary key ,
    event_header varchar(255) ,
    event_desc varchar(255) ,
    event_date timestamp ,
    time_range varchar(255) ,
    create_at varchar(255) ,
    update_at varchar(255) ,
    user_id varchar(255) ,
    hex_code varchar(255) ,
    foreign key(user_id) references Users(user_id) ,
    foreign key(hex_code) references ColorTheme(hex_code)
);