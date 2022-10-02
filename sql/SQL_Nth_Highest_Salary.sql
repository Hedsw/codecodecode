CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
        Select Distinct Salary 
        From Employee 
        Order by Salary Desc 
        Limit 1 Offset N # OFFSET은 N개의 것은 SKIP하라는 뜻 
  );
END

# Select * FROM artists LIMIT 11 OFFSET 9
# You want to skip the first 9 and then only return 11 (10 through 20) results