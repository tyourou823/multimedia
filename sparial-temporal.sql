DROP TABLE IF EXISTS hot_spring;
CREATE TABLE hot_spring
(
  id text,
  name text,
  pt point
);

INSERT INTO hot_spring(id, name, pt) VALUES ('1','FUJINOYU','(10,40)');
INSERT INTO hot_spring(id, name, pt) VALUES ('2','IZUONSEN','(8,38)');
INSERT INTO hot_spring(id, name, pt) VALUES ('3','BESSHOONSEN','(5,10)');
INSERT INTO hot_spring(id, name, pt) VALUES ('4','INAGONOYU','(6,11)');
INSERT INTO hot_spring(id, name, pt) VALUES ('5','KUSATSU','(4,7)');
INSERT INTO hot_spring(id, name, pt) VALUES ('6','NARUKO','(50,78)');	

DROP TABLE IF EXISTS place;
CREATE TABLE place
(
  id text,
  name text,
  area circle
);

INSERT INTO place (id, name, area) VALUES ('1', 'HAKONE',circle(point '(11,42)', 3.0));
INSERT INTO place (id, name, area) VALUES ('2', 'IZU',circle(point '(9,37)', 2.0));
INSERT INTO place (id, name, area) VALUES ('3', 'UEDA',circle(point '(6,12)', 3.0));
INSERT INTO place (id, name, area) VALUES ('4', 'GUNMA',circle(point '(2,6)', 4.0));
INSERT INTO place (id, name, area) VALUES ('5', 'MIYAGI',circle(point '(52,77)', 3.0));

DROP TABLE IF EXISTS kb_user;
CREATE TABLE kb_user
(
  id text,
  name text,
  pt point
);

INSERT INTO kb_user (id, name, pt) VALUES ('1','KIYOKI','(9,10)');
INSERT INTO kb_user (id, name, pt) VALUES ('2','TAKANO','(50,70)');

DROP TABLE IF EXISTS book;
CREATE TABLE book
(
  id text,
  title text,
  create_date timestamptz
);

INSERT INTO book (id, title, create_date) VALUES ('1', 'LISP', '2012/10/19 21:10:30');
INSERT INTO book (id, title, create_date) VALUES ('2','DATABASE','2012/09/01 10:15:21');
INSERT INTO book (id, title, create_date) VALUES ('3','MULTIMEDIA','2013/03/14 15:45:55');
INSERT INTO book (id, title, create_date) VALUES ('4','JAVA','2012/10/20 10:00:12');
INSERT INTO book (id, title, create_date) VALUES ('5','COMPUTING,THEORY','2012/10/15 12:00:35');
INSERT INTO book (id, title, create_date) VALUES ('6','SPACE,MODELING','2013/04/04 18:25:43');
INSERT INTO book (id, title, create_date) VALUES ('7','MOBILE','2012/10/10 10:45:55');
INSERT INTO book (id, title, create_date) VALUES ('8','SENSOR,NETWORK','2013/05/12 09:33:17');
INSERT INTO book (id, title, create_date) VALUES ('9','RFID','2013/01/13 21:05:27');
INSERT INTO book (id, title, create_date) VALUES ('10','WWW','2013/02/21 15:40:11');

