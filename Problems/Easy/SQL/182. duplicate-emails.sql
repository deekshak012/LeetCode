# Write your MySQL query statement below
Select Email
from person
group by email
having Count(person.id) >1 