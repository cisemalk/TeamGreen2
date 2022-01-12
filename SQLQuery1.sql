DELETE FROM TblEmployees
DECLARE @A INT = 0;

WHILE @A<50
BEGIN
INSERT INTO TblEmployees (EmpName, EmpSurname, EmpAddress, EmpPhone) VALUES (NEWID(),NEWID(),NEWID(),(SELECT FLOOR(RAND()*(20-10+1))+10))
SET @A = @A+1;
END;