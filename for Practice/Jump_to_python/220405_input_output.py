# file 생성하기
f1 = open("new_file.t", 'w', encoding = "utf8")
for i in range (1,11):
    data = "%d 번 째 줄입니다. \n" % i
    f1.write(data)
f1.close()

