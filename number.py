#파이썬 기초코딩 
# 계산기를 만들어보세요 
# 조건 : 조건문 전함수를 이용해서 만들어보세요 규칙!

text = "계산기를 만들어봅시다!" # 변수를 사용했습니다
text1 = "정수,소수계산을 모두다 완료하셨습니다.\n수고하셧습니다."
print(text) #print 문사용했습니다.
input("계산기실행하실려면 아무키나 눌르세요>") #input 문사용했습니다.
num1 = int(input("계산하실값을 입력해주세요>"))
num2 = int(input("계산하실값을 입력해주세요>")) # int문 사용했습니다.
num3 = float(input("소수계산기입니다\n계산하실값을 입력해주세요>")) #float 문사용했습니다.
num4 = float(input("소수계산기입니다\n계산하실값을 입력해주세요>")) #입력을안하면 값이안나옵니다. 실행보여드렸습니다.!
print("덧셈값:{}  ".format(num1+num2)) #포멧과 연산자 응용을이용해서 사용했습니다.
print("뺄셈값:{}".format(num1-num2))
print("나눗셈값:{}".format(num1/num2))
print("반올림값:",round(num1,num2)) #round 반올림 함수 이용
print("곱셉값:{}".format(num1*num2))
print("제곱값:",pow(num1,num2)) # 제곱근 pow 값 활용
print("소수값입니다.")
print("소수값:{}".format(num3))
print("뺄셈값:{}".format(num1-num2))
print("덧셈값:{}".format(num1+num2))
print("나눗셈값:{}".format(num1/num2))
print("나눗셈나머지값:{}".format(num1%num2))
print("곲셉:{}".format(num1*num2))
print("제곱값:",pow(num3,num4))
print(text1)


#댓글로 모르는거있으면 남겨주세요! 이상 마치겠습니다 미리해놨어요!