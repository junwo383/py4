def sort (n1, n2) :
    if n1> n2 :
        return n1, n2
    else :
        return n2, n1

n1 = eval(input("수를 입력하세요 : "))

r1, r2 = sort(n1)
print(r1, '이', r2 , '보다 더 큽니다')