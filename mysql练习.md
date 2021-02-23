# mysql练习
- 1、查询所有学生信息
	select * from TbStudent;
- 2、查询所有课程名称及学分(投影和别名)
	select cosname as '课程名称', coscredit as '学分' from TbCourse;
- 3、查询所有女学生的姓名和出生日期(筛选)
	select cosname as '课程名称', coscredit as '学分' from TbCourse;
- 4、查询所有80后学生的姓名。性别和出生日期
	 select stuname, stusex, stubirth from TbStudent where stubirth between '1980-1-1' and '1980-12-31';
- 5、 查询姓王的学生姓名和性别
	select stuname, stusex from TbStudent where stuname like '王%';
- 6、查询性张名字总共两个子的学生的姓名
	select stuname from TbStudent where stuname like '张_';
