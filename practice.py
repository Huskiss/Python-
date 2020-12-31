temp = int(input('기온은 어때요?'))
if 30 <= temp:
    print('날씨가 너무 덥네유. 나가지마세유')
elif 10 <= temp & temp < 30:
    print('날씨가 좋아유!!, 나가노세요!!')
elif 0 <= temp < 10:
    print('조금 쌀쌀하니 따닷하게 하고 나가유!!')
else:
    print('추워 디지것는디 어딜나가유!!')