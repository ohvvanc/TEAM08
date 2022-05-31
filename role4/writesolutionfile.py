import pandas as pd
from role2.solution import findsolution

def writesolutionfile(sol):
    f = open("team08_groupwork\output\result.csv", 'w', encoding='utf8')   #결과값을 덮어쓰기 위해 파일을 엶
    sol.to_csv("team08_groupwork\output\result.csv", mode='a')       #결과가 담긴 Series도 파일에 추가
    f.close()

