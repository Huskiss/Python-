gun = 10 

def checkpoint(soldiers): #경계근무
    gun = 20 #지역변수 : 함수내 gun이라는 변수
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))

print("전체총 : {0}".format(gun))
checkpoint(2) #2명이 경계근무나감
print('남은 총 : {0}'.format(gun))

gun = 10 

# def checkpoint(soldiers): #경계근무
#     global gun #전역변수 : 전역 공간에 있는 gun을 사용 
#     gun = gun - soldiers
#     print('[함수 내] 남은 총 : {0}'.format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}'.format(gun))
    return gun

print("전체총 : {0}".format(gun))
# checkpoint(2) #2명이 경계근무나감
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}'.format(gun))