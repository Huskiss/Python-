# 주어진 코드를 활용하여 부동산 프로그램 만들기
#  출력예제
#  총 3대의 매물이 있습니다.
#  강남 아파트 매매 10억 2010년
#  마포 오피스텔 전세 5억 2007년
#  송파 빌라 월세 500/50 2000년

class House:
    def __init__(self,location,house,deal_type,price,complete_year):
        self.location = location
        self.house = house
        self.deal_type = deal_type
        self.price = price
        self.complete_year = complete_year
        print('{0}에 매물이 있습니다.'.format(self.location))

    def show_detail(self):
        print('  {0} {1} {2} {3} {4}'.format(self.location,self.house,self.deal_type,self.price,self.complete_year))

class 강남(House):
    def __init__(self):
        House.__init__(self,'강남','아파트','매매','10억','2010년')

class 마포(House):
    def __init__(self):
        House.__init__(self,'마포','오피스텔','전세','5억','2007년')

class 송파 (House):
    def __init__(self):
        House.__init__(self,'송파','빌라','월세','500/50','2000년')

houses = []
# house1 = House('강남','아파트','매매','10억','2010년')
# house2 = House('마포','오피스텔','전세','5억','2007년')
# house3 = House('송파','빌라','월세','500/50','2000년')
house1 = 강남()
house2 = 마포()
house3 = 송파()

houses.append(house1)
houses.append(house2)
houses.append(house3)

count = len(houses) # house라는 리스트안의 항목 갯수
print ('- 현재 남아있는 부동산 매물 -')
print ('  총 {}개의 매물이 있습니다.'.format(count))

for house in houses:
    house.show_detail()