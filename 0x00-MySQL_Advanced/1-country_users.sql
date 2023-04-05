-- creates a table users 
Create table if not exists users (
    id int not null auto_increment,
    email varchar(255) not null,
    name varchar(255) not null,
    country enum('US', 'CO', 'TN') not null default 'US',
    primary key (id),
    unique key (email)
);
