-- Write your query below
-- select customer.name 
-- from customers 
-- join orders 
-- on customers.id=orders.customer_id
-- where id 
select name from customers where id not in (select customer_id from orders);