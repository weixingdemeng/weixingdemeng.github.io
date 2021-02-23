# SQL基本指令
show databases;
create database if not exists mysql charset=utf8;
drop database if exists mysql;
use mysql;
create table my_table(column_name column_type);
	create table my_table (
	id int auto_increment,
	name varchar(30) not null,
	primary key('id')
	)engine=InnoDb default charset=utf8;
drop table my_table;
insert into my_table (file1, file2, file3) values (vaule1, vaule2, vaule3)
	insert into my_table ('name') values('qiqi');
select column_name1,column_name2 from table_name [where] [limit n] [offset m]
	select id,name from my_table where name='qiqi';
update my_table set field1=vaule1 field2=vaule2 [where]
	update my_table set name='xxx' where id=1;
delete from my_table [where]
	delete from my_table where name='xxx';
alter table my_table add primary KEy(primary_key_column);
***主键的数据类型为IN***
alter table my_table add[constraint 越苏名]　foreign key(外键字段名)　references table_name2(主键字段名)；
***使用外键的前提：１、存储引擎必须是innodb,否则创建的外键无约束效果。２、外键的列类型必须与父表的主键类型完全一致。３、外键的名字不能重复。４、已经存在数据的字段被设为外键时，必须保证字段中的数据父表的主键数据对应起来***
### on delete 和 on update都有restrict, no action, cascade, set Null属性
1、ON DELETE
restrict:当父表中删除对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除
no action:如果存在从数据，不允许删除主数据
cascade:当在父表中删除对应记录时，首先检查该记录是否有对应外键，如果有则也删除外键在字表中的记录。
set null:当在父表中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null
2、ON UPDATE
restrict:当父表中更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许更新
no action:当父表中更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许更新
cascade:当在父表中更新对应记录时，首先检查该记录是否有对应外键，如果有则也更新外键在字表中的记录。
set null:当在父表中更新对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null
### 重点：索引
什么是索引：MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。实际上，索引也是一张表，该表保存了主键与索引的字段，并指向实体表的记录。但过多的使用索引将会造成滥用。因此索引页会有它的缺点，虽然索引大大提高了查询速度，同时页减低了更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。
创建索引：create index [index_name] on table_name([column_nam]);
删除索引：drop index [index_name] on table_name;
查看索引：show index from table_name;
修改索引：alter table table_name add unique [index_name];
### 聚合函数
什么是聚合函数：对统计的结果进行二次筛选(分组，排序，算和，计算最大值，计算最小值，求平均值等)
group by:按指定字段记录分组，一般会和其他函数联合使用
order by:按制定字段排序，默认asc,可以指定多个排序字段，按字段先后分别排序。
sum()
avg()
count()
max()
min()
### 其他
between and
like
_:匹配一个字符
%：匹配多个字符
distinct
	select distinct num from my_table;
if(字段，exp1,exp2) 或者 ifnull(字段，exp1,exp2):如果字段值为真返回exp1,否则返回exp2
group by having:having语句通常与group by语句联合使用，用来过滤有group by语句返回的记录集，having语句的存在弥补了where不能与聚合函数联合使用的不足
a inner/left/right join b：a表为左表，b表为右表。
1、内关联：inner join on，仅对满足连接条件的列进关联，inner可以省略
2、左外连接：left outer join on ,其中Outer可以省略。输出左表中所有的数据，同时将符合条件的右表中搜索出来的结果合并到左表中，如果左表中存在右表中不存在，则结果集中会将查询的右表字段值设置为NULL。
3、右外连接：Right Outer Jion on 作用：其中outer可以省略，而RIGHT JOIN刚好相反，“A RIGHT JOIN B ON ……”是将符合ON条件的A表搜索结果合并到B表中，作为一个结果集输出：



