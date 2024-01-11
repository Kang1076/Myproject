# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 10:11:05 2024

@author: ham90
"""

import pandas as pd
from tqdm import tqdm
import warnings

'''
preprocessing1을 통해 얻은 훈련 데이터, 테스트 데이터를 좀 더 가공함
'''

warnings.filterwarnings('ignore') #warning 문구 제거
pd.set_option('display.max_columns', None)

path ='.'


traind = pd.read_csv(path + '/source/total관광지 추천시스템 Trainset_D.csv')
testd = pd.read_csv(path + '/source/total관광지 추천시스템 Testset_D.csv')

#%% 중복되는 여행ID, 관광지를 없앰
unique2 = testd[['TRAVEL_ID', 'VISIT_AREA_NM']].drop_duplicates()

temp2 = testd.iloc[unique2.index]

testd = temp2.reset_index(drop=True)
#testd.drop(['EUPMYEON'], axis=1, inplace=True)

unique3 = traind[['TRAVEL_ID', 'VISIT_AREA_NM']].drop_duplicates()

temp3 = traind.iloc[unique3.index]

traind = temp3.reset_index(drop=True)
#traind.drop(['EUPMYEON'], axis=1, inplace=True)

#%% 시/도이름 통일

places = list(traind['SIDO'])
for i in range(len(places)):
    if places[i][-1] == '도':
        if len(places[i])<=5:
            places[i] = places[i][:-1]
    elif places[i][-3:] == '광역시' or places[i][-3:] == '특별시':
        places[i] = places[i][:-3]
traind['SIDO'] = places

traind['SIDO'] = traind['SIDO'].replace('경상북', '경북')
traind['SIDO'] = traind['SIDO'].replace('전라남', '전남')
traind['SIDO'] = traind['SIDO'].replace('경상남', '경남')
traind['SIDO'] = traind['SIDO'].replace('충청남', '충남')
traind['SIDO'] = traind['SIDO'].replace('전라북', '전북')
traind['SIDO'] = traind['SIDO'].replace('충청북', '충북')

traind.drop(traind[traind['SIDO']=='광복동'].index, axis=0, inplace=True)
traind.drop(traind[traind['SIDO']=='동부리'].index, axis=0, inplace=True)
traind['SIDO'].unique()

testd['SIDO'] = testd['SIDO'].replace('충청남도', '충남')
testd['SIDO'] = testd['SIDO'].replace('서울특별시', '서울')
testd['SIDO'].unique()

#%% 최종 훈련데이터, 테스트데이터 csv파일로 저장

traind.to_csv(path + '/source/관광지 추천시스템 Trainset_final.csv', index = False)
testd.to_csv(path + '/source/관광지 추천시스템 Testset_final.csv', index = False)

y_testd = testd['DGSTFN']
X_testd = testd.drop(['DGSTFN'], axis = 1)


#%% 2회 이상 관광한 방문지 리스트 만들기
info = traind[['SIDO', 'VISIT_AREA_NM', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD', 'RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean',
'REVISIT_YN_mean', 'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']]
info.drop_duplicates(['VISIT_AREA_NM'], inplace = True)

visiting_list = traind[['VISIT_AREA_NM']] #train set에 있는 방문지에 대해서만 2회 이상 방문하였는지 확인
visiting_list.reset_index(drop = True, inplace = True)

dfdf = pd.DataFrame(visiting_list.value_counts(), columns = ['count'])
dfdf['VISIT_AREA_NM'] = dfdf.index
dfdf.reset_index(drop = True, inplace = True)

for i in range(len(dfdf)):
    dfdf['VISIT_AREA_NM'][i] = str(dfdf['VISIT_AREA_NM'][i])
    dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i].replace("(","").replace(")","").replace(",","").replace("\''","")
    dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i][1:-1]

dfdf = dfdf[dfdf['count'] >= 2]

visit_list = list(dfdf['VISIT_AREA_NM']) #visit_list에 2회 이상 방문지 리스트

#%%
#방문지가 2회 이상 방문한 관광지 아니면 제거

info.reset_index(drop = True, inplace = True)

for i in tqdm(range(len(info))):
    if info['VISIT_AREA_NM'][i] not in visit_list:
        info = info.drop([i], axis = 0)
info.reset_index(drop = True, inplace = True)
#%% info와 dfdf가 왜 다른지 알아보기 위한 코드 위에 ()를 빼는 과정에서 안에 있는 ()까지 빼내버려서 달라짐
# info_list = list(info['VISIT_AREA_NM'])
# for i in range(len(dfdf)):
#     if dfdf['VISIT_AREA_NM'][i] not in info_list:
#         print(dfdf['VISIT_AREA_NM'][i])

# In[68]:


#여행지 정보 저장
info.reset_index(drop = True, inplace = True)

#%% 시/도 이름 통일

info['SIDO'] = info['SIDO'].replace('인천광역시', '인천')
info['SIDO'] = info['SIDO'].replace('부산광역시', '부산')
info['SIDO'] = info['SIDO'].replace('경상북도', '경북')

#%% 
info.to_csv(path + '/source/관광지 추천시스템 여행지 정보 방문 2회 이상_mean5.csv', index=False)
