# file 생성하기
# score_file = open("new_file.txt", 'w', encoding = "utf8")

# for i in range (1,11):
#     data = "%d 번 째 줄입니다. \n" % i
#     score_file.write(data)

# score_file.close()


# readline

# f = open("new_file.txt","r",encoding="utf8")
# line = f.readline()
# print(line)
# f.close()

# for

# f = open("new_file.txt","r",encoding="utf8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# # add data

# f = open("new_file.txt","a",encoding="utf8")
# for i in range(11, 20):
#     data = "%d 번 째 줄입니다." %i
#     f.write(data)
# f.close()

# f = open("new_file.txt", "r", encoding="utf8")
# data = f.read()
# print(data)
# f.close()

# with open("new.txt", "w") as f:
#     f.write("Life is too short, you should learn python")

# with open("new.txt", "r") as f:
#     a = f.read()
#     print(a)

# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result / len(args)

# a = avg_numbers(1,2)
# print(a)
# b = avg_numbers(1,2,3,4,5)
# print(b)

   
f1 = open("test.txt", "r", encoding = "utf8")
body = f1.read()
f1.close()

body = body.replace("python", "java")

f1 = open("test.txt", "w", encoding="utf8")
a = f1.write(body)
f1.close()

