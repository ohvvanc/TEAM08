from role1.dataframe import makedataframe

def except1(a):
    while True:
        try:
            b = int(a)
            if b > 0:
                c = makedataframe(b)
                return c
                break
            else:
                print('양의 정수를 입력하세요')
        except ValueError:
            print('숫자를 입력하세요')
            a = input("데이터의 크기를 입력하시오: ")
            continue
