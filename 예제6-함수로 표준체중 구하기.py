# 표준체중을 구하는 프로그램을 작성하시오.
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
# 조건1. 표준 체중은 별도의 함수 내에서 계산 
#      * 함수명 : std_weight
#      * 전달값 : 키(height), 성별(gender)
# 조건2. 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height,gender):
    if gender == '남자':
        return height*height*22
       
    elif gender == '여자':
        return height*height*21
        
        
height = float(input('키 : '))
gender = str(input('성별 : '))
weight = std_weight(height,gender)  
if weight == None:
    print('사람이 아닙니다!!!')
else:
    print('키 {0}m {1}의 표준체중은 {2}KG 입니다.'.format(height,gender,weight))
