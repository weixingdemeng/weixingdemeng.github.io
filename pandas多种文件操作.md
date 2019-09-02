# pandas多种文件操作


	"""
	JSON数据
	pandas.read_json可以自自动将特别格式的JSON数据集转换为Series或DataFrame
	"""
	import pandas as pd
	import numpy as np
	data = pd.read_json('database.json')
	# print(type(data))
	# 从pandas输出到json
	# print(data.to_json())
	"""
	XML和HTML
	pandas的一个内置的功能：read_html,它可以使用lxml和Beautiful Soup自动将HTML
	文件中的表格解析为DateFrame对象
	"""
	"""
	安装相关库：
	conda install lxml
	pip install beautifulsoup4 html5lib
	"""
	# 读取html中的表格
	tables = pd.read_html('test.html')
	
	# 查看html中有多少个表格
	table_length = len(tables)
	# 查看第一个表格的前五行数据
	tables[0].head()
	
	"""
	pandas处理二进制数据
	"""
	# 将数据以二进制的形式存储到指定位置
	data.to_pickle('pickle')
	# 将二进制数据读出来
	pd.read_pickle('pickle')
	new_data = pd.read_pickle('pickle')
	"""
	HDF(层次型数据格式)5格式
	HDF5是一种存储大规模科学数组数据的非常好的文件格式。,HDF5支持多种压缩器的即时压缩,
	还能更高效地存储重复模式数据。对于那些非常大的无法直接放入内存的数据集。HDF5就是
	不错的选择,因为它可以高效地分块读写。
	"""
	frame = pd.DataFrame({'a': np.random.randn(100)})
	print(frame)
	store = pd.HDFStore('mydata.h5')
	store['obj1'] = frame
	store['obj1_col'] = frame['a']
	print(store)
	# HDF5文件中的对象可以通过与字典一样的API进行获取
	obj1 = store['obj1']
	print(obj1)
	# HDFStore支持两种存储模式,’fixed’和’table’。后者通常会更慢,但是支持使用特殊语法
	# 进行查询操作
	store.put('obj2', frame, format='table')
	store.select('obj2', where=['index >= 10 and index <= 15'])
	store.close()
	# pandas.read_hdf函数可以快捷使用这些工具
	frame.to_hdf('mydata.h5', 'obj3', format='table')
	pd.read_hdf('mydata.h5', 'obj3', where=['index < 5'])
	"""
	读取Microsoft Excel文文件
	pandas的ExcelFile类或pandas.read_excel函数支持读取存储在Excel 2003(或更高版本)中
	的表格型数据。这两个工具分别使用扩展包xlrd和openpyxl读取XLS和XLSX文件。你可以用
	pip或conda安装它们
	"""
	# 方式１
	xlsx = pd.ExcelFile('ex1.xlsx')
	pd.read_excel(xlsx, 'Sheet1')
	# 方式2
	frame = pd.read_excel('ex1.xlsx', 'Sheet1')
	# 将pandas数据写入为Excel格式
	# 方式１
	writer = pd.ExcelWriter('ex2.xlsx')
	writer.save()
	# 方式２
	frame.to_excel('ex2.xlsx')
	"""
	Web APIs交互
	"""
	import requests
	url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
	response = requests.get(url)
	print(response)
	data = response.json()
	issues = pd.DataFrame(data, columns=['number', 'title','labels', 'state'])
	print(issues)
	
	"""
	pandas与数据库交互（todo）
	"""
	import sqlalchemy as sqla
	db= sqla.create_engine('mysql+pymysql://root:123456@127.0.0.1/taobao?charset=utf8')
	pd.read_sql('select * from product', db)