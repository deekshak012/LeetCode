# Write your MySQL query statement below
select p.FirstName, p.LastName,a.City,a.State 
from  Person p LEFT JOIN Address a 
on p.PersonId=a.PersonId 