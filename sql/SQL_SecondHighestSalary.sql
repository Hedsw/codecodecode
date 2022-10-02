# Write your MySQL query statement below
SELECT 
    IFNULL (
        (SELECT Distinct Salary 
        From Employee
        ORDER BY Salary Desc # Desc - Descending Order의 뜻 
        LIMIT 1 OFFSET 1), 
        NULL
    ) as SecondHighestSalary