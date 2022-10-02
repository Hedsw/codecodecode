SELECT Name AS Country, Continent AS B, Region AS "ANSWER"FROM COUNTRY;
# Column 선택할 떄
SELECT Name, Continent, Region FROM Country WHERE Continent = 'Europe' ORDER BY Name LIMIT 5 OFFSET 10;
# Row 선택할 때 

SELECT COUNT(*) FROM Country WHERE Population > 1000000;
Population > 1000000 이상인 것이 몇개인지 카운트 a

SELECT COUNT(LifeExpectancy) FROM Country; 
LifeExpectancy를 가지고 있는게 몇개 인지 카운트


SELECT COUNT(*) FROM Country WHERE Population > 1000000;
Population > 1000000 이상인 것이 몇개인지 카운트 a

SELECT COUNT(LifeExpectancy) FROM Country; 
#LifeExpectancy를 가지고 있는게 몇개 인지 카운트



SELECT * FROM customer;

INSERT INTO customer(name, address, city, state, zip)
    Values('Fred Flinstone', '123 Cobblestone way', 'Bedrock', 'CA', '91234');

INSERT INTO customer(name, city, state)
    Values('Jimi Hendrix', 'Renton', 'WA');
    
SELECT * FROM customer;

UPDATE customer SET address = '123 Music Avenue', zip = '02747' WHERE id = 5;
UPDATE customer SET address = '2603 S Washington St', zip = '98056' WHERE id = 6;
UPDATE customer SET address = NULL, zip = NULL WHERE id = 4;


SELECT * FROM customer WHERE id = 4;

DELETE FROM customer WHERE id = 4;
SELECT * FROM customer;

DELETE FROM customer WHERE id = 5;
SELECT * FROM customer;

the proper syntax for aliasing a field? 
SELECT FirstName AS "First Name";

an example of a query to get only data containing the word "Apple"? 
SELECT * FROM Fruits WHERE Name = 'Apple';


테이블 생성
CREATE TABLE test (
    a INTEGER,
    b TEXT
);

INSERT INTO test VALUES ( 1, 'a');
INSERT INTO test VALUES ( 2, 'b');
INSERT INTO test VALUES ( 3, 'c');
SELECT * FROM test;


CREATE TABLE test ( a , b  );
INSERT INTO test VALUES ('one', 'two');
SELECT * FROM test;
DROP TABLE test;
DROP TABLE IF EXISTS test;


DROP TABLE test;
CREATE TABLE test (a INTEGER, b TEXT, c TEXT);

INSERT INTO test VALUES ( 1, 'this', 'Right here!' );
INSERT INTO test (b, c) VALUES (' That', 'Over there!' );
INSERT INTO test DEFAULT VALUES;
INSERT INTO test ( a, b, c) SELECT id, name, description from item;

SELECT * FROM test;
SELECT * FROM test WHERE a = 1;
DELETE FROM test WHERE a = 1;

NULL은 VAlue가 아니라서, NULL인거 확인하려면 IS NULL로 해야함.. 위에 = 로 확인한 것은 Value라서 그런 것
SELECT * FROM test WHERE a IS NULL;


CREATE TABLE test (
 a INTEGER NOT NULL, 
 b TEXT NOT NULL,
 c TEXT 
);


INSERT INTO test VALUES (1, 'this', 'that');
INSERT INTO test (a,b) VALUES (1, 'two');

SELECT * FROM test;

DROP TABLE IF EXISTS test;



UNIQUE는 이 테이블 안에 똑같은 값이 하나만 있어야 할 때 설정, NOT NULL은 값이 NULL값이 들어가거나 EMPTY가 되지 않도록 할 때 설정
DEFAULT는 아무것도 안들어온다면, 항상 디폴트 값을 주고 싶을 때 설정 
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT UNIQUE, b TEXT NOT NULL, c TEXT DEFAULT 'panda');
INSERT INTO test (a, b) VALUES ('one', 'two');
INSERT INTO test (a, b) VALUES ('one', 'two');
SELECT * FROM test;


ALTER는 뒤에 Column을 추가할 때 사용함
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT, b TEXT, c TEXT);
INSERT INTO test VALUES ('one', 'two', 'three');
INSERT INTO test VALUES ('two', 'thre', 'four');
INSERT INTO test VALUES ('three', 'four', 'five');
SELECT * FROM test;

ALTER TABLE test ADD e TEXT DEFAULT 'panda';



PRIMARY KEY를 쓰면, ID 넘버가 자동으로 생성 됨. 

DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    a INTEGER,
    b TEXT
);

INSERT INTO test (a, b) VALUES ( 10, 'a');
INSERT INTO test (a, b) VALUES ( 11, 'b');
INSERT INTO test (a, b) VALUES ( 12, 'c');
SELECT * FROM test;



SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 OR Population IS NULL ORDER BY Population DESC;
    
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;

// 앞 뒤로 island라는 말이 붙어 있는거 다 고르기
SELECT Name, Continent, Population FROM Country
    WHERE Name Like '%island%' ORDER BY Name;
    
// ~~ Island로 끝나는 거 고르기
SELECT Name, Continent, Population FROM Country
    WHERE Name Like '%island' ORDER BY Name;
    
// Island ~~ 로 끝나는 거 고르기 
SELECT Name, Continent, Population FROM Country
    WHERE Name Like 'island%' ORDER BY Name;



// 인구수가 100000 미만이고, 오세아니아 대륙인 것들을 Popluation을 기준으로 디센딩하게 뽑기
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 AND Continent = 'Oceania' ORDER BY Population DESC;

// Continent 콜럼안에서 유럽과 아시아인 것만 뽑아내기
SELECT Name, Continent, Population FROM Country
    WHERE Continent IN ('Europe', 'Asia') ORDER BY Name;



SELECT Continent FROM Country;

// SELECT DISTINCT는 중복된 거 없애는 것.. 이 예시에서는 Continent에서 중복된 것들 없애는 것 
SELECT DISTINCT Continent FROM Country;



//a, b 콜럼 합해서 Test테이블 안에서 중복된거 없이 구하기
SELECT DISTINCT a,b FROM test;
// b 콜럼만 따져서 중복된거 없이 하기 
SELECT DISTINCT a FROM test;


DROP TABLE test;

CREATE TABLE test (a INTEGER, b TEXT, c TEXT);

INSERT INTO test VALUES ( 1, 'this', 'Right here!' );

INSERT INTO test (b, c) VALUES (' That', 'Over there!' );

INSERT INTO test DEFAULT VALUES;

INSERT INTO test ( a, b, c) SELECT id, name, description from item;

SELECT * FROM test;
SELECT * FROM test WHERE a = 1;
DELETE FROM test WHERE a = 1;

INSERT INTO test(a, b, c) VALUES (0, NULL, '');
SELECT * FROM test WHERE b IS NULL;
SELECT * FROM test WHERE c = '';

DROP TABLE IF EXISTS test;

CREATE TABLE test (
 a INTEGER NOT NULL, 
 b TEXT NOT NULL,
 c TEXT 
);


INSERT INTO test VALUES (1, 'this', 'that');
INSERT INTO test (a,b) VALUES (1, 'two');

SELECT * FROM test;
DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT UNIQUE NOT NULL, b TEXT NOT NULL, c TEXT DEFAULT 'panda');
INSERT INTO test (a, b) VALUES (NULL, 'two');
INSERT INTO test (a, b) VALUES (NULL, 'two');
SELECT * FROM test;

DROP TABLE IF EXISTS test;
CREATE TABLE test (a TEXT, b TEXT, c TEXT);
INSERT INTO test VALUES ('one', 'two', 'three');
INSERT INTO test VALUES ('two', 'thre', 'four');
INSERT INTO test VALUES ('three', 'four', 'five');
UPDATE test SET a = 'change?', b = 'well..', c = 'hacked' WHERE a = 'one';
SELECT * FROM test;

ALTER TABLE test ADD e TEXT DEFAULT 'panda';

DROP TABLE IF EXISTS test;
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    a INTEGER,
    b TEXT
);

INSERT INTO test (a, b) VALUES ( 10, 'a');
INSERT INTO test (a, b) VALUES ( 11, 'b');
INSERT INTO test (a, b) VALUES ( 12, 'c');
SELECT * FROM test;


// SELECT 모음집
SELECT Name, Continent, Population FROM Country
    WHERE Population < 100000 OR Population IS NULL ORDER BY Population DESC;

SELECT Continent FROM Country;

DROP TABLE IF EXISTS test;
CREATE TABLE test (a int, b int);
INSERT INTO test VALUES (1, 1);
INSERT INTO test VALUES (2, 1);
INSERT INTO test VALUES (3, 1);
INSERT INTO test VALUES (4, 2);
INSERT INTO test VALUES (2, 2);
INSERT INTO test VALUES (1, 2);
SELECT * FROM test;

SELECT Name FROM Country;
SELECT Name FROM Country ORDER BY Name;
SELECT Name FROM Country ORDER BY Name DESC;
SELECT Name FROM Country ORDER BY Name ASC;
SELECT Name, Continent FROM Country ORDER BY Continent, Name;
SELECT Name, Continent, Region FROM Country ORDER BY Continent DESC, Region, Name;

//// 테스트 
DROP TABLE IF EXISTS booltest;
CREATE TABLE booltest (a INTEGER, b INTEGER);
INSERT INTO booltest VALUES (1, 0);
SELECT * FROM booltest;


// < 5 또는 > 3 이런 식으로 범위를 주고 싶을 때 사용 함.. If Else문과 똑같음 
SELECT 
    CASE WHEN a < 5 THEN 'true' ELSE 'false' END as boolA,
    CASE WHEN b THEN 'true' ELSE 'false' END as boolB
    FROM booltest
;

// 하나만 특정해서 고를 때 사용하는 것 IF ELSE문과 똑같지만 하나의 값이 맞는지 확인할 때 사용 
SELECT 
    CASE a WHEN "1" THEN 'true' ELSE 'false' END as boolA,
    CASE b WHEN 1 THEN 'true' ELSE 'false' END as boolB
    FROM booltest
;

// Sale 테이블을 S라 칭하고, S테이블에서 date, price값을 가져오고, Item 테이블을 I라 칭해서 description과 name을 가져와서 
// ID 값이 같은 것들을 묶어서 출력한다. 
SELECT s.id AS sale, s.date, i.name, i.description, s.price
    FROM sale AS s
    JOIN item AS i ON s.item_id = i.id
    ;

//Mulitple로 나눌 때 쓴다
SELECT c.name AS Cust, c.zip, i.name AS Item, i.description, s.quantity AS Quan, s.price
    FROM customer AS c
    LEFT JOIN sale AS s ON s.customer_id = c.id
    LEFT JOIN item AS i ON s.item_id = i.id
    ORDER BY CUST, ITEM
;
   
SELECT Name, LENGTH(Name) As Len FROM City ORDER BY Len ASC, Name;

SELECT SUBSTR('1 this string', 6);

// released에 있는 것을 쪼개서 파싱할 때 쓴다
SELECT released, 
    SUBSTR(released, 1, 4) AS Year, 
    SUBSTR(released, 6, 2) AS Month, 
    SUBSTR(released, 9, 2) AS Day
    FROM album ORDER BY released
    ;

// TRIM은 문자를 파싱하고 난 후 쪼갤 때 쓰는 것.. 그래서 LTRIM을 하면 왼쪽 것을 자르는 것
// RTRIM하면 오른쪽을 자름. 만약 특정 문자를 기준으로 자르고 싶다면 마지막 줄에 있는 것처럼 하면 됨
SELECT TRIM('    string    ');
SELECT LTRIM('    string    ');
SELECT RTRIM('    string    ');
SELECT RTRIM('.....string....', '.');


SELECT 'stRiNg' = 'string'; // 0으로 출력 됨. 왜냐? 같지 않으니까 대소문자 구분됨
SELECT LOWER('StRiNg') = LOWER('string'); // 1로 출력 됨. 왜냐? 둘 다 소문자로 변경했기 때문
SELECT UPPER('StRiNg') = UPPER('string'); // 1로 출력 됨. 왜냐? 둘 다 대문자로 변경했기 때문
SELECT UPPER(Name) FROM City ORDER BY Name; // World 데이터베이스 안에서 City 칼럼안에서 대문자만 출력
SELECT LOWER(Name) FROM City ORDER BY Name; // 소문자만 출력

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       # print(nums[-k:])
        #print(nums[:-k])
        nums1 = nums[-k:] + nums[:-k] 
        
        return (nums[:-k] + nums[-k:])

SELECT TYPEOF (1 + 1);
SELECT TYPEOF (1 + 1.0);
SELECT TYPEOF ('panda');
SELECT TYPEOF ('panda' + 'koala');

SELECT 1 / 2;
SELECT 1.0 / 2;
SELECT CAST(1 AS REAL) / 2;
SELECT 17 / 5;
SELECT 17 / 5, 17 % 5;

SELECT 2.5555;
SELECT ROUND(2.55555, 3); // ROUND UP을 소숫점 3자리까지만 하라는 뜻
SELECT ROUND(2.55555, 0); // 소숫점 자리 제한 없는 것. 그래서 바로 3이 됨
SELECT ROUND(2.55555);



// 시간 바꾸는거..
SELECT DATETIME('now');
SELECT DATE('now');
SELECT TIME('now');
SELECT DATETIME('now', '+1 day');
SELECT DATETIME('now', '+3 days');
SELECT DATETIME('now', '-1 month');
SELECT DATETIME('now', '+1 year');
SELECT DATETIME('now', '+3 hours', '+27 minutes', '-1 day', '+3 years');


// Region 중복된거 몇개 있는지 셀 때 씀
SELECT Region, COUNT(*) AS Count
    FROM Country
    GROUP BY Region
    ORDER BY Count DESC, Region
;
// GROUP BY는 Aggregate을 실행하기 전에 써야하는 것. 
// HAVING 은 Agrregate 하려고 씀 
// WHERE은 하나 특정할 때 씀.
SELECT a.title AS Album, COUNT(t.track_number) as Tracks
    FROM track AS t
    JOIN album AS a
        ON a.id = t.album_id
    WHERE a.artist = 'The Beatles'      
    GROUP BY a.id
    HAVING Tracks >= 10
    ORDER BY Tracks DESC, Album
;

// 요약하는 방법들..
SELECT COUNT(*) FROM Country;
SELECT COUNT(Population) FROM Country;
SELECT AVG(Population) FROM Country;
SELECT Region, AVG(Population) FROM Country DESC GROUP BY Region;
SELECT Region, MIN(Population), MAX(Population) FROM Country GROUP BY Region;
SELECT Region, SUM(Population) FROM Country GROUP BY Region;

SELECT COUNT(HeadOfState) FROM Country;
SELECT HeadOfState FROM Country ORDER BY HeadOfState;
SELECT * FROM Country;
SELECT COUNT(DISTINCT HeadOfState) FROM Country;

// Transaction 쓰는 법.. 아주 좋음.
// 트랜잭션이란? 
하나의 처리를 여러 단계로 다루는 기능을 트랜잭션(Transaction)이라고 합니다. 
하나의 처리를 Commit이라는 명령어를 수행하기전 마지막으로 한번 더 확인할 수 있는 기회를 줌으로써 좀더 안정적인 데이터베이스 작업을 가능하게 합니다. 
트랜잭션의 실행결과를 데이터베이스에 반영하는것을(Commit)이라고 하고 반영하기 전으로 되돌리는것을 롤백(RollBack)이라고 합니다. 


DROP TABLE IF EXISTS widgetInventory;
DROp TABLE IF EXISTS widgetSales;

CREATE TABLE widgetInventory (
    id INTEGER PRIMARY KEY,
    description TEXT,
    onhand INTEGER NOT NULL
);

CREATE TABLE widgetSales (
    id INTEGER PRIMARY KEY,
    inv_id INTEGER,
    quan INTEGER,
    price INTEGER
);

INSERT INTO widgetInventory ( description, onhand ) VALUES ('rock', 25);
INSERT INTO widgetInventory ( description, onhand ) VALUES ('paper', 21);
INSERT INTO widgetInventory ( description, onhand ) VALUES ('scissors', 25);

SELECT * FROM widgetInventory;
SELECT * FROM widgetSales;


//TRANSACTION 쓰는 법
BEGIN TRANSACTION;
INSERT INTO widgetSales (inv_id, quan, price) VALUES( 1, 5, 500 );
UPDATE widgetInventory SET onhand = ( onhand - 5 ) WHERE id = 1;
END TRANSACTION;


//롤벡하는법
BEGIN TRANSACTION;
INSERT INTO widgetInventory ( description, onhand) VALUES ('toy', 25);
ROLLBACK;
SELECT * FROM widgetInventory;


//트렌젝션을 쓰면 훨씬 속도가 빨라진다. 
// A transaction can drastically improve the performance of a set of write operations.
왜 빠르냐면 트렌젝션은  a number of statements are performed as a unit.


CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT);

BEGIN TRANSACTION;
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
INSERT INTO test ( data ) VALUES ( 'this is a good sized line of text.');
END TRANSACTION;

SELECT COUNT(*) FROM test

DROP TABLE test;



//트리거 트리거를 생성하면 테이블에 데이터 추가 및 업데이트 등을 한 경우 자동으로 다른 SQL 문을 실행할 수 있다. 
예를 들어 테이블의 컬럼 값을 업데이트하면 자동으로 다른 테이블의 컬럼 값을 같은 값으로 업데이트하는 등의 처리가 가능하다. 
여기에서는 트리거 생성 방법 등에 대해 설명한다.
출처: https://araikuma.tistory.com/702 [프로그램 개발 지식 공유]

CREATE table product (id integer, name text, price integer);
CREATE table log (id integer PRIMARY KEY, act, text);

CREATE trigger itrigger INSERT on product 
begin
    insert into log(act) values('INSERT Action');
end
;

CREATE trigger utrigger UPDATE on product
begin 
    Insert into log(act) values('UPDATE Action');
end
;

CREATE trigger dtrigger DELETE on product
begin
    INSERT into log(act) values('DELETE Action');
end
;

INSERT into product values (1,'book', 20000);
SELECT * FROM product;
SELECT * FROM log;

UPDATE product set price = 25000 WHERE id = 1;
DELETE from product WHERE id = 1;



// 트리거 and 트랜잭션 한번에 사용하는 방법
// 트리거를 사용해서 Update하는 것을 막을 수 있다. 트리거를 BEFORE를 사용해서 UPDATE 되기 전에, 하는 것을 막아 둔다면,
// TRANSACTION에서 업데이트를 하려고 한다고 할지라도, 업데이트가 되지 않는다. 트리거로 막아 뒀으니.. 아래 코드 참고


DROP TABLE IF EXISTS widgetSale;

CREATE TABLE widgetSale (id integer PRIMARY KEY, item_id INTEGER, customer_id INTEGER, quan INT, price INT, reconciled INT);

INSERT INTO widgetSale(item_id, customer_id, quan, price, reconciled) VALUES (1, 3, 5, 1995, 0);
INSERT INTO widgetSale(item_id, customer_id, quan, price, reconciled) VALUES (2, 2, 3, 1495, 1);
INSERT INTO widgetSale(item_id, customer_id, quan, price, reconciled) VALUES (3, 1, 1, 2995, 0);
SELECT * FROM widgetSale;

CREATE TRIGGER updateWidgetSale BEFORE UPDATE ON widgetSale
    BEGIN
        SELECT RAISE(ROLLBACK, 'cannot update table "widgetSale"') FROM widgetSale
            WHERE id = NEW.id AND reconciled = 1;
    END
;

BEGIN TRANSACTION;
    UPDATE widgetSale SET quan = 9 WHERE id = 2;
END TRANSACTION;

SELECT * FROM widgetSale;



select FirstName, LastName, City, State
from Person left join Address
on Person.PersonID = Address.PersonId;


# Write your MySQL query statement below
SELECT 
    IFNULL(
        (SELECT Distinct Salary 
        From Employee
        ORDER BY Salary Desc # Desc - Descending Order의 뜻 
        LIMIT 1 OFFSET 1), 
        NULL
    ) as SecondHighestSalary


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




SELECT S1.Score, COUNT(S2.Score) AS 'RANK' FROM Scores S1,
    (SELECT DISTINCT Score FROM Scores) S2
    WHERE S1.Score <= S2.Score
    GROUP BY S1.Id
    ORDER BY S1.Score DESC;
    


SELECT distinct Num as ConsecutiveNums from Logs as l
    WHERE Num = (Select Num FROM logs WHERE Id = l.Id -1) AND Num = (Select Num FROM logs WHERE Id = l.Id + 1)
    

SELECT E1.Name as Employee
    FROM Employee as E1, Employee as E2
    WHERE E1.ManagerId = E2.Id and E1.Salary > E2.Salary


    // DISTINCT를 안 넣으면 a@b.com가 두번 출력됨
SELECT DISTINCT a.Email FROM Person a JOIN Person b
        ON a.Email = b.Email
        WHERE a.Id <> b.Id

/둘다 됨
SELECT Email from Person  
    Group By Email
    Having Count(*) > 1;
    
    


SELECT DISTINCT a.Email FROM Person a JOIN Person b
    ON a.Email = b.Email
    WHERE a.Id <> b.Id
    
SELECT Email FROM Person 
    GROUP BY Email
    Having Count(*) > 1;
    
    GROUP BY Email = EMAIL을 정렬해서 중복 된거 빼고, 정렬 시킨다 그 다음 HAVING Count는 정렬 된 것 중 중복된 갯수가 1개 이상인 것들을 뽑아 내는 것.
    
    
SELECT E1.Email FROM Person E1 JOIN Person E2
    ON E1.Email = E2.EMAIL
    WHERE E1.Id <> E2.Id
    
SELECT DISTINCT E1.Email as Email FROM Person AS E1, Person AS E2
    WHERE E1.Email = E2.EMAIL AND E1.Id <> E2.Id

SELECT DISTINCT E1.Email as Email FROM Person AS E1, Person AS E2
    WHERE E1.Email = E2.EMAIL AND E1.Id <> E2.Id

    # Write your MySQL query statement below

SELECT Name as Customers from Customers as Cus
    LEFT JOIN Orders as O
    ON Cus.Id = O.CustomerId
    WHERE O.CustomerId IS NULL;

둘 다 가능! 

SELECT Name as Customers from Customers as C
    WHERE Id NOT IN (SELECT CustomerId from Orders);

# Write your MySQL query statement below

DELETE b FROM Person a, Person b
    WHERE a.Email = b.Email AND a.Id < b.Id;
    
SELECT W.name, W.population, W.area from World as W
    WHERE W.area > 3000000 OR W.population > 25000000;



# Write your MySQL query statement below

SELECT * FROM cinema 
    WHERE cinema.description <>'boring' AND cinema.id % 2 = 1 ORDER BY cinema.rating DESC


SELECT 
    CASE
        WHEN seat.id % 2 <> 0 AND seat.id < (SELECT COUNT(*) FROM seat) THEN seat.id +1 
        WHEN seat.id % 2 = 0 THEN seat.id - 1
        ELSE seat.id
    END AS id,
    student from seat
    ORDER BY id ASC;
    
# SELECT 하고 CASE 안에 것을 ()안에 묶어서 거기 나온 값을 as id로 명령해줘서 첫 번째 Row, 두 번째 Row는 student로 해준다 
# 다시말해서.. SELECT (CASE..) as id, student FROM seat ORDER BY id ASC 랑 똑같음 
# 만약 CASE문 전에 뭔가를 하고 싶다면, student, (CASE..), student FROM seat ORDER BY id ASC 처럼 그 앞에 쓸 거 넣으면 됨

SELECT 
    CASE
    WHEN seat.id % 2 <> 0 AND seat.id < (SELECT COUNT(seat.id) FROM seat) THEN seat.id + 1
    WHEN seat.id % 2 = 0 THEN seat.id - 1
    ELSE seat.id

SELECT
    (CASE 
    WHEN seat.id % 2 <> 0 AND seat.id < (SELECT COUNT(seat.id) FROM seat) THEN seat.id + 1
    WHEN seat.id % 2 = 0 AND seat.id < (SELECT COUNT(seat.id) FROM seat) THEN seat.id -1
    ELSE seat.id 
    END
    ) as id,
    student FROM seat
    ORDER BY id ASC;

UPDATE salary 
    SET 
       salary.sex = CASE salary.sex WHEN 'm' THEN 'f' ELSE 'm'
    END;



# Write your MySQL query statement below

SELECT p.FirstName, p.LastName, a.City, a.State FROM Person AS p
    LEFT JOIN Address AS a ON a.PersonId = p.PersonId;



# Write your MySQL query statement below
SELECT 
    IFNULL(
        (SELECT Distinct Salary 
        From Employee
        ORDER BY Salary Desc # Desc - Descending Order의 뜻 
        LIMIT 1 OFFSET 1), 
        NULL
    ) as SecondHighestSalary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((
          SELECT Distinct Salary FROM Employee 
          ORDER BY Salary DESC 
          LIMIT 1 OFFSET N
      ), NULL)
      
  );
END

SET N = N - 1


# Write your MySQL query statement below

SELECT S1.Score, COUNT(S2.Score) AS 'RANK' FROM Scores S1,
    (SELECT DISTINCT Score FROM Socres) S2
    WHERE S1.Score <= S2.Score
    GROUP BY S1.Id
    ORDER BY S1.Score DESC


SELECT S1.Score COUNT(S2.Score) as 'RANK' FROM Scores S1,
    (SELECT DISTINCT Score FROM Scores) S2



SELECT S1.Score, COUNT(S2.Score) AS 'RANK' FROM Scores S1,
    (SELECT DISTINCT Score FROM Scores) S2
    WHERE S1.Score <= S2.Score
    GROUP BY S1.Id
    ORDER BY S1.Score DESC;
    
SEECT Score,
    DENSE_RANK() over (ORDER BY score DESC) as 'Rank'
    FROM Scores

// DENSE_RANK는 중간에 비는 숫자 없이 1 ~ N까지 원하는 순서래도 쭉 써줌
// RANK는 중간에 비는 숫자가 있음. 예를 들어 4.0 4.0 이 두 번 들어있고 그 다음 3.87 이 있다면
// DENSE_RANK 는 1 1 2 3 4.. 이렇게 순서가 되고
// RANK 는 1 1 3 4 5.. 이렇게 됨. 2를 건너뛰고 3이 된다. 그 이유는
// 11이 두개 있어서 



SELECT DISTINCT Num as ConsecutiveNums  FROM Logs as l
    WHERE Num = (SELECT Num from Logs WHERE Id = l.Id -1) AND Num = (SELECT Num from Logs WHERE Id = l.Id + 1)

SELECT E1.Name AS Customers FROM Customers E1
    WHERE Id NOT IN (SELECT CustomerId FROM Orders)


# Write your MySQL query statement below

SELECT D.Name as Department, E.Name as Employee, E.Salary as Salary 
    FROM Employee E, Department D
    WHERE D.Id = E.DepartmentId 
    AND E.Salary = (SELECT max(Salary) FROM Employee E2 WHERE E2.DepartmentId = D.Id)





SELECT Department.Name as Department, Employee.Name as Employee, Employee.Salary FROM Employee, Department
    WHERE Department.Id = Employee.DepartmentId AND Employee.Salary = (SELECT max(Salary) FROM Employee WHERE Department.Id = Employee.DepartmentId) 
    

SELECT DISTINCT E1.Email as Email FROM Person as E1 JOIN Person as E2
    WHERE E1.Id <> E2.Id AND E1.Email = E2.Email
    
SELECT Name as Customers FROM Customers 
    WHERE Customers.Id NOT IN (SELECT CustomerId FROM Orders)

DELETE b FROM Person a, Person b
    WHERE a.Id < b.Id AND a.Email = b.Email

DELETE P2 FROM Person P, Person P2
    WHERE P.Id < P2.Id AND P.Email = P2.Email

# Write your MySQL query statement below

SELECT W1.id as id FROM Weather W1, Weather W2
    WHERE W1.Temperature > W2.Temperature AND TO_DAYS(W1.recordDate) = TO_DAYS(W2.recordDate) +1;
    

# TO_DAYS를 하는 이유는 Date이라서 그런 것
# 원래라면 W1.recordDate = W2.recordDate + 1 으로 해도 되지만,
# 그렇게 했더니 계속 ERROR가 나고, Date만 바꾸려면 TO_DAYS를 붙여서 함 

# Write your MySQL query statement below

SELECT w.name as name, w.population as population, w.area as area
    FROM World as w
    WHERE 3000000 < w.area OR 25000000 < w.population
;


SELECT DISTINCT class FROM courses 
    GROUP BY class HAVING COUNT(DISTINCT student)>=5;
// class별로 나누고 그 클레스에 맞는 Student를 카운트하라. 

# Write your MySQL query statement below

SELECT DISTINCT s1.* FROM Stadium as s1, Stadium as s2, Stadium as S3
    WHERE 
    ((s1.id + 1 = s2.id AND s1.id + 2 = s3.id) 
     OR (s1.id -1 = s2.id AND s1.id + 1 = s3.id) 
     OR (s1.id -2 = s2.id AND s1.id -1 = s3.id))
     AND s1.people >= 100
     AND s2.people >= 100
     AND s3.people >= 100
     ORDER BY s1.id ASC



SELECT Distinct s1.id, s1.visit_date, s1.people FROM stadium as s1, stadium s2, stadium s3
    WHERE ((s1.id + 1 = s2.id AND s1.id + 2= s3.id)
    OR (s1.id - 1 = s2.id AND s1.id + 1 = s3.id)
    OR (s1.id - 2 = s2.id AND s1.id - 1 = s3.id))
    AND s1.people >= 100 
    AND s2.people >= 100 
    AND s3.people >= 100
    ORDER BY s1.id ASC 


SELECT id, movie, description, rating FROM cinema
    WHERE cinema.id % 2 = 1 AND cinema.description <> 'boring'
    ORDER BY cinema.rating DESC
    
596번 문제, 197번 문제, 184번 문제, 183번, 181번 문제, 177번 문제 

197. Rising Temperature
SELECT w2.id FROM Weather w1, Weather w2
    WHERE w1.Temperature < w2.Temperature AND TO_DAYS(w1.recordDate) + 1 = TO_DAYS(w2.recordDate)

178. Rank Scores
SELECT s1.Score, Count(s2.Score) as 'Rank' FROM Scores S1, (SELECT DISTINCT Score FROM Scores) S2
    WHERE s1.Score <= s2.Score
    GROUP BY s1.Id
    ORDER BY s1.Score DESC 

184. Department Highest Salary
SELECT D.Name as Department, E.Name as Employee, E.Salary as Salary 
    FROM Employee E, Department D
    WHERE D.Id = E.DepartmentId 
    AND E.Salary = (SELECT max(Salary) FROM Employee E2 WHERE E2.DepartmentId = D.Id)

183. Customers Who Never Order
SELECT c.Name as Customers FROM Customers c
    WHERE c.Id NOT IN (SELECT CustomerId FROM Orders)

177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT IFNULL((
          SELECT Distinct Salary FROM Employee 
          ORDER BY Employee.Salary DESC
          Limit 1 OFFSET N
      ), NULL)
  );
END

196. Delete Duplicate Emails
DELETE P2 FROM Person P, Person P2
    WHERE P.Id < P2.Id AND P.Email = P2.Email

191. pdate Salary 
UPDATE salary 
    SET 
       salary.sex = CASE salary.sex WHEN 'm' THEN 'f' ELSE 'm'
    END;
    
596. Classes More Than 5 Students
SELECT class FROM courses
    GROUP BY courses.class HAVING count(courses.student) >= 5

175. Combine Two Tables
SELECT p.FirstName, p.LastName, a.City, a.State FROM Person AS p
    LEFT JOIN Address AS a ON a.PersonId = p.PersonId;

