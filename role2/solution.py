import itertools #순열계산하는 툴

import pandas as pd


def findsolution(x): #x라는 데이터프레임의 솔루션을 구한다
    n = len(x) #x의 길이 (nxn크기일 때 n값 가져옴)
    result = list(itertools.permutations(list(range(n)),n))
    #0부터 n-1까지의 값들로 만들 수 있는 모든 순서쌍을 리스트에 저장 n=3일 경우 [(0, 1, 2),(0, 2, 1),(1, 0, 2),(1, 2, 0),(2, 0, 1),(2, 1, 0)]
    #즉 기계를 작업에 할당 할 수 있는 모든 가짓수를 저장 [(A-0/B-1/C-2) ,(A-0,B-2,C-1), ...]
    sum_list = [] #총 비용을 저장할 리스트 생성
    for k in result: #이제 위에 result에서 뽑아낸 가짓수에서 하나하나 비용을 계산한다
        #print(k)
        cost = [] #비용을 계산하기 위한 리스트 생성
        for i, t in enumerate(k): #k가 (0,1,2)일 경우 (i,t)는 인덱스와 값 (0,0),(1,1),(2,2) / (0,2,1)일 경우 (i,t)는 (0,0),(1,2),(2,1)
            #print(i,t)
            cost.append(x.iloc[i,t]) #cost에 비용을 하나하나 추가 11번째 줄 예시에서 cost=[데이터프레임에서(0,0),(1,1),(2,2)]
            #print(cost)
            if len(cost) == n: #리스트에 비용을 하나하나 추가하다가 n개의 작업을 하므로 리스트의 길이가 n개가 되면
                sum_cost = sum(cost) #비용의 합을 구하고
                sum_list.append(sum_cost) #비용의 합을 저장 n이3일 경우 6개의 합이 저장됨
    #print(sum_list)
    solution = min(sum_list) #이 저장된 비용의 합중에서 최소값이 솔루션임
    overlap = [i for i in range(len(result)) if sum_list[i] == solution]
    #최솟값을 가지는 해가 여러 개일 때, 그 값을 가지는 sum_list의 인덱스 저장
    # print(sum_list)
    # print(solution)
    # print(overlap)
    print(f'총 {len(overlap)}개의 해가 존재합니다.')
    overlap_list = [] #데이터 중 최솟값을 가지는 데이터의 인덱스를 저장할 리스트
    for i in overlap:
        #print(result[i])
        overlap_list.append(result[i])
    solindex = []  # 두 빈 리스트를 만들어 어떤 기계에 어떤 작업을 할당하였는지 표현하는 Series 데이터를 만들 것
    solvals = []
    for i in range(len(overlap)): #해의 개수만큼 dataframe을 생성
        for j in range(n):
            solindex.append('기계' + chr(j + 65))
            solvals.append('작업' + str(overlap_list[i][j] + 1))
        solvals.append(solution)
        solindex.append('비용')
        # print(solindex , solvals)
    return pd.Series(solvals, index=solindex)