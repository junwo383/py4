#재미삼아 만들어본 if문  elif문 으로 자율주행자동차 시스템 가동안내  # 복슴할겸 만들어봤어요
# name : jun
import datetime #import 문 사용

now = datetime.datetime.now() #변수

print("======자율주행자동차 가동안내======") #print문
name = input("당신의영어이름을 입력해주세요. 나중에사용내역 시스템에 저장하겠습니다.")
print(name)
question_car = input("자율주행자동차 시스템 가동하실려면\nButton:1.네 2.아니오 터치해주세요>") #input문사용
if question_car <"1.네" : #if문사용
    print("사용하겠습니다.") 
elif question_car <"2.아니오" :
    print("사용안하겠습니다.")
else :
    print("운전자님! 버튼을 잘못눌르셨습니다!,다시한번버튼을 눌려주시기바랍니다.")

print("{}년 {}월 {}일 {}시 {}분 {}초".format( #시간함수이용
    now.year,

    now.month,

    now.day,

    now.hour,

    now.minute,

    now.second
))
