# Write your MySQL query statement below
# select c.name as Customers
# from Customers c left join orders o
# on c.id = o.customerId
# where o.id is null

select c.name as Customers
from customers c
where c.id not in 
(
    select customerid from orders
);
