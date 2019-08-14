---
title: Django运行机制
auth: seven
---
### 第一步: 请求 比如/hello/
### 第二步: Django查看ROOT_URLCONF设置，找到根URL配置
### 第三步: Django比较URL配置中的各个URL模式，找到与/hello/匹配的那个
### 第四步: 如果找到匹配的模式，调用对应的视图函数。
### 第五步:视图函数返回一个HttpResponse对象
### 第六步: Django把HttpResponse对象转换成正确的HTTP响应，得到网页。
# URL配置和松耦合
松耦合(解耦):是一种软件开发方式，价值在于让组件可以互换。
URL和视图函数之间很好的使用了松耦合，将URL和视图函数分别放在不同的两个地方，修改时相互之间不会影响或者影响很小。
# 动态URL
问题:如果导入的是path，怎么添加路由，可以达到动态的效果
# Django模板
Django模板是一些文本字符串，作用是把文档的表现和数据区分开。模板系统的设计目的是呈现表现、而不是程序逻辑。
{{ person_name }}是变量，把指定变量的值插入这里。
{% if ordered_warranty %}是模板标签，只要能让模板系统“做事”都是标签。
过滤器，|   {{ship_date|date:"F j, Y" }}
# 模板系统的使用
Django自带的一个模板：DTL
如果想在python代码中使用Django的模板系统，基本方式如下：1)以字符串形式提供原始的模板代码，创建Template对象。2)在Template对象上调用render()方法，传入一系列变量(上下文)。返回的是完全渲染模板后得到的字符串，模板的变量和模板标签已经根据上下文求出值了。
```
from django import template
>>> t = template.Template('My name is {{ name }}.')
>>> c = template.Context({'name': 'Nige'})
>>> print (t.render(c))
My name is Nige.
>>> c = template.Context({'name': 'Barry'})
>>> print (t.render(c))
My name is Barry.
```
### 1.创建Template对象
最简单的方式是实例化。
```
from django.template import Template 
t = Template('My name is {{ name }}.
```
在mysite项目目录中输入python manage.py shell 启动交互式解释器
### 2.渲染模板(render())
有了 Template 对象之后，可以为其提供上下文，把数据传给它。上下文就是一系列模板变量和相应的值。
在 Django 中，上下文使用 django.template 模块中的 Context 类表示
```
from django.template import Context, Template
>>> t = Template('My name is {{ name }}.')
>>> # 创建一个Context对象
>>> c = Context({'name': 'Stephane'})
>>> t.render(c)
'My name is Stephane.'
# 渲染多个
t = Template('Hello, {{ name }}')
for name in ('John', 'Julie', 'Pat'):
print (t.render(Context({'name': name})))
# 点号可以访问字典的键、
>> from django.template import Template, Context
>>> person = {'name': 'Sally', 'age': '43'}
>>> t = Template('{{ person.name }} is {{
person.age
}} years old.')
>>> c = Context({'person': person})
>>> t.render(c)
'Sally is 43 years old.'
# 点号还可以访问对象的属性。
> from django.template import Template, Context
>>> import datetime
>>> d = datetime.date(1993, 5, 2)
>>> d.year
1993
>>> d.month
5
>>> d.day
2
>>> t = Template('The month is {{ date.month }}
and the year is {{ date.year }}.')
>>> c = Context({'date': d})
>>> t.render(c)
'The month is 5 and the year is 1993.'
# 点号查找可以嵌套多层
from django.template import Template, Context
>>> person = {'name': 'Sally', 'age': '43'}
>>> t = Template('{{ person.name.upper }} is {{
person.age
}} years old.')
>>> c = Context({'person': person})
>>> t.render(c)
'SALLY is 43 years old.'

```
总结起来，模板系统遇到变量名中的点号时会按照下述顺序尝试：
1)字典查找（如 foo["bar"]）
2)属性查找（如 foo.bar）
3)方法调用（如 foo.bar())
4)列表索引查找（如 foo[2]）
5)点号查找可以嵌套多层
### 如何处理无效变量
一般来说，如果变量不存在，模板系统在变量处插入引擎的 string_if_invalid 配置选项。这个选项的默认值为一个空字符串
### 基本的模板标签和过滤器
标签：if/elif/else/endif  -- 支持and, or, not和取反，and优先级比or高
如果需要通过括号指明优先级，应该使用嵌套的 if 标签。不支持使用括号控制操作的顺序。如果觉得有必要使用括号，可以考虑在模板外部执行逻辑，然后通过专用的模板变量传入结果。或者，直接使用嵌套的 {% if %} 标签。
for 