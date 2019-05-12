# 00






# 204120222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222# items函数返还键与键值
# student = {'王尼玛':'1001','王你把':'1004'}
# print('调用后items函数的结果为: %s'%student.items())
#


# ----------------------------------小潘专属分割线
# keys函数返还键但不返还键值
# student = {'王尼玛':'1001','王你把':'1004'}
# print('测试的样子: %s'%student.keys())

# setdefault
# student = {'王尼玛':'1001','王你把':'1004'}
# print('查找库日天:%s:'%student.setdefault('库日天'))
# print('王尼玛:%s' %student.setdefault('王尼玛'))
# print(student)
# ----------------------------------小潘专属分割线
# updata函数
# student = {'王尼玛':'1001','王你把':'1004'}
# student2 = {'吊炸天':'1003'}#不能直接的添加在字符格式化中需要单独赋值，当含有相同值的时候将会被覆盖。
# student.update(student2)
# print('新的字典:%s ' %student.update(student2))
# 新的字典:None
# print('新的字典:%s ' % student)

# ----------------------------------小潘专属分割线

# student = ['xiaoqiang','xiaoming','xiaofang']
# number = [1001,1002,1003,1004]
# for name,num in zip(student,number):
#     # print(f'{name}的学号是:{num}')
#     print(f'{name}{num}')
#

# import random
#
# number = random.randint(1,100)
# # print(number)
# guess = 0
# while True:
#     num_input = input("请输入一个0到100的数字:")
#     guess +=1
#     if not num_input.isdigit():33
#         print('请输入数字')
#     elif int(num_input)<0 or int(num_input)>=100:
#         print('输入的数字必须在0到100之间')
#     else:
#         if number==int(num_input):
#             print(f"恭喜你回答正确,共计{guess}次")#注意此处括号内需加上f
#             break
#         elif number>int(num_input):
#             print("您输入的太小了")
#         elif number<int(num_input):
#             print("您输入的太大了")
#         else:
#             print("别玩了，你妈喊你回家吃饭了")

# def meide():
#     print("草泥马哦")#函数功能自定义，注意不要与已有内在函数想重合，当然此处功能不限制与只能有一个可以是多个。
# meide()#此处为函数调用

# ----------------------------------小潘专属分割线

           # --------       必须参数------
# def testone(str_1,str_2):#括号内输入的所需的参数，参数名随意，参数个数随意中间加括号隔开即可
#     print(f'这句话是：{str_1}')
#     print(f'这是一个传入参数，讲的是：{str_2}')
# testone('我他妈看不懂','吃屎去吧')#这里传入必须参数请注意需要与定义时的参数个数相同
           # --------       关键字参数------
# def test2(age,name):
#     print(f'年龄：{age}')
#     print(f'姓名:{name}')
#     return
# test2(name='草泥马',age=22)
# 只要指定参数名参数传入的顺序就不会改变
                      # --------       默认参数------
# def test3(name,age=22,address='北京'):#默认第二个人参数值为22，若最后不给第二个参数赋值则调用默认值
#     print(f'我叫：{name}')
#     print(f'我今年{age}岁')
#     print(f'我来自：{address}')
# test3('小明',age=25,address='上海')
#     #请注意在此默认参数情况下默认参数所在的代码必须在非默认函数的后面！ 针对函数调用的时候其余的时候没有太大影响
# # 代码如下：
# # SyntaxError: positional argument follows keyword argument
# # 若该项目代码中传入的有两个默认代码那么在利用参数名改变其中参数的值时，另一个默认参数的改变必须加上参数名再更改否则报错
# #  SyntaxError: positional argument follows keyword argument

# def test4(str_1,*str_2):#第一个是必须参数，第二个是可变参数他是一个元组，当我们王第二个可变参数添加参数时，不受数量的限制，可以不传入参数他传递回去的永远是以一个元组的形式。
#     print(str_1)
#     for test in str_2:
#         print(f'我属于不定长参数部分：{test}')
#     return
# test4('小梦','库日天',123,'吊炸天','shanghai')

#
# other = {'城市':'北京','爱好':'编程'}
# def test5(name,number,**kw):
#     print(f'名称：{name}，学号:{number},其他:{kw}')
# test5('草泥马',1110,城市=other['城市'],爱好=other['爱好'])#从other函数所生成的列表中调取参数，然后赋值给可变参数的kw，kw的改变并不会影响原有other的值

# def test6(p1,p2,df=2,*vart,**kw):
#     print(f'p1={p1},p2={p2},df={df},vart={vart},kw={kw}')#注意此处kw是字典形式当传入参数时应以字典去赋值
# test6(1,2,3,'abc','爱你',王尼玛='傻逼')#此处注意字典的形式一开始是以等号的形式输入的
#
# def test7(x,y):
#     # x=10
#     # y=20
#     z=x+y
#     print(f'函数值为: ,{z}')
# test7(10,20)
# def test8():
#     x=10
#     y=20
#     z=x+y
#     # return z#注意此处如不给出return函数作为返回值输出那么最后结果便会是以下结果。
# # 函数值：None
# print(f'函数值：{test8()}')
