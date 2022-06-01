from role1.dataframe import makedataframe

def except1(a):
    while True:                                                                                                         #양의 int가 입력될 때까지 반복
        try:                                                                                                            #양의 int가 나오지 않는 경우를 대비함
            b = int(a)                                                                                                  #int가 입력되었을 때
            if b > 0:                                                                                                   #입력된 숫자가 양의 정수일 때
                c = makedataframe(b)                                                                                    #데이터 생성
                return c                                                                                                #생성한 데이터값 반환
                break                                                                                                   #while문에서 빠져나옴
            else:                                                                                                       #int이지만 음수가 입력됐을 경우
                a = input("양의 정수를 입력하시오\n데이터의 크기를 다시 입력하시오: ")                                               #입력값을 다시 받음
                continue                                                                                                #처음으로 다시 돌아감
        except ValueError:                                                                                              #int가 입력되지 않았을 경우
            try:                                                                                                        #float가 입력됐을 경우
                d = float(a)                                                                                            #float가 입력됐을 경우에는 정상적으로 넘어가지만, 문자열의 경우 ValueError발생
                a = input("정수를 입력하시오\n데이터의 크기를 다시 입력하시오: ")                                                   #입력값을 다시 받음
                continue                                                                                                #처음으로 돌아감
            except ValueError:                                                                                          #문자열이 입력됐을 경우
                a = input("숫자를 입력하시오\n데이터의 크기를 다시 입력하시오: ")                                                   #입력값을 다시 받음
                continue                                                                                                #처음으로 돌아감
