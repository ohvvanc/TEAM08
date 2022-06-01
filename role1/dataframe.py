import pandas as pd #데이터프레임생성 모듈
import numpy as np # 랜덤 정수 데이터값 생성 모듈
def makedataframe(n):
    col1 = [('작업'+str(i)) for i in range(1, n+1)] #열
    ind1 = [('기계'+chr(k)) for k in range(65, n+65)] #행, chr는 ascii 숫자값을 문자형으로 변환 A=65,B=66...
    return pd.DataFrame(np.random.randint(1, 11, size=(n, n)), index=ind1, columns=col1)
#  데이터프레임생성    데이터는1이상10이하정수,nxn사이즈, 행=ind1 , 열=col1