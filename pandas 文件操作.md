# pandas 文件操作

	import pandas as pd
	import numpy as np
	import sys
	# 读取csv文件
	# df = pd.read_csv('yob1880.txt')
	# 读取csv文件，需要加分割符号
	# df１ = pd.read_table('yob1880.txt', sep=',')
	# 定义列名
	pd.read_csv('yob1880.txt', header=None)
	names = ['第一列', '第二列', '第三列']
	df2 = pd.read_csv('yob1880.txt', names=names)
	# 将指定列设定为dataframe的索引列
	df3 = pd.read_csv('yob1880.txt', names=names, index_col='第三列')
	# 将多个列设置成层次化的索引
	df4 = pd.read_csv('yob1880.txt', names=names, index_col=['第一列','第三列'])
	# 处理不同分割符分割开的数据,sep中可以传入正则表达式进行匹配
	result = pd.read_table('yob1880.txt', sep='\s+')
	# 跳过指定的行进行筛选数据
	df5 = pd.read_csv('yob1880.txt', skiprows=[0, 2, 3])
	# 对缺失值进行处理
	df6 = pd.read_csv('yob1880.txt', na_values=['NULL'])
	# 使用字典的形式对不同列的缺失值进行不同的处理
	na_values = {'第一列': ['foo', 'NA'], '第二列': ['two']}
	df7 = pd.read_csv('yob1880.txt', na_values=na_values)
	# 读取文件指定行数
	df8 = pd.read_csv('yob1880.txt', nrows=5)
	# 逐块读取数据,可以对df9进行逐块进行处理
	df9 = pd.read_csv('yob1880.txt', chunksize=1000)
	# 将数据写入指定csv文件中,sep设定分割符
	df8.to_csv('out.csv', sep='|')
	# 写入的数据，如果有缺失值，则默认为空串，设定缺失值
	# df8.to_csv(sys.stdout, na_rep='NULL')
	# 禁用行和列的标签
	# df8.to_csv(sys.stdout, index=False, header=False)
	# 写出部分列，并按指定的顺序进行排序
	# df8.to_csv(sys.stdout, index=False, columns=['7065', 'F', 'Mary'])
	# 设置多个日期
	dates = pd.date_range('1/1/2000', periods=7)
	ts = pd.Series(np.arange(7), index=dates)
	ts.to_csv('date_time.csv')