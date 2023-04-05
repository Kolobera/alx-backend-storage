-- Create unique index on users table
Create table if not exists users (
    id int not null auto_increment,
    name varchar(255) not null,
    email varchar(255) not null,
    primary key (id),
    unique key (email)
);
