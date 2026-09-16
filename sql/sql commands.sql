/* the
multiline
comment
*/

USE intro_sql;

select id,city,country from customers;

select * from customers;

select company_name as Company_Name from customers; 

select distinct country from customers;

select id,phone,Company_Name from customers where country="USA";

select * from orders;

select id,customer_id,shipper,freight from orders where freight>100;

select * from products;
-- comments
select id,product_name,category,unit_price from products where category="Condiments" and discontinued=0;