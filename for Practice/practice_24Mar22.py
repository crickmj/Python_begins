from re import L


scores = {"수학":0, "영어":50, "코딩":100}
for subject in scores.items():
    print(subject.ljust,scores)
    
