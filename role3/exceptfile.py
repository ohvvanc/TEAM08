from role1.dataframe import makedataframe

def except1(a):
    while True:
        try:
            b = int(a)                                                                                                  #정수가 입력되었을 때
            if b > 0:                                                                                                   #입력된 숫자가 양의 정수일 때
                c = makedataframe(b)
                return c
                break
            else:
                print('양의 정수를 입력하시요')
                a = input("데이터의 크기를 다시 입력하시오: ")
                continue
        except ValueError:
            try:
                d = float(a)
                print('정수를 입력하시오')
                a = input("데이터의 크기를 다시 입력하시오: ")
                continue
            except ValueError:
                print('숫자를 입력하시요')
                a = input("데이터의 크기를 다시 입력하시오: ")
                continue
