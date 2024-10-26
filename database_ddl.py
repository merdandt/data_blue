STUDENT = """CREATE TABLE STUDENT(
StudentID Int Not Null IDENTITY (1,1),
LastName CHAR(30) Not Null,
FirstName CHAR(30) Not Null,
Major CHAR(30) Null,
DateofBirth datetime Null,
StartYear char(30) Not Null,
Email varchar(50) Not Null,
State char(2) Not Null,
Gender Char(1) Not Null,
CONSTRAINT STUDENT_PK Primary key(StudentID),
);

CREATE TABLE ACTIVITY (
ActivityID Int Not Null IDENTITY (1,1),
Description CHAR(30) Not Null,
Fee numeric(5,2) Null,
Risk int Null,
MinAge int Null,
CONSTRAINT ACTIVITY_PK Primary key(ActivityID),
);

CREATE TABLE STUDENT_ACTIVITY(
StudentID Int Not Null,
ActivityID Int Not Null,
Fee_Paid numeric(5,2) Null,
StartDate DateTime Null,
EndDate DateTime Null,
CONSTRAINT STUDENT_ACTIVITY_PK Primary key(StudentID, ActivityID),
CONSTRAINT STUDENT_STUDENT_ACTIVITY_FK FOREIGN KEY (StudentID) REFERENCES
STUDENT(StudentID),
CONSTRAINT ACTIVITY_STUDENT_ACTIVITY_FK FOREIGN KEY (ActivityID) REFERENCES
ACTIVITY(ActivityID),
);

CREATE TABLE GYM_LOCKER(
LockerNumber Int Not Null IDENTITY(224,1),
LockerLocation CHAR(30) Not Null,
LockerCombination INT NOT NULL,
StudentID Int Null,
StartDate DateTime Null,
EndDate DateTime Null,
CONSTRAINT LOCKER_PK Primary key(LockerNumber),
CONSTRAINT STUDENT_LOCKER_FK FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
);

CREATE TABLE AWARD(
AwardID Int Not Null IDENTITY(1,1),
Description Char(30) Not Null,
CashPrize numeric(5,2) Null,
CONSTRAINT AWARD_PK Primary key(AwardID),
);

CREATE TABLE STUDENT_AWARD(
StudentID Int Not Null,
AwardID Int Not Null,
AwardYear Int Not Null,
CONSTRAINT STUDENT_AWARD_PK Primary key(StudentID, AwardID),
CONSTRAINT STUDENT_AWARD_STUDENT_FK FOREIGN KEY (StudentID) REFERENCES
STUDENT(StudentID),
CONSTRAINT ACTIVITY_STUDENT_AWARD_FK FOREIGN KEY (AwardID) REFERENCES
AWARD(AwardID),
);


CREATE TABLE FACULTY (
FID INT NOT NULL,
LastName CHAR(30) NOT NULL,
FirstName CHAR(30) NOT NULL,
Department CHAR(30) NOT NULL,
CONSTRAINT FACULTY_PK PRIMARY KEY(FID)
);

CREATE TABLE CLASS (
CRN INT NOT NULL,
ClassName CHAR(50) NOT NULL,
Semester_Taught CHAR(30) NOT NULL,
FID INT NOT NULL,
CONSTRAINT CLASS_PK Primary Key(CRN),
CONSTRAINT CLASS_FACULTY_FK FOREIGN KEY(FID) REFERENCES FACULTY(FID),
);

CREATE TABLE STUDENT_CLASS (
StudentID INT NOT NULL,
CRN INT NOT NULL,
Semester CHAR(15) NOT NULL,
Last_Day_Attended DateTime NULL,
CONSTRAINT STUDENT_CLASS_PK Primary Key(CRN, StudentID),
CONSTRAINT STUDENT_CLASS_STUDENT_FK FOREIGN KEY(StudentID) REFERENCES STUDENT
(StudentID),
CONSTRAINT STUDENT_CLASS_CLASS_FK FOREIGN KEY(CRN) REFERENCES CLASS (CRN),
);
"""

ANTIQUE = """CREATE TABLE CUSTOMER(
CustomerID Int NOT Null IDENTITY (1,1),
LastName Char(30) Not Null,
FirstName Char(30) Not Null,
City Char(30) Null,
State Char(2) Null,
CONSTRAINT CUSTOMER_PK Primary key(CustomerID)
);

CREATE TABLE EMPLOYEE(
EmployeeID Int NOT Null IDENTITY (1,1),
LastName Char(30) Not Null,
FirstName Char(30) Not Null,
City Char(30) Null,
State Char(2) Null,
Gender Char(10) Not Null,
Salary Decimal(10,2) Not Null,
ManagerID INT NULL,
CONSTRAINT EMPLOYEE_PK Primary key(EMPLOYEEID),
CONSTRAINT EMPLOYEE_EMPLOYEE_FK FOREIGN KEY (MANAGERID) REFERENCES
EMPLOYEE(EMPLOYEEID),
);

CREATE TABLE PRODUCT(
Productid Int NOT Null IDENTITY (1,1),
ProductName Char(30) Not Null,
MetalType Char(30) Not Null,
QualityID INT Not Null,
ProductCountry Char(30) Not Null,
VendorID INT Null,
CONSTRAINT PRODUCT_PK Primary key(PRODUCTID),
);

CREATE TABLE SALE(
SaleID Int NOT Null IDENTITY (1,1),
CustomerID INT,
EmployeeID INT,
SaleDate DATETIME NOT NULL,
CONSTRAINT SALE_PK PRIMARY KEY(SaleID),
CONSTRAINT SALE_CUSTOMER_FK FOREIGN KEY (CustomerID) REFERENCES
Customer(CustomerID),
CONSTRAINT SALE_EMPLOYEE_FK FOREIGN KEY (EmployeeID) REFERENCES
Employee(EmployeeID),
);

CREATE TABLE SALE_ITEM(
SALEID INT NOT NULL,
ItemID Int NOT NULL,
UnitPrice Numeric (20,2) NOT NULL,
Quantity Int NOT NULL,
CONSTRAINT SALE_ITEM_PK PRIMARY KEY (SaleID, ItemID),
CONSTRAINT SALE_ITEM_FK FOREIGN KEY (SaleID) REFERENCES SALE(SaleID),
CONSTRAINT SALE_ITEM_PRODUCT_FK FOREIGN KEY (ItemID) REFERENCES Product(ProductID)
);

CREATE TABLE TRAINING_COURSE(
TrainingID Int NOT Null IDENTITY (1,1),
TrainingName Char(30) NOT NULL,
TrainingDescription Char(50) NOT NULL,
TrainingCost Numeric (20,2) NOT NULL,
CONSTRAINT TRAINING_PK PRIMARY KEY (TrainingID),
);

CREATE TABLE EMPLOYEE_TRAINING(
EmployeeID INT NOT NULL,
TrainingID Int NOT NULL,
Grade Char(1) NULL,
CompletionDate DATETIME NULL,
CONSTRAINT E_TRAINING_PK PRIMARY KEY (EmployeeID, TrainingID),
CONSTRAINT EMPLOYEE_T_FK FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE(EmployeeID),
CONSTRAINT TRAINING_T_FK FOREIGN KEY (TrainingID) REFERENCES
TRAINING_COURSE(TrainingID),
);
"""

PLANET = """CREATE TABLE PLANET(
PlanetID Int Not Null IDENTITY (1,1),
Name Char(30) Not Null,
Mass Numeric(10,3) Not Null,
Diameter BigInt Not Null,
Density BigInt Null,
Gravity Numeric(8,1) Not Null,
RotationPeriod Numeric(8,2) Not Null,
LengthofDay Numeric(8,1) Not Null,
DistanceFromSun Numeric(8,1) Null,
OrbitalPeriod Numeric(9,2) Not Null,
Moons Int Null,
Location Char(10) Null,
Interest Char(10) Null,
CONSTRAINT PLANET_PK Primary key(PlanetID),
);
"""