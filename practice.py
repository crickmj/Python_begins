
cabinet = {"a-3":"유재석", "b-100":"김태호"}

print(cabinet["a-3"])

print(cabinet)

cabinet["c-20"] = "조세호" 
print(cabinet)

cabinet["a-3"] = "종국이"
print(cabinet)

# 간 손님

del cabinet["a-3"]
print(cabinet)

# key 들만 출력

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)
