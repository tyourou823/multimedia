drop table if exists colors;
create table colors(
	id int,
	name text,
	r int,
	g int,
	b int	
);

insert into colors(id,name,r,g,b) values(1,'red',191,30,51);
insert into colors(id,name,r,g,b) values(2,'yellow',250,212,58);
insert into colors(id,name,r,g,b) values(3,'yellow green',185,196,47);
insert into colors(id,name,r,g,b) values(4,'green',47,181,106);
insert into colors(id,name,r,g,b) values(5,'blue',0,103,192);
insert into colors(id,name,r,g,b) values(6,'purple',162,96,191);
insert into colors(id,name,r,g,b) values(7,'brown',115,78,49);
insert into colors(id,name,r,g,b) values(8,'pink',244,169,170);
insert into colors(id,name,r,g,b) values(9,'white',255,255,255);
insert into colors(id,name,r,g,b) values(10,'black',1,1,1);

drop table if exists landscape;
create table landscape(
	id int,
	name text,
	url text,
	red int,
	yellow int,
	yg int,
	green int,
	blue int,
	purple int,
	brown int,
	pink int,
	white int,
	bk int
);

create table result(
	name text,
	result int
);