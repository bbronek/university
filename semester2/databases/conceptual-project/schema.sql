------------ DROP TABLES ------------

drop table if exists Model_engine;
go

drop table if exists Dealer_model;
go

drop table if exists Vehicle_equipment;
go

drop table if exists Equipment;
go

drop table if exists Truck;
go

drop table if exists Passenger_car;
go

drop table if exists Sale;
go

drop table if exists Customer;
go

drop table if exists Vehicle;
go

drop table if exists Dealer;
go

drop table if exists Model;
go

drop table if exists Brand;
go

drop table if exists Engine;
go

------------ CREATE - CREATE TABLES AND RELATIONSHIPS ------------

CREATE TABLE Brand
(
    name           VARCHAR(25) PRIMARY KEY,
    foundation_year   INT
);

CREATE TABLE Model
(
  id                VARCHAR(20) PRIMARY KEY,
  introduction_year  INT,
  Brand_name       VARCHAR(25)  NOT NULL REFERENCES Brand(name),
  Model_id          VARCHAR(20)  REFERENCES Model(id)
);

CREATE TABLE Passenger_car
(
    passenger_count    INT,
    trunk_capacity INT,
    Model_id    VARCHAR(20) REFERENCES Model(id),
    PRIMARY KEY (Model_id)
);

CREATE TABLE Truck
(
    payload INT,
    Model_id    VARCHAR(20) REFERENCES Model(id),
    PRIMARY KEY (Model_id)
);

CREATE TABLE Engine
(
    id  VARCHAR(20) PRIMARY KEY,
    fuel_type   VARCHAR(10),
    specifications  VARCHAR(20)
);

CREATE TABLE Model_engine
(
    Model_id    VARCHAR(20) REFERENCES Model(id),
    Engine_id   VARCHAR(20) REFERENCES Engine(id),
    PRIMARY KEY (Model_id,Engine_id)

);

CREATE TABLE Dealer
(
    name   VARCHAR(20) PRIMARY KEY,
    address   VARCHAR(20)
);

CREATE TABLE Vehicle
(
  VIN               CHAR(17)    PRIMARY KEY,
  production_year     INT,
  transmission   VARCHAR(20),
  country_of_origin  VARCHAR(15),
  mileage          INT,
  Engine_id         VARCHAR(20)  NOT NULL REFERENCES Engine(id),
  Model_id          VARCHAR(20)  NOT NULL REFERENCES Model(id),
  Dealer_name      VARCHAR(20) REFERENCES Dealer(name)
);

CREATE TABLE Equipment
(
  name  VARCHAR(20) PRIMARY KEY

);

CREATE TABLE Vehicle_equipment
(
    Equipment_name    VARCHAR(20) REFERENCES Equipment(name),
    Vehicle_VIN                   CHAR(17) REFERENCES Vehicle(VIN),
    PRIMARY KEY (Equipment_name,Vehicle_VIN)
);


CREATE TABLE Dealer_model
(
    Dealer_name        VARCHAR(20) REFERENCES Dealer(name),
    Model_id            VARCHAR(20) REFERENCES Model(id),
    PRIMARY KEY (Dealer_name,Model_id)
);

CREATE TABLE Customer
(
    id                  VARCHAR(20) PRIMARY KEY,
    first_name                VARCHAR(20),
    last_name            VARCHAR(20),
    phone_number      CHAR(9)
);

CREATE TABLE Sale
(
    Customer_id    VARCHAR(20)     NOT NULL REFERENCES Customer(id),
    Vehicle_VIN CHAR(17)        NOT NULL REFERENCES Vehicle(VIN),
    Dealer_name VARCHAR(20)     NOT NULL REFERENCES Dealer(name),
    date         DATE,
    price         INT,
    PRIMARY KEY (Customer_id,Vehicle_VIN,Dealer_name,date)

);
GO


------------ INSERT - INSERT DATA ------------

INSERT INTO Brand   VALUES ('audi',1909);
INSERT INTO Brand   VALUES ('bmw',1916);

INSERT INTO Model   VALUES ('12345',1954,'audi',NULL);
INSERT INTO Model   VALUES ('54879',1908,'bmw','12345');

INSERT INTO Passenger_car VALUES (4,120,'12345');
INSERT INTO Truck VALUES (8574,'54879');

INSERT INTO Engine VALUES ('24','petrol','good');

INSERT INTO Model_engine VALUES ('12345','24');
INSERT INTO Model_engine VALUES ('54879','24');

INSERT INTO Equipment VALUES ('keychain');


INSERT INTO Dealer Values ('Karl', 'SchwarzStraBe');
INSERT INTO Dealer Values ('Thomas', 'LuftwafeStraBe');

INSERT INTO Vehicle VALUES ('12345678945612387',1967,'drty6','Germany',54,'24','12345','Karl');
INSERT INTO Vehicle VALUES ('45698712365874956',1914,'reqw','Germany',5487,'24','54879','Thomas');

INSERT INTO Vehicle_equipment VALUES ('keychain','12345678945612387');

INSERT INTO Dealer_model Values ('Karl', '12345');
INSERT INTO Dealer_model Values ('Thomas', '54879');

INSERT INTO Customer Values ('123', 'Jan', 'Przerwa', '123456789');
INSERT INTO Customer Values ('789', 'Janusz', 'Tetmajer', '759841263');

INSERT INTO Sale Values ('123','12345678945612387','Karl', '2017-05-26',58745);

------------ SELECT ------------
SELECT * FROM Brand;
SELECT * FROM Model;
SELECT * FROM Passenger_car;
SELECT * FROM Truck;
SELECT * FROM Engine;
SELECT * FROM Model_engine;
SELECT * FROM Vehicle;
SELECT * FROM Equipment;
SELECT * FROM Vehicle_equipment;
SELECT * FROM Customer;
SELECT * FROM Sale;
