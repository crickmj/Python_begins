#def profile(name, age, main_lang):
 #   print("이름은: {0}\t나이: {1}\t주 사용 언어: {2}"\
 #       .format(name,age,main_lang))
    
#profile("유재석", 20, "python")
#profile("김태호", 21, "java") 

# 같은 학교, 같은 학년, 같은 반 수업 -> 기본값 설정

def profile(name, age=17, main_lang="python"):
    print("이름은: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name,age,main_lang))
    
profile("유재석")
profile("김태호")


# 키워드 값을 이용한 함수 호출 --> 순서에 관계없이 def  이후로 설정! 

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="python", age=20)
profile(name="김태호", age=25, main_lang="java")

# 가변인자 이용한 함수 

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age), end=" ") # end = " " 는 출력 후 terminal 상 줄바꿈 하지 않고 유지 
#     print(lang1,lang2,lang3,lang4,lang5)
    
# profile("유재석", 20, "python", "java","c","c++","c#")
# profile("김태호", 23, "Kotlin", "Swift", " "," ", " ")
    
def profile(name, age, *language): # *을 넣어서 가변인자 형성
    print("이름: {0}\t나이: {1}\t".format(name,age), end=" ") # end = " " 는 출력 후 terminal 상 줄바꿈 하지 않고 유지 
    for lang in language:
       print(lang, end=" ")
    print()
    
 
profile("유재석", 20, "python", "java","c","c++","c#","java script")
profile("김태호", 23, "Kotlin", "Swift")
    
## global 변수 설정

gun = 10

def checkpoint(soldiers): #경계근무
    global gun 
    gun = gun - soldiers 
    print("[함수 내] 남은 총: {0}".format(gun))
    
def checkpoint_ret(gun, soldiers): 
    gun = gun - soldiers 
    print("[함수 내] 남은 총: {0}".format(gun)) 
    return(gun)

print("전체 총: {0}".format(gun)) 

## checkpoint에 2명 경계근무

gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))