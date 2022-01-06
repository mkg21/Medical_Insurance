CREATE DATABASE medical_insurance;
USE medical_insurance;

CREATE TABLE customer
  (
     id      INT NOT NULL auto_increment PRIMARY KEY,
     f_name  VARCHAR(20) NOT NULL,
     m_name  VARCHAR(20) NOT NULL,
     l_name  VARCHAR(20) NOT NULL,
     e_mail  VARCHAR(30) NOT NULL,
     address VARCHAR(50) NOT NULL,
     b_date  DATE NOT NULL,
     gender  VARCHAR(6) NOT NULL,
     phone   CHAR(11) NOT NULL
  );

CREATE TABLE dependent
  (
     cus_id  INT NOT NULL,
     name    VARCHAR(20) NOT NULL,
     b_date  DATE NOT NULL,
     gender  VARCHAR(6) NOT NULL,
     kinship VARCHAR(20) NOT NULL,
     FOREIGN KEY (cus_id) REFERENCES customer (id),
     PRIMARY KEY (cus_id, name, kinship)
  );

CREATE TABLE hospital
  (
     id      INT NOT NULL auto_increment PRIMARY KEY,
     name    VARCHAR(20) NOT NULL,
     address VARCHAR(50) NOT NULL,
     e_mail  VARCHAR(30) NOT NULL,
     phone   CHAR(11) NOT NULL
  );

CREATE TABLE plan
  (
     id       INT NOT NULL auto_increment PRIMARY KEY,
     type     VARCHAR(20) UNIQUE NOT NULL,
     benefits TEXT NOT NULL,
     price    DECIMAL(8, 2) NOT NULL
  );

CREATE TABLE enrolled
  (
     hos_id  INT NOT NULL,
     plan_id INT NOT NULL,
     FOREIGN KEY (hos_id) REFERENCES hospital (id),
     FOREIGN KEY (plan_id) REFERENCES plan (id),
     UNIQUE no_dup (hos_id, plan_id)
  );

CREATE TABLE contract
  (
     id       INT NOT NULL auto_increment PRIMARY KEY,
     plan_id  INT NOT NULL,
     cus_id   INT DEFAULT NULL UNIQUE,
     res_id   INT DEFAULT NULL,
     dep_name VARCHAR(20) DEFAULT NULL,
     kinship  VARCHAR(20) DEFAULT NULL,
     payment_method  VARCHAR(20),
     FOREIGN KEY (cus_id) REFERENCES customer (id),
     FOREIGN KEY (res_id, dep_name, kinship) REFERENCES dependent (cus_id, name, kinship),
     FOREIGN KEY (plan_id) REFERENCES plan (id),
     UNIQUE res_id (res_id, dep_name, kinship),

     CHECK ((cus_id IS NOT NULL) OR ( res_id IS NOT NULL AND dep_name IS NOT NULL AND kinship IS NOT NULL )),
     CHECK ((cus_id IS NULL AND res_id IS NOT NULL) OR (cus_id IS NOT NULL AND res_id IS NULL))
  );

CREATE TABLE claim
  (
     id               INT NOT NULL auto_increment PRIMARY KEY,
     con_id           INT NOT NULL,
     hos_id           INT NOT NULL,
     expenses         DECIMAL(10, 2) NOT NULL,
     expenses_subject TEXT NOT NULL,
     expenses_details TEXT NOT NULL,
     status           TINYINT DEFAULT NULL,
     f_date             DATE NOT NULL,
     FOREIGN KEY (con_id) REFERENCES contract (id),
     FOREIGN KEY (hos_id) REFERENCES hospital (id)
  );


/*------------------------------  SAMPLE DATA -----------------------------------------*/

insert into customer values(DEFAULT, 'Hany','Ahmed','Mahmoud','Hany123@gmail.com','11 nasr street, cairo governorat','1963-09-15','male','01112151718');
insert into customer values(DEFAULT, 'Omar','Mohamed','Madgy','Omar123@gmail.com','24 Hassan street, Ghardaka governorate','1968-02-17','male','01012151718');
insert into customer values(DEFAULT, 'Hoda','Emad','Fawzy','Hoda123@gmail.com','13 alnakheel street, Mansoura governorate','1981-05-15','female','01112151718');
insert into customer values(DEFAULT, 'Noor','Naser','Mahmoud','Noor123@gmail.com','18 Foad street, Alexandira','1978-12-25','male','01012151777');
insert into customer values(DEFAULT, 'Sara','Akram','Hassan','Sara123@gmail.com','11 nasr street, cairo governorat','1988-06-15','female','01512151718');
insert into customer values(DEFAULT, 'Hany','Yasser','Saad','Hany2123@gmail.com','11 nasr street, cairo governorat','1963-01-22','male','01112153389');
insert into customer values(DEFAULT, 'Mazen','Mostafa','Talaat','Mazen123@gmail.com','18 Foad street, Alexandira','1967-09-15','male','01112166692');
insert into customer values(DEFAULT, 'Malek','Emad','Mandoor','Malek123@gmail.com','13 alnakheel street, Mansoura governorate','1973-03-12','male','01013350078');

insert into dependent values(1,'Maria','2000-03-15','female','daughter');
insert into dependent values(1,'Magy','2003-03-17','female','daughter');
insert into dependent values(2,'rafat','2008-11-01','male','son');
insert into dependent values(4,'karim','2005-03-11','male','son');
insert into dependent values(6,'Maha','2000-12-11','female','daughter');
insert into dependent values(6,'yara','2007-03-11','female','daughter');
insert into dependent values(6,'Dina','1975-03-11','female','wife');
insert into dependent values(7,'ali','2000-01-11','male','son');
insert into dependent values(7,'Yousef','2002-08-08','male','son');
insert into dependent values(7,'Taher','1997-03-11','male','son');
insert into dependent values(7,'Sahar','1977-03-11','female','wife');



insert into plan values (DEFAULT, 'Basic','5% coverage',6000.00);
insert into plan values (DEFAULT, 'Premium','15% coverage',10000.00);
insert into plan values (DEFAULT, 'Golden','30% coverage',15000.00);



insert into contract values (DEFAULT, 1, 1, null, null,null,'Cash, visa');
insert into contract values (DEFAULT, 3, 2, null, null,null,'Cash, visa');
insert into contract values (DEFAULT, 3, 3, null, null,null,'Master Card,cash');
insert into contract values (DEFAULT, 3, 4, null, null,null,'Master Card,cash');
insert into contract values (DEFAULT, 3, 5, null, null,null,'Master Card,cash');
insert into contract values (DEFAULT, 3, 6, null, null ,null,'Cash, visa');
insert into contract values (DEFAULT, 3, 7, null, null,null,'Cash, visa');
insert into contract values (DEFAULT, 3, 8, null, null,null,'Cash, visa');

insert into contract values (DEFAULT, 3, null, 1, 'Maria', 'daughter','Cash, visa');
insert into contract values (DEFAULT, 2, null, 1, 'Magy', 'daughter','Cash, visa');
insert into contract values (DEFAULT, 2, null, 2, 'rafat', 'son','Cash, visa');
insert into contract values (DEFAULT, 2, null, 4, 'karim', 'son','Cash, visa');
insert into contract values (DEFAULT, 2, null, 6, 'Maha', 'daughter','Cash, visa');
insert into contract values (DEFAULT, 1, null, 6, 'yara', 'daughter','Cash, visa');
insert into contract values (DEFAULT, 1, null, 6, 'Dina', 'wife','Cash, visa');
insert into contract values (DEFAULT, 1, null, 7, 'ali', 'son','Cash, visa');
insert into contract values (DEFAULT, 2, null, 7, 'Yousef', 'son','Cash, visa');
insert into contract values (DEFAULT, 3, null, 7, 'Taher', 'son','Cash, visa');
insert into contract values (DEFAULT, 3, null, 7, 'Sahar', 'wife','Cash, visa');


insert into hospital values (DEFAULT, 'Dar Elshefa','21 alfath street, tanta governorate','Dar Elshefa322@gmail.com','01093344535');
insert into hospital values (DEFAULT, 'Abn sina','24 Hassan street, Ghardaka governorate','Abnasin223@gmail.com','01093399995');
insert into hospital values (DEFAULT, 'Celopatra','15 Foadalgendy street, tanta governorate','celopatra999@gmail.com','01193399995');
insert into hospital values (DEFAULT, 'Al gama','16 altahreer square, cairo governorate','Algama224@gmail.com','01093399999');
insert into hospital values (DEFAULT, 'Alkinanah','11 nasr street, cairo governorate','Alkinana111@gmail.com','01297799995');
insert into hospital values (DEFAULT, 'Tiba','13 alhelw street, tanta governorate','Tiba307@gmail.com','01000465772');
insert into hospital values (DEFAULT, 'Alfyrooz','17 alahraam gardens, cairo governorate','Alfyrooz467@gmail.com','01022399995');
insert into hospital values (DEFAULT, 'Alamrican','18 Foad street, Alexandira','Alamrican468@gmail.com','01155599995');
insert into hospital values (DEFAULT, 'Alandalos','19 alimobarak street, tanta governorate','Alandalos469@gmail.com','01593399995');
insert into hospital values (DEFAULT, 'Almaidan','13 alnakheel street, Mansoura governorate','Almaidan4610@gmail.com','01577790995');

insert into enrolled values (1, 1);
insert into enrolled values (3, 1);
insert into enrolled values (4, 1);
insert into enrolled values (9, 1);
insert into enrolled values (2, 2);
insert into enrolled values (4, 2);
insert into enrolled values (5, 2);
insert into enrolled values (8, 2);
insert into enrolled values (7, 2);
insert into enrolled values (9, 2);
insert into enrolled values (1, 3);
insert into enrolled values (2, 3);
insert into enrolled values (3, 3);
insert into enrolled values (4, 3);
insert into enrolled values (5, 3);
insert into enrolled values (6, 3);
insert into enrolled values (7, 3);
insert into enrolled values (8, 3);
insert into enrolled values (9, 3);
insert into enrolled values (10, 3);


insert into claim values (DEFAULT, 1, 1, 2000, 'broken hand','covering 100% of the expenses', 0, '2021-08-28');
insert into claim values (DEFAULT, 1, 1, 500 , 'fever','covering 100% of the expenses', null, '2021-04-19');
insert into claim values (DEFAULT, 1, 2, 200 , 'flu','covering 100% of the expenses', 1, '2021-11-10');
insert into claim values (DEFAULT, 2, 3, 300 , 'gastroenteritis','covering 100% of the expenses', 0, '2021-07-04');
insert into claim values (DEFAULT, 2, 1, 290 , 'asthma','covering 100% of the expenses', null, '2021-08-25');
insert into claim values (DEFAULT, 3, 3, 4000, 'broken leg','covering 100% of the expenses', 0, '2021-01-04');
insert into claim values (DEFAULT, 4, 3, 500 , 'fever','covering 100% of the expenses', null, '2021-10-04');
insert into claim values (DEFAULT, 4, 2, 480 , 'chest pain','covering 100% of the expenses', null, '2021-03-14');
insert into claim values (DEFAULT, 6, 3, 780 , 'flu','covering 100% of the expenses', null, '2021-10-15');
insert into claim values (DEFAULT, 6, 3, 2300, 'broken leg','covering 100% of the expenses', 0, '2021-01-10');
insert into claim values (DEFAULT, 10, 2, 2000, 'asthma','covering 100% of the expenses',0, '2021-08-21');
insert into claim values (DEFAULT, 5, 1, 700 , 'cold','covering 100% of the expenses', 1, '2021-04-06');
insert into claim values (DEFAULT, 7, 3, 2000, 'chest pain','covering 100% of the expenses', 0, '2021-04-03');
insert into claim values (DEFAULT, 8, 1, 250 , 'fever','covering 100% of the expenses', 0, '2021-09-07');
insert into claim values (DEFAULT, 6, 3, 780 , 'flu','covering 100% of the expenses', 0, '2021-04-11');
































