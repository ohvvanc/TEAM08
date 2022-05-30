from role1.dataframe import makedataframe #makedataframe 이라는 함수를 가져옴
from role2.solution import findsolution #findsolution 이라는 함수를 가져옴
if __name__ == '__main__': #패키지 파일에서 main 파일엔 이 문장이 반드시 있어야함 여러 모듈을 가져온후 이문장 밑에 실제 실행코드 입력
    dt = makedataframe(int(input("데이터 크기를 입력하시오: "))) #데이터크기를 입력받고 데이터프레임을 dt에 저장
    print(dt)
    print(findsolution(dt)) #findsolution 함수에 dt 입력