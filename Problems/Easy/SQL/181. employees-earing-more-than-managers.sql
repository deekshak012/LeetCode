# Write your MySQL query statement below
select e.name as Employee 
from Employee e inner join Employee m 
on e.managerid = m.id
where e.Salary>m.Salary