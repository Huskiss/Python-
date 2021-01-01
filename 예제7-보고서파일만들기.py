# 매주 1회 보고서 만들기
# x 주차 주간보고서
# 부서 : 
# 이름 : 
# 업무 요약 :
# 1주차 부터 50주차 까지의 보고서를 만드는 프로그램 제작하기

for mon in range(1,51):
     with open('{0}주차.txt'.format(str(mon)),'w',encoding='utf8') as report_file:
         report_file.write('- {0}주차 주간보고서 -'.format(mon))
         report_file.write('\n  부서 : ')
         report_file.write('\n  이름 : ')
         report_file.write('\n  업무 요약 : ')