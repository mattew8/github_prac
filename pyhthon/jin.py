#자료형

#변수 네이밍시 주의사항 1)의미o 2)이해o 3)있을법한 것X

# a = 1 #나쁨

# py_study = "jin" #좋음

# #숫자

# b = 1
# c = 200

# print("나눗셈 : ", b/c)

# #타임체크
# print(type(b//c)) # 정수는 인트/소수는 플로트

#문자 (대부분 + * 연산자 까지만)
# d = "안녕하세요"
# e = "안녕"
# print(e)
# print(d)
# print(e*50)
# print(d+e)

#리스트 - 순서가 있는 수납장
# mylist = []
# mylist2 = list()

# mylist.append(2)
# mylist2.append("첫째")
# mylist.append(mylist2)

# print(mylist)
# print(mylist2)

# print("팝:",mylist.pop())

# #리스트는 많은 메서드 - 필요할때 찾아 쓰기

# mylist3 = [1,2,3,4,5,6]
# #index는 [0,1,2,3,4,5]

# print("인덱스", mylist3[2])
# print("슬라이싱", mylist3[2:5])
# print("슬라이싱", mylist3[:4])
#파이썬 범위지정 - a=<b<c

#dictionary 사전 자료형 

# mydict = dict()
# mydict2 = {}
# #dic에 값 입력
# mydict["치훈"] = "스터디장"
# mydict["진호"] = "스터디원"
# #dic에 있는 자료 찾기
# print(mydict)
# print(mydict["진호"])

# mydict["리스트"] = [1,2,3]
# print(mydict)
# mydict["오"] = 5
# mydict["십"] = 10
# print(mydict["오"])*mydict["십"])
# #list/dic 차이
# #순서o/순서x
# #속도는 dic이 빠름

