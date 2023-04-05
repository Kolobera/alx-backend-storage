-- creates a table users
Create table if not exists users (
    id int not null auto_increment,
    email varchar(255) not null,
    name varchar(255),
    primary key (id),
    unique key (email)
);
