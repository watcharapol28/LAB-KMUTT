create schema project;
use project;

create table user_(
	user_email varchar(40) primary key,
    user_name varchar(20),
    user_password varchar(20),
    update_at timestamp,
    create_at timestamp,
    delete_at timestamp
);

create table user_schedule(
	user_schedule_id varchar(20) primary key,
    user_schedule_header varchar(20),
    user_schedule_date timestamp,
    user_schedule_time_range timestamp,
    create_at timestamp,
    update_at timestamp,
    delete_at timestamp
);

create table color_theme(
	color_theme_id varchar(20) primary key,
    color_hex_code varchar(20),
    color_name varchar(20),
    create_at timestamp,
    update_at timestamp,
    delete_at timestamp
);

create table schedule_(
	schedule_id varchar(20) primary key,
    schedule_header varchar(20),
	schedule_details varchar(20),
    schedule_date date,
    schedule_time_range timestamp,
    create_at timestamp,
    update_at timestamp,
    delete_at timestamp,
    create_by varchar(20),
    update_by varchar(20)
);