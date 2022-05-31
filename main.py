from role1.dataframe import makedataframe #makedataframe 이라는 함수를 가져옴
from role2.solution import findsolution #findsolution 이라는 함수를 가져옴
from role4.writesolutionfile import writesolutionfile
import os
if __name__ == '__main__': #패키지 파일에서 main 파일엔 이 문장이 반드시 있어야함 여러 모듈을 가져온후 이문장 밑에 실제 실행코드 입력
    dt = makedataframe(int(input("데이터 크기를 입력하시오: "))) #데이터크기를 입력받고 데이터프레임을 dt에 저장
    print("---------Dataframe-----------")
    print(dt)
    print("----------Solution-----------")
    print(findsolution(dt)) #findsolution 함수에 dt 입력
    if not os.path.isdir("output"): #output 이라는 폴더에 csv파일을 저장하기위해 폴더가 없을 경우 폴더 생성
        os.mkdir("output")
    writesolutionfile(dt, findsolution(dt))    #파일에 데이터데이블과 결과가 담긴 Series 데이터를 추가