##풀이
#추첨프로그램만들기
#추첨으로 1명치킨, 3명 커피
#댓글 20명, 아이디는 1~20이라고 가정
#댓글과 상관없이 무작위로 추첨하되 중복불가
#random모듈의 shuffle(리스트의 값을 무작위로 순서 바꿈)과 smaple()을 활용
from random import *
users = range(1,21) #1분터20까지 숫자 생성
# print(type(users)) # users가 range 타입임
users = list(users) # users를 list타입으로 바꾸어줌
shuffle(users)
print(users)

winners = sample(users,4)

print('-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('커피 당첨자 : {0}'.format(winners[1:]))
print('-- 축하합니다 --')

## 추가 확인 - type확인 및 ref에 users 배당하기
#from random import *
# users = range(1,21) #1분터20까지 숫자 생성
# # print(type(users)) # users가 range 타입임
# users = list(users) # users를 list타입으로 바꾸어줌
# shuffle(users)
# users = tuple(users) -> 튜플에서는 셔플이 안된다
# print(users)

# ref = range(1,21)
# ref = list(ref) # users를 list타입으로 바꾸어줌
# shuffle(ref)
# ref = tuple(ref)
# print(ref) 
# ref = users
# print(ref)