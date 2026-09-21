/* the
multiline
comment
*/
-- accessing the db
USE intro_sql;

-- selecting particular columns from the table

select id,city,country from customers;
-- selecting all the culmns from the table
select * from customers;

-- changing the existing column name
select company_name as Company_Name from customers; 

-- removing the duplicate row from the table
select distinct country from customers;

-- selecting required columns where the given value is true
select id,phone,Company_Name from customers where country="USA";

select * from orders;

-- selecting the required columns where the given conditiona is true
select id,customer_id,shipper,freight from orders where freight>100;

select * from products;
-- comments
select id,product_name,category,unit_price from products where category="Condiments" and discontinued=0;

-- selecting the required columns where the values are btwn the given conditions
select * from orders;
select id,customer_id,shipper,freight,order_date from orders where order_date between '2020-01-01' and '2020-12-31';

select * from customers;

select id,phone from customers where country="USA" or country="Germany";

-- selecting the columns using order by keyword
select * from customers;

select id,employee_id,company_name,country from customers order by country asc;
select id,employee_id,company_name,country from customers order by country desc,id asc,company_name desc;

-- sql group by clauses
select country from customers;
select country from customers group by country;
select count(id) as "count", country from customers group by country;

select * from products;

select category,sum(unit_price) as "total unit_price" from products group by category;

select country from customers group by country;

select category,min(units_in_stock) as "total stock" from products group by category;

select category,max(units_in_stock) as "total stock" from products group by category;


-- creating database
create database db;

-- deleting database
drop database db;

create database db;
use db;

-- creating table
create table new_table(id int not null auto_increment,first_name varchar(255),last_name varchar(255),department varchar(255),primary key(id));