#사이트별로 비밀번호를 만들어 주는 프로그램 만들어보기
# 예) http://naver.com
#규칙1 : http: //부분은 제외
#규칙2 : 처음 만나는 점(.) 이후 모든 부분은 제외 
#규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + '!'로 구성
#예) 생성된 비밀번호 : nav51!

site = 'http://google.com'
# site = 'http://naver.com'
# rule1 = site[7:]
# rule2 = rule1[:-4]
# password = rule2[:3]+str(len(rule2))+str(rule2.count('e'))+'!'
# print(rule1)
# print(rule2)
# print(password)

#다른 방법-강사풀이
rule1 = site.replace('http://','')
rule2 = rule1[:rule1.find('.')]
password = rule2[:3]+str(len(rule2))+str(rule2.count('e'))+'!'
print('{0}의 비밀번호는 {1}입니다 '.format(site,password))