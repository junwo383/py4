print("자동차 시속계산기")
a = int (input("자동차계기판\n첫번쨰값입력해주세요. :"))
d = int (input("자동차계기판\n두번쨰값입력해주세요. :"))
mean = input("1.plu 2.sub 3.mu1 4.div 사용하실 영어 입력 해주세요 :")
if mean == "plu":
    print(a+d)
elif mean == "sub":
    print(a-d)
if mean == "mu1":
    print(a*d)
elif mean == "div":
    print(a/d)

print("자동차 시속 계산기 이용해주셔서 감사합니다")