import csv
import os

def writesolutionfile(dt, sol):
    path = os.getcwd() #csv파일을 저장할 경로를 불러오기 위해 os함수 사용
    f = open(path+"\\output\\result.csv", 'w', encoding='utf8')   #결과값을 덮어쓰기 위해 파일을 엶
    sol.to_csv(path+"\\output\\result.csv", mode='w' , header = False )       #solution을 csv파일에 저장
    f.close()

