------------ USUŃ TABELE ------------

drop table if exists Posiada2
go

drop table if exists Posiada4
go

drop table if exists Posiada6
go

drop table if exists Dodatkowe_wyposazenie
go

drop table if exists Samochod_ciezarowy
go

drop table if exists Samochod_osobowy
go

drop table if exists Sprzedaz
go

drop table if exists Klient
go

drop table if exists Samochod
go

drop table if exists Dealer
go

drop table if exists Model
go

drop table if exists Marka
go

drop table if exists Silnik
go

------------ CREATE - UTWÓRZ TABELE I POWIĄZANIA ------------

CREATE TABLE Marka
(
    nazwa           VARCHAR(25) PRIMARY KEY,
    rok_zalozenia   INT
);

CREATE TABLE Model
(
  id                VARCHAR(20) PRIMARY KEY,
  rok_wprowadzenia  INT,
  Marka_nazwa       VARCHAR(25)  NOT NULL REFERENCES Marka(nazwa),
  Model_id          VARCHAR(20)  REFERENCES Model(id)
);

CREATE TABLE Samochod_osobowy
(
    liczba_pasazerow    INT,
    pojemnosc_bagaznika INT,
    Model_id    VARCHAR(20) REFERENCES Model(id),
    PRIMARY KEY (Model_id)
);

CREATE TABLE Samochod_ciezarowy
(
    ladownosc INT,
    Model_id    VARCHAR(20) REFERENCES Model(id),
    PRIMARY KEY (Model_id)
);

CREATE TABLE Silnik
(
    id  VARCHAR(20) PRIMARY KEY,
    rodzaj_paliwa   VARCHAR(10),
    opis_paramtrow  VARCHAR(20)
);

CREATE TABLE Posiada2
(
    Model_id    VARCHAR(20) REFERENCES Model(id),
    Silnik_id   VARCHAR(20) REFERENCES Silnik(id),
    FOREIGN KEY (Model_id) REFERENCES Model(id),
    PRIMARY KEY (Model_id,Silnik_id)

);

CREATE TABLE Dealer
(
    nazwa   VARCHAR(20) PRIMARY KEY,
    adres   VARCHAR(20)
);

CREATE TABLE Samochod
(
  VIN               CHAR(17)    PRIMARY KEY,
  rok_produkcji     INT,
  skrzynia_biegow   VARCHAR(20),
  kraj_pochodzenia  VARCHAR(15),
  przebieg          INT,
  Silnik_id         VARCHAR(20)  NOT NULL REFERENCES Silnik(id),
  Model_id          VARCHAR(20)  NOT NULL REFERENCES Model(id),
  Dealer_nazwa      VARCHAR(20) REFERENCES Dealer(nazwa)
);

CREATE TABLE Dodatkowe_wyposazenie
(
  nazwa  VARCHAR(20) PRIMARY KEY

);

CREATE TABLE Posiada6
(
    Dodatkowe_wyposazenie_nazwa    VARCHAR(20) REFERENCES Dodatkowe_wyposazenie(nazwa),
    Samochod_VIN                   CHAR(17) REFERENCES Samochod(VIN),
    FOREIGN KEY (Samochod_VIN) REFERENCES Samochod(VIN),
    PRIMARY KEY (Dodatkowe_wyposazenie_nazwa,Samochod_VIN)
)



CREATE TABLE Posiada4
(
    Dealer_nazwa        VARCHAR(20) REFERENCES Dealer(nazwa),
    Model_id            VARCHAR(20) REFERENCES Model(id),
    FOREIGN KEY (Dealer_nazwa) REFERENCES Dealer(nazwa),
    PRIMARY KEY (Dealer_nazwa,Model_id)
);

CREATE TABLE Klient
(
    id                  VARCHAR(20) PRIMARY KEY,
    imie                VARCHAR(20),
    nazwisko            VARCHAR(20),
    numer_telefonu      CHAR(9)
);

CREATE TABLE Sprzedaz
(
    Klient_id    VARCHAR(20)     NOT NULL REFERENCES Klient(id),
    Samochod_VIN CHAR(17)        NOT NULL REFERENCES Samochod(VIN),
    Dealer_nazwa VARCHAR(20)     NOT NULL REFERENCES Dealer(nazwa),
    data         DATE,
    cena         INT,
    PRIMARY KEY (Klient_id,Samochod_VIN,Dealer_nazwa,data)

);
GO


------------ INSERT - WSTAW DANE ------------

INSERT INTO Marka   VALUES ('audi',1909);
INSERT INTO Marka   VALUES ('bmw',1916);

INSERT INTO Model   VALUES ('12345',1954,'audi',NULL);
INSERT INTO Model   VALUES ('54879',1908,'bmw','12345');

INSERT INTO Samochod_osobowy VALUES (4,120,'12345');
INSERT INTO Samochod_ciezarowy VALUES (8574,'54879');

INSERT INTO Silnik VALUES ('24','benzyna','dobry');

INSERT INTO Posiada2 VALUES ('12345','24');
INSERT INTO Posiada2 VALUES ('54879','24');

INSERT INTO Dodatkowe_wyposazenie VALUES ('brelok');

INSERT INTO Posiada6 VALUES ('brelok','12345678945612387');

INSERT INTO Dealer Values ('Karl', 'SchwarzStraBe');
INSERT INTO Dealer Values ('Thomas', 'LuftwafeStraBe');

INSERT INTO Samochod VALUES ('12345678945612387',1967,'drty6','Niemcy',54,'24','12345','Karl');
INSERT INTO Samochod VALUES ('45698712365874956',1914,'reqw','Niemcy',5487,'24','54879','Thomas');

INSERT INTO Posiada4 Values ('Karl', '12345');
INSERT INTO Posiada4 Values ('Thomas', '54879');

INSERT INTO Klient Values ('123', 'Jan', 'Przerwa', '123456789');
INSERT INTO Klient Values ('789', 'Janusz', 'Tetmajer', '759841263');

INSERT INTO Sprzedaz Values ('123','12345678945612387','Karl', '2017-05-26',58745);

------------ SELECT ------------
SELECT * FROM Marka;
SELECT * FROM Model;
SELECT * FROM Samochod_osobowy;
SELECT * FROM Samochod_ciezarowy;
SELECT * FROM Silnik;
SELECT * FROM Posiada2;
SELECT * FROM Samochod;
SELECT * FROM Dodatkowe_wyposazenie;
SELECT * FROM Posiada6;
SELECT * FROM Klient;
SELECT * FROM Sprzedaz;






