# Write your MySQL query statement below

WITH highest_salary AS(
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
    DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS sal_rank
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM highest_salary
WHERE sal_rank = 1