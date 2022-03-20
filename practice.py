python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index+1)
print(index)

print(python.find("Java"))

print(python.count("n"))
