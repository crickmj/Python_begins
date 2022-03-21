# 리스트 [] 순서를 가지는 객체의 집합 

# 지하철 칸 별로 10, 20, 30명

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호 씨가 몇 번째 칸에 타고 있는가?

print(subway.index("조세호"))

# 하하 씨가 탔어요 다음 정류장 다음 칸에

subway.append("하하")
print(subway)

# 사람들 사이에 넣어보쟈, append는 항상 뒤에! 정형돈을 유재석과 조세호 사이에

subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람들을 한 명씩 뒤에서 꺼냄

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인하기

subway.append("유재석")
print(subway)

subway.count("유재석")
print(subway.count("유재석"))

# 정렬도 가능

num_list = [5,2,4,3,1]

num_list.sort()
print(num_list)