# print "hello world"
# name = "zen"
# print "my name is", name
# first_name = "Zen"
# last_name = "coder"
# print "My name is {}{}".format(first_name, last_name)


# hw = "hello %s" % 'world'
# print hw
# the output would be:
# hello world
# x = "hello world"
# print x.capitalize()
# output:
# ninjas = ['jon', 'gus', 'jane']
# my_list = ['4', ['list', 'in', 'a', 'new'], 987]
# empty_list = []

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cuecumber', 'carrots']

# fruits_and_vegetables = fruits + vegetables
# print fruits_and_vegetables
# salad = 3 * vegetables
# print salad

# drawer = ['documents', 'envelopes', 'pens']
# print drawer[0]
# print drawer[1]
# print drawer[2]

# drawer.append(100)
# print drawer

# x = [99,4,2,5,-3];
# print x[:3]

# my_list = [1, 'zen', 'hi']
# print len(my_list)

# age = 17
# if age >= 18:
    # print 'legal age'
# elif age == 17:
    # print 'gang gang 17'
# else:
    # print 'foh young bitch'

# for count in range(0, 5):
    # print "looping -", count

# my_list = [4, 'dog', 99, ['list','inside','another'], 'hello world!']
# for element in my_list:
    # print element

# count = 0
# while count < 5:
    # print 'looping -', count
    # count += 1

# x = 3
# y = x
# while y > 0:
    # print y
    # y = y - 1
    # if y == 0:
        # break
# else:
    # print "final else statement"

# x =[2,54,-2,7,12,98]
# print x
# print min(x)
# print max(x)


# str = "its thanksgiving day.its my birthday,too!"
# print str
# print str.find("day")
# str = str.replace("day", "month")
# print str
#
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0], x[len(x) - 1]

# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# print x
# x.sort()
# print x
# first_list = x[0:len(x)/2]
# second_list = x[len(x)/2:len(x)]
# print "first list", first_list
# print "second list", second_list
# second_list.insert(0,first_list)
# print second_list

# for count in range (1, 100, 15):
    # print count

# a = [1, 2, 5, 10, 255, 3]
# sum = 0
# for i in a:
    # sum += i
print sum
#
# print sum/len(a)

# need to change from javascript to python
# s = 8

# board = ""

# for count in range (1, 8):
    # for x = 0 x < s x+
    #   ifx + y % 2 === 0
        # board += " "
    #   else
        # board += "#"

    # board += "\n"
# print board
# javascript to python


# def add(a,b):
    # x = a + b
    # return x

# result = add(3,5)
# print result

# def multiply(arr,num):
    # print arr, num
    # for x in arr:
        # print x
        # x *= num
    # return arr

# a = [2,4,10,16]
# b = multiply(a,5)
# print b


# def multiply(arr,num):
    # print arr, num # output should be [2,4,10,16] 5
    # for x in arr:
        # print x
        # x *= num
        # print x
    # return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b


# def multiply(arr,num):
    # for x in range(len(arr)):
        # arr[x] *= num
    # return arr
# a = [2,4,10,16]
# b = multiply(a,5)
# print b

# dog = ("canis familiaris", "dog", "carnivore", 12)
# print dog[2]
# for data in dog:
    # print data
    # dog[0] = "x"
# dog = dog + ("domestic",)
# print dog

# value = ("michael", "instructor", "coding dojo")
# (name, position, company) = value
# print name
# print position
# print company
#
# print len(value)
# print max(value)
# print min(value)
# print sum(value)
# print any(value)
# print all(value)
# for index,item in enumerate(value):
    # print(str(index)+ "="+str(item))

# print sorted(value)
# print tuple(reversed(value))

# def get_circle_area(r):
    # c = 2 * math.pi * r
    # a = math.pi * r * r
    # return (c, a)
    #

weekend = {"sun": "sunday", "mon": "monday"}
capitals = {}
capitals["svk"] = "bratislava"
capitals["deu"] = "berlin"
capitals["dnk"] = "copenhagen"
print weekend["sun"]
print capitals["svk"]

# for data in capitals:
    # print data

# for key in capitals.iterkeys():
    # print key

for val in capitals.itervalues():
    print val

for key,data in capitals.iteritems():
    print key, "=", data

context = {
    'questions': [
        {'id': 1, 'content': 'why is there a light in the fridge and not in the freezer?'},
        {'id': 2, 'content': 'why don\'t sheep shrink when it rains?'},
        {'id': 3, 'content': 'why are they called apartments when they are all stuck together?'},
        {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}

for key, data in context.items():
    for value in data:
        print "question #", value["id"], ":", value["content"]
        print "----"

data ={"house":"haus","cat":"katze","red":"rot"}
print data.items()
print data.keys()
print data.values()
