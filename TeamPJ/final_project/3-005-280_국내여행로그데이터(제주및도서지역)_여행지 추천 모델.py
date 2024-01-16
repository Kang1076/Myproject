#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
import joblib
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore') #warning 문구 제거
pd.set_option('display.max_columns', None)

#%%

#데이터 불러오기
path = '.'
visit_area_info = pd.read_csv(path + '/tn_visit_area_info_방문지정보_D.csv') # 방문지 정보 activity
travel = pd.read_csv(path+'/tn_travel_여행_D.csv') # 여행 travel
traveller_master = pd.read_csv(path+'/tn_traveller_master_여행객 Master_D.csv') #여행객 정보 Master traveler


# # 전처리

# ## 1) visit_area_info 방문지 정보 df

# In[4]:


# 관광지 선택
visit_area_info = visit_area_info[ (visit_area_info['VISIT_AREA_TYPE_CD'] == 1) | 
                                  (visit_area_info['VISIT_AREA_TYPE_CD'] == 2) |
           (visit_area_info['VISIT_AREA_TYPE_CD'] == 3) | (visit_area_info['VISIT_AREA_TYPE_CD'] == 4) |
           (visit_area_info['VISIT_AREA_TYPE_CD'] == 5) | (visit_area_info['VISIT_AREA_TYPE_CD'] == 6) |
            (visit_area_info['VISIT_AREA_TYPE_CD'] == 7) | (visit_area_info['VISIT_AREA_TYPE_CD'] == 8)]


# In[5]:


#인덱스 재정렬
visit_area_info = visit_area_info.reset_index(drop = True)


# In[6]:


#제대로 추출되었는지 확인
visit_area_info['VISIT_AREA_TYPE_CD'].unique()


# In[7]:


visit_area_info.dropna(subset = ['LOTNO_ADDR'], inplace = True)
visit_area_info = visit_area_info.reset_index(drop = True)


# In[8]:


# 시도/군구 변수 생성
sido = []
gungu = []
eupmyeon = []
for i in range(len(visit_area_info['LOTNO_ADDR'])):
    sido.append(visit_area_info['LOTNO_ADDR'][i].split(' ')[0])
    gungu.append(visit_area_info['LOTNO_ADDR'][i].split(' ')[1])
    eupmyeon.append(visit_area_info['LOTNO_ADDR'][i].split(' ')[2])


# In[9]:


visit_area_info['SIDO'] = sido
visit_area_info['GUNGU'] = gungu
visit_area_info['EUPMYEON'] = eupmyeon


# ### 변수 선택

# TRAVEL_ID 여행 ID
# 
# VISIT_AREA_NM 방문 장소 이름
# 
# SIDO 시/도
# 
# GUNGU 군/구
# 
# VISIT_AREA_TYPE_CD 관광 장소 유형
# 
# DGSTFN 만족도
# 
# REVISIT_INTENTION 재방문의향
# 
# RCMDTN_INTENTION 추천의향
# 
# RESIDENCE_TIME_MIN 체류시간분
# 
# REVISIT_YN 재방문여부

# In[10]:

## 추후 x,y 코드 가져와서 시각화 해야할 수 있다.
visit_area_info = visit_area_info[['TRAVEL_ID', 'VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD', 'DGSTFN',
                                  'REVISIT_INTENTION', 'RCMDTN_INTENTION', 'RESIDENCE_TIME_MIN', 'REVISIT_YN']]


# ## 2) travel 여행 정보 df

# In[11]:

# ?? 미션 우선도가 뭐임?
# TRAVEL_MISSION_CHECK의 첫번째 항목 가져오기
travel_list = []
for i in range(len(travel)):
    value = int(travel['TRAVEL_MISSION_CHECK'][i].split(';')[0])
    travel_list.append(value)

travel['TRAVEL_MISSION_PRIORITY'] = travel_list


# ### 변수 선택

# TRAVEL_ID: 여행 ID
# 
# TRAVELER_ID: 여행자 ID
# 
# TRAVEL_MISSION_PRIORITY: 개별 미션 우선도 중 첫번째

# In[12]:


travel = travel[['TRAVEL_ID', 'TRAVELER_ID', 'TRAVEL_MISSION_PRIORITY']]


# ## 3) traveller_master 여행자 정보 df

# ### 변수 선택

# TRAVELER_ID 여행객ID
# 
# GENDER 성별
# 
# AGE_GRP 연령대
# 
# INCOME 소득
# 
# TRAVEL_STYL(1,2,3,4,5,6,7,8) 여행 스타일 
# 
# TRAVEL_MOVTIVE(1) 여행 동기 - 2,3은 결측치가 있어 제외
# 
# TRAVEL_NUM 여행빈도
# 
# TRAVEL_COMPANIONS_NUM 동반자 수
# 

# In[13]:


traveller_master = traveller_master[['TRAVELER_ID', 'GENDER', 'AGE_GRP', 'INCOME', 'TRAVEL_STYL_1', 
                                     'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4', 'TRAVEL_STYL_5', 
                                     'TRAVEL_STYL_6', 'TRAVEL_STYL_7','TRAVEL_STYL_8', 
                                      'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM' ]]


# ## 데이터 프레임 합치기

# In[14]:


df = pd.merge(travel, traveller_master, left_on = 'TRAVELER_ID', right_on = 'TRAVELER_ID', how = 'inner')


# In[15]:


df = pd.merge(visit_area_info, df, left_on = 'TRAVEL_ID', right_on = 'TRAVEL_ID', how = 'right')


# In[16]:


len(df['TRAVEL_ID'].unique())


# ## 만족도(y) 결측치 삭제

# In[17]:


df = df.dropna(subset = ['DGSTFN'])
df.reset_index(drop=True, inplace=True)


# In[18]:


len(df['TRAVEL_ID'].unique())


# ## 체류시간 결측치 대체
# 

# 체류시간 0을 median 60으로 바꾸기

# In[19]:


df['RESIDENCE_TIME_MIN'] = df['RESIDENCE_TIME_MIN'].replace(0,60)


# ## 재방문여부 원핫인코딩

# In[20]:


df['REVISIT_YN'] = df['REVISIT_YN'].replace("N",0)
df['REVISIT_YN'] = df['REVISIT_YN'].replace("Y",1)


# ## 여행스타일 결측치 삭제

# In[21]:


df.dropna(subset = ['TRAVEL_STYL_1'], inplace = True)
df.reset_index(drop= True, inplace = True)


# In[22]:


df


# In[23]:


df.shape


# In[24]:


df.isna().sum().sum()


# In[25]:


len(df['TRAVEL_ID'].unique())


# # Train-test split

# -유니크한 관광지 정보가 모두 train set에 있어야 한다. (train set에 경복궁 없고 test set에만 경복궁 있으면 안된다. 왜냐하면 방문지 변수가 있기 때문에 입력되지 않은 방문지에 대한 정보는 모델이 학습할 수 없기 때문이다.)
# 
# -또한 새로운 유저에 대한 추측이기 때문에 유저 데이터는 무조건 train / test 중 한 곳에만 있다. (유저 A의 ㄱ관광지는 train, ㄴ관광지는 test 에 있을 수 없다.)
# 
# -이를 반영해서 train test split 진행하면 된다. 
# 
# -train set에서만 (방문지마다 체류시간 평균, 추천의향의 평균, 재방문여부의 평균, 동반자 수의 평균, 재방문의향의 평균)을 산출하고, 이 값을 test set에 대입한다. 

# In[26]:

# Train세트와 test세트(df1)를 만듬
from tqdm import tqdm
df1 = df
Train = pd.DataFrame(columns = list(df.columns))
for i in tqdm(list(df['VISIT_AREA_NM'].unique())): # 유니크한 관광지 목록 중에서
    df2 = df1[df1['VISIT_AREA_NM'] == i] # 특정 관광지에 간 모든 사람 뽑아서
    np.random.seed(42)
    if df2.empty:
        pass
    else:
        random_number = np.random.randint(len(df2)) 
        df_id = df2.iloc[[random_number]] # 그 중 랜덤으로 관광지에 간 사람 한 명 뽑아서
        index = df_id.iloc[0,0]
        df3 = df1[df1['TRAVEL_ID'] == index] #그 사람이 간 모든 관광지를 구해서
        df1 = pd.merge(df3, df1, how = 'outer', indicator = True)
        df1 = df1.query('_merge =="right_only"').drop(columns = ['_merge']) # 기존 데이터프레임에서 그 사람 내용을 삭제하고
        Train = pd.concat([Train,df3], ignore_index=True) #train set 에 추가


# In[27]:

# train 0.8 // test 0.2 비율로 맞추기
while len(df1)/len(df) > 0.2:
    np.random.seed(42)
    random_number = np.random.randint(len(df1))
    df_id = df1.iloc[[random_number]]
    index = df_id.iloc[0,0]
    df3 = df1[df1['TRAVEL_ID'] == index]
    df1 = pd.merge(df3, df1, how = 'outer', indicator = True)
    df1 = df1.query('_merge =="right_only"').drop(columns = ['_merge'])
    Train = pd.concat([Train, df3], ignore_index=True)


# ## Train set에서 방문지에 대한 변수 생성
# 방문지마다 체류시간 평균, 추천의향의 평균, 재방문여부의 평균, 동반자 수의 평균, 재방문의향의 평균 산출

# In[29]:


#새로운 데이터프레임 생성해서, 이 데이터프레임에 평균값을 추가한 새로운 Train set 생성할 것임

new_train = pd.DataFrame(columns = list(Train.columns) + ['RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean',
                                                          'REVISIT_YN_mean', 'TRAVEL_COMPANIONS_NUM_mean',
                                                          'REVISIT_INTENTION_mean'])

# globals()[str(j)+'_mean'] 이거 그냥 전역변수 이렇게 생각하지 말고 변수를 동적으로 생성한다고 생각해야함
# 쉽게 생각하려면 그냥 첫 j에서 문자열 'RESIDENCE_TIME_MIN_mean'과 똑같다.

# 기존 열들로 새로운 열 만드는 반복문 new_train에 새로운 훈련셋이 담김
for i in tqdm(list(Train['VISIT_AREA_NM'].unique())): #유니크한 관광지 목록 중에서
    df2 = Train[Train['VISIT_AREA_NM'] == i] # 특정 관광지에 간 모든 사람 뽑아서
    for j in ['RESIDENCE_TIME_MIN', 'RCMDTN_INTENTION', 'REVISIT_YN', 'TRAVEL_COMPANIONS_NUM', 'REVISIT_INTENTION']:
        #체류시간 평균 산출 
        globals()[str(j)+'_mean'] = df2[str(j)]
        globals()[str(j)+'_mean'] = np.mean(globals()[str(j)+'_mean'])
        #데이터프레임에 들어가게 값을 리스트 형태로 변환
        globals()[str(j)+'_mean'] = np.repeat(globals()[str(j)+'_mean'], len(df2)) 
        df2[str(j)+'_mean'] = globals()[str(j)+'_mean']
    #새로운 데이터프레임에 방문지별 평균값 대입
    new_train = pd.concat([new_train, df2], axis = 0)


# In[30]:


#편의를 위해 유저별 정렬
new_train.sort_values(by = ['TRAVEL_ID'], axis = 0, inplace = True)


# ## DATA SET 저장

# In[31]:


#train set 저장
new_train.to_csv(path + '/관광지 추천시스템 Trainset_D.csv', index = False)
#test set 저장
df1.to_csv(path + '/관광지 추천시스템 Testset_D.csv', index = False)


# In[32]:


# 파일 불러오기
path = '.'

Train = pd.read_csv(path + '/관광지 추천시스템 Trainset_D.csv')
test = pd.read_csv(path + '/관광지 추천시스템 Testset_D.csv')


# In[33]:


print(Train.shape)
print(test.shape)


# In[35]:


Train


# In[36]:


test


# # 여행 방문지 필터링

# ## 6번 이상 방문한 곳

# In[37]:

count = pd.DataFrame(Train['VISIT_AREA_NM'].value_counts())
count.reset_index(inplace=True)

# In[38]:


print(list(count.groupby(['VISIT_AREA_NM'])['VISIT_AREA_NM'].count()))


# In[39]:


#6번 이상 방문한 곳으로만 필터링
### 여기 숫자 변경
six_places = list(count[count['count']>=6]['VISIT_AREA_NM'])
###
for i in range(len(Train)):
    if Train['VISIT_AREA_NM'][i] not in six_places:
        Train = Train.drop([i], axis = 0)
Train.reset_index(drop = True, inplace = True)


# In[40]:


#확인
count1 = pd.DataFrame(Train['VISIT_AREA_NM'].value_counts())
count1.reset_index(inplace=True)
count1.groupby(['VISIT_AREA_NM'])['VISIT_AREA_NM'].count()


# In[41]:


Train.shape


# In[42]:


(len(Train['TRAVEL_ID'].unique()) + len(test['TRAVEL_ID'].unique())) / 4000


# In[43]:


(len(Train['TRAVEL_ID'].unique()) + len(test['TRAVEL_ID'].unique()))


# In[46]:


len(Train['TRAVEL_ID'].unique())/ 4000


# In[45]:


len(Train['TRAVEL_ID'].unique())


# In[47]:


len(test['TRAVEL_ID'].unique())/4000


# In[48]:


len(test['TRAVEL_ID'].unique())


# In[49]:


Train


# # Catboost 모델 기반 추천시스템 학습

# In[50]:


#학습에 필요없는 feature 제거
Train.drop(['TRAVELER_ID', 'REVISIT_INTENTION',
            'RCMDTN_INTENTION','RESIDENCE_TIME_MIN', 'REVISIT_YN'], axis = 1, inplace = True)
test.drop(['TRAVELER_ID', 'REVISIT_INTENTION',
            'RCMDTN_INTENTION','RESIDENCE_TIME_MIN', 'REVISIT_YN'], axis = 1, inplace = True)


# In[51]:


# 데이터 타입 변경
Train['VISIT_AREA_TYPE_CD'] = Train['VISIT_AREA_TYPE_CD'].astype('string')
test['VISIT_AREA_TYPE_CD'] = test['VISIT_AREA_TYPE_CD'].astype('string')


# In[52]:


y_train = Train['DGSTFN']
X_train = Train.drop(['DGSTFN'], axis = 1)


# ## 초모수 조절
# Cross Validation Set 생성 + Random Search 함수

# train set의 feature, target, cv 개수를 입력하면 cross validaiton set을 생성해주는 함수 생성
# 
# 최대한 많은 관광지 정보를 보존하기 위해 cv = 10 으로 설정

# In[53]:


def cross_validation(X_train, y_train, cv, iteration, number, learning_rate, depth,
                     early_stopping_rounds, random_state): #X_train 데이터, y_train 데이터, cv 개수, random search 횟수, random_state

    X_train1 = X_train #변수 옮기기
    y_train1 = y_train #변수 옮기기
    
    # cv수 만큼 훈련세트, 훈련세트타겟 생성
    for i in range(cv): #각 fold마다의 X_train, y_train 생성 (Train_1, Train_2, ... / target_1, target_2, ...)
        globals()['Train_'+str(i+1)] = pd.DataFrame(columns = list(X_train.columns))
        globals()['target_'+str(i+1)] = []
    print(str(cv)+'개의 fold를 생성중입니다.....')
    for i in tqdm(range(cv)):
        np.random.seed(random_state) #초기 시드 설정
        while (len(globals()['Train_'+str(i+1)]) / len(X_train)) < (1/cv): #1/cv 비율 만큼의 데이터가 모일 때까지
            random_number = np.random.randint(len(X_train1))
            df_id = X_train1.iloc[[random_number]]
            index = df_id.iloc[0,0] #랜덤하게 유저를 선택하고
            df1 = X_train1[X_train1['TRAVEL_ID'] == index] #그 유저가 갔던 모든 여행지 불러오고
            target_index = X_train1[X_train1['TRAVEL_ID'] == index].index
            X_train1 = pd.merge(df1, X_train1, how = 'outer', indicator = True)
            X_train1 = X_train1.query('_merge =="right_only"').drop(columns = ['_merge']) #기존 데이터프레임은 해당 유저 정보 삭제
            globals()['Train_'+str(i+1)] = pd.concat([globals()['Train_'+str(i+1)], df1], ignore_index=True) #validation set에 유저의 X_train 삽입
            globals()['target_'+str(i+1)].extend(list(y_train[list(target_index)])) #유저의 X_train에 상응하는 y_train 삽입
            if len(X_train1) == 0: #기존 데이터프레임에 모든 유저정보가 사라지면 validation set 생성이 완료된 것이므로 정지
                break
    print(str(cv)+'개의 fold 생성이 완료되었습니다!')
    print('함수에서 설정한 초모수 범위 내에서 ' + str(cv)+'개의 validation 검정을 진행합니다...' )
    
    
    np.random.seed(random_state)
    initial = 0
    
    # cross_valdation함수의 iteration매개변수 만큼 반복진행
    for a in tqdm(range(iteration)):
        print(str(a+1) + "번째 초모수 조절치에 대한 학습을 진행합니다....")
        ##########여기에 원하는 hyperparameter 기입###########
        ######################################################
        n_estimators = np.random.choice(np.arange(3000, 3501, 500))
        #n_estimators = 2500
        print(n_estimators)
        ######################################################
######################################################
        final_recall = [] # K개의 검증 성능이 들어갈 리스트

        for j in range(cv): #K개 fold중
            # cv수 만큼 fold를 나누고 그 중 하나는 검증세트로, 나머지는 합쳐서 훈련세트로 만듬
            # y_new_train에는 타겟값
            print(str(a+1) + '번째 초모수 조절치의' + str(j+1)+'번째 fold를 학습하고 있습니다....')
            #한 fold에 대해서 학습
            combine_df_list = list(range(1, (cv+1))) # 1부터 cv까지 숫자리스트 만들어서
            del combine_df_list[j] #숫자 하나를 지우고, 그 숫자가 있는 Train set을 Validation set으로 설정
            #예를 들어 1이 빠졌으면 Train_1이 validation set, Train_2, Train_3, ... 는 Train set
            X_new_train = pd.DataFrame(columns = list(globals()['Train_'+str(j+1)].columns))
            y_new_train = []
            for i in combine_df_list: #지운 숫자 외의 숫자가 있는 Train set들을 결합
                X_new_train = pd.concat([X_new_train, globals()['Train_'+str(i)]], axis = 0) #X_train 결합
                y_new_train.extend(globals()['target_'+str(i)]) #y_train 결합
            y_new_train = np.array(y_new_train).astype(float)
            X_new_train.drop(['TRAVEL_ID'], axis = 1, inplace = True) #필요 없는 컬럼 제거
            if 'DGSTFN' in list(X_new_train.columns): #global 함수에서 발생하는 오류 해결
                X_new_train.drop(['DGSTFN'], axis = 1, inplace = True)
            # 캣부스트회귀 모델 만들고
            model = CatBoostRegressor(n_estimators = n_estimators,
                                  cat_features = ['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
                                              'TRAVEL_MISSION_PRIORITY', 'AGE_GRP', 'GENDER'],
                                  learning_rate = learning_rate,
                                  depth = depth,
                                  random_state = 42)
        ##############################################################################################
            # 훈련시키고
            model.fit(X_new_train, y_new_train, early_stopping_rounds=early_stopping_rounds) #########모델 적합

            #학습한 fold에 대한 test 값 도출
            # 여기에 결국 검증세트로 predict했을때 얼만큼의 성능이 나왔는지에 대한 지표가 들어갈거임
            # 자세한건 밑에서 다시 나올때
            recall_10_list = [] #validation set의 recall 측정값들이 들어갈 리스트
            #####################유저 정보##################################
            # 유저 정보는 검증세트에서 가저온다
            # 결국 여기서 얻는건 data1이라는 데이터프레임인데 data1은 웹에서 얻게되는 이용자의 유저 정보로 보면됨
            # 근데 이제 sido_gungu_list열이 추가가 되는데 이건 이용자가 원하는 여행장소(시군구)로 볼 수 있다.
            # data1은 중복id없음
            data = globals()['Train_'+str(j+1)][['TRAVEL_ID', 'SIDO', 'GUNGU', 'EUPMYEON', 'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                                    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                                    'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                                    'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM']]
            data1 = pd.DataFrame(columns=['TRAVEL_ID', 'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                                    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                                    'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                                    'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM', 'sido_gungu_list'])
            for i in list(data['TRAVEL_ID'].unique()):
                temp_df = data[data['TRAVEL_ID'] == i]
                temp_df1 = temp_df[['SIDO', 'GUNGU', 'EUPMYEON']] #각 유저별 방문한 시군구 확인
                temp_df1.reset_index(drop = True, inplace = True)
                sido_gungu_visit = []
                for k in range(len(temp_df1)):
                    sido_gungu_visit.append(temp_df1['SIDO'][k] + '+' + temp_df1['GUNGU'][k] + '+' + temp_df1['EUPMYEON'][k])
                sido_gungu_list = list(set(sido_gungu_visit))
                new = temp_df.drop(['SIDO', 'GUNGU', 'EUPMYEON'], axis = 1) #기존 시도, 군구 제외하고
                new = new.head(1)
                new['sido_gungu_list'] = str(sido_gungu_list)
                data1 = pd.concat([data1, new], axis = 0) #새로운 데이터프레임 생성 
            data1.reset_index(drop = True, inplace = True)
            ##########################여행지 정보################################
            # 여행지 정보는 훈련세트에서 가져온다. 방문횟수가 number매개변수 이상인 여행지를 중복없이 담은
            # info 데이터 프레임을 얻는다.
            info = X_new_train[['SIDO', 'VISIT_AREA_NM', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD','RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean',
            'REVISIT_YN_mean', 'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']]
            info.drop_duplicates(['VISIT_AREA_NM'], inplace = True)
            ###### n회 이상 관광한 방문지 리스트 생성
            visiting_list = X_new_train[['VISIT_AREA_NM']] #train set에 있는 방문지에 대해서만 2회 이상 방문하였는지 확인
            visiting_list.reset_index(drop = True, inplace = True)
            #데이터 전처리
            dfdf = pd.DataFrame(visiting_list.value_counts(), columns = ['count'])
            dfdf['VISIT_AREA_NM'] = dfdf.index
            dfdf.reset_index(drop = True, inplace = True)
            for i in range(len(dfdf)):
                dfdf['VISIT_AREA_NM'][i] = str(dfdf['VISIT_AREA_NM'][i])
                dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i].replace("(","").replace(")","").replace(",","").replace("\''","")
                dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i][1:-1]
            #n회 이상 적용
            dfdf = dfdf[dfdf['count'] >= number] 
            visit_list = list(dfdf['VISIT_AREA_NM']) #visit_list에 n회 이상 방문지 리스트
            #방문지가 n회 이상 방문한 관광지 아니면 제거
            info.reset_index(drop = True, inplace = True)
            for i in range(len(info)):
                if info['VISIT_AREA_NM'][i] not in visit_list:
                    info = info.drop([i], axis = 0)
            info.reset_index(drop = True, inplace = True)
            ##########################모델 10개 관광지 추천############################
            # 이 result에 담기는 값은
            result = []
            for i in range(len(data1)):
                #데이터
                # final_df는 predict할 때 사용하는 데이터프레임(가공된 검증세트 같은 느낌)
                # 여기가 좀 이해 안될 수 있는데 훈련세트 안에 있는 관광지 중에서 
                # 이용자가 원하는 장소(시군구)에 있는 관광지가 들어있는 데이터 프레임이 final_df임
                
                # 이걸 위해 간단히 설명을 덧붙이자면 이 모델은 이용자가 시군구를 입력하면 거기에 있는 
                # 여행자가 좋아할만한 다양한 장소들을 추천해주는 모델이 아님 실제로는 훈련세트안에 있는 장소들을
                # 기억해놨다가 이용자가 시군구를 입력하면 해당 시군구에 있는 입력된 관광지들이 쭉 나오고
                # 그 중에서 이용자가 갔을 때 만족도가 높을 것 같은 장소 상위 10개를 추천해주는 모델임
                # 즉 훈련세트를 통해 학습시킨 관광지만 추천해 줄 수 있다.
                
                # 결론적으로 final_df는 이용자가 입력한(여기선 방문한 이지만 입력한으로 본다.) 시군구에 있는
                # 훈련세트를 통해 학습된 관광지들이 전부 담긴 데이터프레임이다.
                
                # 그렇기 때문에 검증세트에서 방문한 시군구가 훈련세트에 입력되어 있지않으면 빈 데이터프레임이된다.
                
                final_df = pd.DataFrame(columns = ['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
                       'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                       'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                       'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                       'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
                       'RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean', 'REVISIT_YN_mean',
                       'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']) #빈 데이터프레임에 내용 추가
                ####### 시/도 군/구 별 자료 수집
                temp = data1['sido_gungu_list'][i].replace("[","").replace("]","").replace("\'","").replace(", ",",")
                places_list = list(map(str, temp.split(",")))
                for q in places_list:
                    sido, gungu, eupmyeon = map(str, q.split("+"))

                    info_df = info[(info['SIDO'] == sido) & (info['GUNGU'] == gungu)& (info['EUPMYEON'] == eupmyeon)] 

                    # info_df.drop(['SIDO'], inplace = True, axis = 1)
                    info_df.reset_index(inplace = True, drop = True)
                    data2 = data1.drop(['sido_gungu_list','TRAVEL_ID'], axis =1)
                    user_df = pd.DataFrame([data2.iloc[i].to_list()]*len(info_df), columns = ['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                                        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                                        'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                                        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM'])
                    df = pd.concat([user_df, info_df], axis = 1)
                    df = df[['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
                   'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                   'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                   'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                   'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
                   'RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean', 'REVISIT_YN_mean',
                   'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']] # 변수정렬
                    df['VISIT_AREA_TYPE_CD'] = df['VISIT_AREA_TYPE_CD'].astype('string')
                    final_df = pd.concat([final_df, df], axis = 0)
                final_df.reset_index(drop = True, inplace = True)
                final_df.drop_duplicates(['VISIT_AREA_NM'], inplace = True)

                #모델 예측
                y_pred = model.predict(final_df)
                y_pred = pd.DataFrame(y_pred, columns = ['y_pred'])
                test_df1 = pd.concat([final_df, y_pred], axis = 1)
                test_df1.sort_values(by = ['y_pred'], axis = 0, ascending=False, inplace = True) # 예측치가 높은 순대로 정렬

                test_df1 = test_df1.iloc[0:10,] #상위 10개 관광지 추천

                visiting_candidates = list(test_df1['VISIT_AREA_NM']) # 모델이 추천한 관광지들을 리스트 형태로 변환

               # 유저정보와 추천 관광지
               # 여기서 다시 유저정보를 나눠주고
                test_df2 = test_df1[['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                                    'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                                    'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                                    'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM']]
                # 위에서 말했듯이 이용자(검증세트)가 입력한(방문한) 시군구가 훈련세트에 없는 경우가 있기 때문에
                # 그런 경우에는 len(test_df2)가 0이 될 수 있다. 이 때는 빈리스트를 result에 담는다.
                # 그 밖에 값이 있으면 test_df2의 열이름을 리스트로 rec에 담고 추천장소(이용자가 입력한
                # 시군구에 있는 관광지(근데 이 관광지는 훈련세트에 있음))를 append해준다. 그 후 result에 추가한다.
                # result는 data1의 길이와 같은 길이를 갖는다. data1은 이용자(검증세트)의 id를 유니크로 뽑아낸 길이
                
                # 결론만 말하면 result는 이용자의 유저정보와 추천 관광지가 리스트형태로 담겨 있는 리스트이다.
                if len(test_df2) == 0:
                    rec = []
                    result.append(rec)
                else:

                    rec = test_df2.iloc[0].to_list()

                    rec.append(visiting_candidates)

                    result.append(rec)
            # result를 final_df라는 데이터프레임에 담아주고
            final_df = pd.DataFrame(result,
                                columns = ['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                                'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                                'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                                'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM', 'recommend_result_place'])
            # 그 중 추천 관광지만 가져온다
            # travel_id는 data1의 travel_id 즉 중복없는 이용자 아이디가 담긴다.
            final_df = final_df[['recommend_result_place']]
            travel_id = data1[['TRAVEL_ID']]
            travel_id.reset_index(drop = True, inplace = True)
            # 여기서 final_df에는 이용자 travel_id와 각각에게 추천된 추천 관광지가 담긴다.
            final_df = pd.concat([travel_id, final_df], axis = 1)

            #추천지 10개 미만인 여행 ID확인
            travel_id_list = [] # 추천지 10개 미만인 여행id가 담김
            for i in range(len(final_df)):
                recommend_list = final_df['recommend_result_place'][i]
                if str(recommend_list).count(',') < 9:
                    travel_id_list.append(final_df['TRAVEL_ID'][i])
                if pd.isna(str(recommend_list)):
                    travel_id_list.append(final_df['TRAVEL_ID'][i])
            ## 군구 리스트
            # 검증세트의 군구열이 구, 시, 군으로 끝나면 마지막 글자를 제외한다.
            places = list(set(globals()['Train_'+str(j+1)]['GUNGU']))
            for i in range(len(places)):
                if places[i][-1] == '구' or places[i][-1] == '시' or places[i][-1] == '군':
                    places[i] = places[i][:-1]

            ###############################################################
            ######## 최종 성능 평가 #########################################
            #########################################################
            # visit_list에는 훈련세트로 학습한 중복없는 number매개변수 이상 방문된 장소가 담김
            visit_list = list(info['VISIT_AREA_NM'])
            # 검증세트에 만족도(타겟)열 추가
            globals()['Train_'+str(j+1)]['DGSTFN'] = globals()['target_'+str(j+1)]

            for i in list(globals()['Train_'+str(j+1)]['TRAVEL_ID'].unique()):

                #추천한 방문지가 10개 미만이면 0
                if i in travel_id_list:
                    recall_10_list.append(0)
                    continue
                # 그냥 검증세트 중 추천관광지가 10개 이상인 여행id
                satisfied = globals()['Train_'+str(j+1)][globals()['Train_'+str(j+1)]['TRAVEL_ID'] == i]
                satisfied.reset_index(drop = True, inplace = True) 

                # 그 중 만족도 4이상인 여행id만 따로 빼서 satisfied1에 담음
                satisfied1 = satisfied[satisfied['DGSTFN'] >=4 ] #만족의 기준은 4이상 일때만 만족이라고 정의
                if len(satisfied1) == 0: # 유저가 만족한 관광지가 하나도 없으면 recall@10은 어차피 0
                    recall_10_list.append(0)
                    continue
                else:
                    # 이용자(검증세트)가 실제 방문한 장소 중 만족도(타겟)가 4이상인 장소가 item_list에 담겼다.
                    item_list = satisfied1['VISIT_AREA_NM']


                item_list = list(set(item_list))


            #final_df의 추천지 10개랑 비교

                recommend_list = final_df[final_df['TRAVEL_ID'] == i]['recommend_result_place']

                # 검증세트가 실제 방문했을 때 만족도가 4이상인 관광지가 추천지 10개 안에 있으면 summ에 +1한다.
                summ = 0
                for n in item_list:
                    word_list = list(n.split(' '))
                    if word_list[-1][-1] == '점': #지점명 삭제
                        del word_list[-1]
                    for o in word_list:
                        if o in places:#장소에 군/구 명 있으면 아무것도 하지 않고 스킵
                            pass
                        else:
                            for p in recommend_list: #장소에 교차어 있으면 해당 장소는 방문했다고 인식하기
                                if o in str(p) :
                                    summ += 1
                # 풀어 말하면 어떤 사람이 특정 시군구에 갔을 때 실제로 방문해서 만족했던 곳이 추천지 10개 안에
                # 몇 개가 있는지에 대한 비율
                recall10_for_1user = summ / min(10, len(satisfied1)) #recall@10 산식
                if recall10_for_1user > 1:
                    recall10_for_1user = 1
                # 얘들을 append해주면 recall_10_list에는 검증세트 모두에 대한 예측비율이 담김
                recall_10_list.append(recall10_for_1user)
            globals()['Train_'+str(j+1)].drop(['DGSTFN'], axis = 1, inplace = True) #globals 함수 오류 해결하기 위한 코드
            
            # 이걸 다시 평균내면 한 폴드의 전체 예측성능이 나온다.
            recall_for_one_cv = sum(recall_10_list) / len(recall_10_list) #한 fold에 대한 recall@10값 추출
            
            # 이걸 다시 cv수 만큼 리스트에 담아주고
            final_recall.append(recall_for_one_cv)
        
        # 평균내 주면 전체 검증세트에 대한 최종 예측성능이 나온다.
        recallat10 = sum(final_recall) / len(final_recall)
        print('이번 결과는:', recallat10)
        ###################### hyperparameter 바꾸면 여기도 수정해야 ######################
        ###################################################################################
        print('이번 결과의 parameter은: ', 'n_estimators:', n_estimators)
        if recallat10 > initial:
            initial = recallat10
            print('신기록!:', initial)
            print('n_estimators:', n_estimators)
            final_estimator = n_estimators

         #####################################################################################
    print('최종 parameter은 :',  final_estimator)
    return(initial)


# In[54]:


#초모수 조절
cross_validation(X_train, y_train, cv = 10, iteration = 2, number = 6,
                 learning_rate = 0.03, depth = 8, early_stopping_rounds = 5, random_state = 42)


# ## Catboost 적합

# 범주형 변수 목록
# 
# VISIT_AREA_NM 방문지
# 
# SIDO 시도
# 
# GUNGU 군구
# 
# VISIT_AREA_CD 관광지 종류 코드
# 
# TRAVEL_MISSION_PRIORITY 유저가 설정한 본인의 미션 중 첫번째
# 
# AGE_GRP 연령대
# 
# GENDER 성별

# In[55]:


y_train = Train['DGSTFN']
X_train = Train.drop(['DGSTFN', 'TRAVEL_ID'], axis = 1)


# In[56]:


model = CatBoostRegressor(n_estimators = 5000,
                          cat_features = ['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
                                      'TRAVEL_MISSION_PRIORITY', 'AGE_GRP', 'GENDER'],
                          learning_rate = 0.03,
                          depth = 8,
                          random_state = 42)

    # 훈련시키고
model.fit(X_train, y_train, early_stopping_rounds=5)


# In[57]:


now = time
print(now.strftime('%Y-%m-%d %H:%M:%S'))


# ## 모델 저장

# In[58]:


joblib.dump(model,path + '/catboost_model_D_test.pkl')


# In[59]:


modeld = joblib.load(path + '/catboost_model_D_test.pkl')
traind = pd.read_csv(path + '/관광지 추천시스템 Trainset_D.csv')
testd = pd.read_csv(path + '/관광지 추천시스템 Testset_D.csv')


# In[60]:


print(len(Train['TRAVEL_ID'].unique()))
print(len(test['TRAVEL_ID'].unique()))


# In[ ]:





# # Test D

# ## 모델의 10개 관광지 후보 불러오기

# ### 유저 정보

# In[61]:


y_testd = testd['DGSTFN']
X_testd = testd.drop(['DGSTFN'], axis = 1)


# In[62]:


#유저정보
data = testd[['TRAVEL_ID', 'SIDO', 'GUNGU', 'EUPMYEON', 'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                            'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                            'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                            'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM']]


# In[63]:


#내가 간 시도 군구 리스트:
data1 = pd.DataFrame(columns=['TRAVEL_ID', 'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                            'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                            'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                            'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM', 'sido_gungu_list'])
for i in tqdm(list(data['TRAVEL_ID'].unique())):
    temp_df = data[data['TRAVEL_ID'] == i]
    temp_df1 = temp_df[['SIDO', 'GUNGU', 'EUPMYEON']] #각 유저별 방문한 시군구 확인
    temp_df1.reset_index(drop = True, inplace = True)
    sido_gungu_visit = []
    for j in range(len(temp_df1)):
        sido_gungu_visit.append(temp_df1['SIDO'][j] + '+' + temp_df1['GUNGU'][j] + '+' +temp_df1['EUPMYEON'][j])
    sido_gungu_list = list(set(sido_gungu_visit))
    new = temp_df.drop(['SIDO', 'GUNGU', 'EUPMYEON'], axis = 1) #기존 시도, 군구 제외하고
    new = new.head(1)
    new['sido_gungu_list'] = str(sido_gungu_list)
    data1 = pd.concat([data1, new], axis = 0) #새로운 데이터프레임 생성        
    


# In[64]:


#유저 정보 저장
data1.reset_index(drop = True, inplace = True)
data1.to_csv(path + '/관광지 추천시스템 Testset_D- 유저 정보.csv', index=False)


# ### 여행지 정보

# In[65]:


#여행지 정보
info = traind[['SIDO', 'VISIT_AREA_NM', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD','RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean',
            'REVISIT_YN_mean', 'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']]
info.drop_duplicates(['VISIT_AREA_NM'], inplace = True)


# In[66]:


###### 6회 이상 관광한 방문지 리스트 생성
visiting_list = traind[['VISIT_AREA_NM']] #train set에 있는 방문지에 대해서만 2회 이상 방문하였는지 확인
visiting_list.reset_index(drop = True, inplace = True)
#데이터 전처리
dfdf = pd.DataFrame(visiting_list.value_counts(), columns = ['count'])
dfdf['VISIT_AREA_NM'] = dfdf.index
dfdf.reset_index(drop = True, inplace = True)
for i in range(len(dfdf)):
    dfdf['VISIT_AREA_NM'][i] = str(dfdf['VISIT_AREA_NM'][i])
    dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i].replace("(","").replace(")","").replace(",","").replace("\''","")
    dfdf['VISIT_AREA_NM'][i] = dfdf['VISIT_AREA_NM'][i][1:-1]
#6회 이상 적용
dfdf = dfdf[dfdf['count'] >= 6]########################## 
visit_list = list(dfdf['VISIT_AREA_NM']) #visit_list에 2회 이상 방문지 리스트


# In[67]:


#방문지가 6회 이상 방문한 관광지 아니면 제거
info.reset_index(drop = True, inplace = True)
for i in tqdm(range(len(info))):
    if info['VISIT_AREA_NM'][i] not in visit_list:
        info = info.drop([i], axis = 0)
info.reset_index(drop = True, inplace = True)


# In[68]:


#여행지 정보 저장
info.reset_index(drop = True, inplace = True)
info.to_csv(path + '/관광지 추천시스템 Testset_D- 여행지 정보.csv', index=False)


# In[69]:


len(info['VISIT_AREA_NM'].unique())
len(Train['VISIT_AREA_NM'].unique())


# ### 모델의 10개 추천 관광지 목록 제작 코드

# In[70]:


data = pd.read_csv(path + '/관광지 추천시스템 Testset_D- 유저 정보.csv')
info = pd.read_csv(path + '/관광지 추천시스템 Testset_D- 여행지 정보.csv')


# In[71]:


result = []
for i in tqdm(range(len(data1))):
    #데이터
    
    final_df = pd.DataFrame(columns = ['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
           'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
           'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
           'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
           'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
           'RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean', 'REVISIT_YN_mean',
           'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']) #빈 데이터프레임에 내용 추가
    ####### 시/도 군/구 별 자료 수집
    temp = data1['sido_gungu_list'][i].replace("[","").replace("]","").replace("\'","").replace(", ",",")
    places_list = list(map(str, temp.split(",")))
    for q in places_list:
        sido, gungu, eupmyeon = map(str, q.split("+"))

        info_df = info[(info['SIDO'] == sido) & (info['GUNGU'] == gungu) & (info['EUPMYEON'] == eupmyeon)] 

        # info_df.drop(['SIDO'], inplace = True, axis = 1)
        info_df.reset_index(inplace = True, drop = True)
        data2 = data1.drop(['sido_gungu_list','TRAVEL_ID'], axis =1)
        user_df = pd.DataFrame([data2.iloc[i].to_list()]*len(info_df), columns = ['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                            'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                            'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                            'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM'])
        df = pd.concat([user_df, info_df], axis = 1)
        df = df[['VISIT_AREA_NM', 'SIDO', 'GUNGU', 'EUPMYEON', 'VISIT_AREA_TYPE_CD',
       'TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
       'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
       'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
       'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM',
       'RESIDENCE_TIME_MIN_mean', 'RCMDTN_INTENTION_mean', 'REVISIT_YN_mean',
       'TRAVEL_COMPANIONS_NUM_mean', 'REVISIT_INTENTION_mean']] # 변수정렬
        df['VISIT_AREA_TYPE_CD'] = df['VISIT_AREA_TYPE_CD'].astype('string')
        final_df = pd.concat([final_df, df], axis = 0)
    final_df.reset_index(drop = True, inplace = True)
    final_df.drop_duplicates(['VISIT_AREA_NM'], inplace = True)

    #모델 예측
    y_pred = modeld.predict(final_df)
    y_pred = pd.DataFrame(y_pred, columns = ['y_pred'])
    test_df1 = pd.concat([final_df, y_pred], axis = 1)
    test_df1.sort_values(by = ['y_pred'], axis = 0, ascending=False, inplace = True) # 예측치가 높은 순대로 정렬

    test_df1 = test_df1.iloc[0:10,] #상위 10개 관광지 추천

    visiting_candidates = list(test_df1['VISIT_AREA_NM']) # 모델이 추천한 관광지들을 리스트 형태로 변환

# 유저정보와 추천 관광지
    test_df2 = test_df1[['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                        'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                        'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                        'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM']]
    if len(test_df2) == 0:
        rec = []
        result.append(rec)
    else:
        
        rec = test_df2.iloc[0].to_list()

        rec.append(visiting_candidates)

        result.append(rec)



# In[72]:


final_df = pd.DataFrame(result,
                            columns = ['TRAVEL_MISSION_PRIORITY', 'GENDER', 'AGE_GRP', 'INCOME',
                            'TRAVEL_STYL_1', 'TRAVEL_STYL_2', 'TRAVEL_STYL_3', 'TRAVEL_STYL_4',
                            'TRAVEL_STYL_5', 'TRAVEL_STYL_6', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8',
                            'TRAVEL_MOTIVE_1', 'TRAVEL_NUM', 'TRAVEL_COMPANIONS_NUM', 'recommend_result_place'])
final_df = final_df[['recommend_result_place']]
travel_id = data1[['TRAVEL_ID']]
travel_id.reset_index(drop = True, inplace = True)
final_df = pd.concat([travel_id, final_df], axis = 1)


# In[73]:


#output_df 저장
final_df.to_csv(path + '/관광지 추천시스템 Testset- OUTPUT_D.csv', index=False)
#output_df 불러오기
final_df = pd.read_csv(path + '/관광지 추천시스템 Testset- OUTPUT_D.csv')


# ## 실제 유저가 다녀온 관광지랑 비교하여 Recall@10 산출

# In[74]:


final_df


# In[75]:


#추천지 10개 미만인 여행 ID확인
# 이 숫자를 줄여도 성능이 올라가지 않을까?
travel_id_list = []
for i in tqdm(range(len(final_df))):
    recommend_list = final_df['recommend_result_place'][i]
    if pd.isna(recommend_list):
        travel_id_list.append(final_df['TRAVEL_ID'][i])
        continue
    if recommend_list.count(',') < 9:
        travel_id_list.append(final_df['TRAVEL_ID'][i])


# In[76]:


#군/군 리스트 출력
## 이 부분 해결 하기 위해서 군/구 목록 places라는 변수에 뽑아오기
'''
4. 성능을 올리기 위해 다음과 같은 추가 방법 도입:
- 아무래도 사람이 수기로 데이터를 입력하다 보니까 유사/동일 장소를 갔음에도 컴퓨터는 다른 장소로 인식 
    -ex1: ’파라다이스시티‘와 ’파라다이스시티 주차장‘을 다른 장소로 인식
    -ex2: ‘국립중앙박물관 특별전시관’과 ‘국립중앙박물관’을 다른 장소로 인식
- 그러므로 ‘모델이 추천한 추천지 10개’와 ‘유저가 만족한다고 했던 곳’을 단어 별로 쪼개서 공통어가 있으면 교집합 개수에 추가
    -ex1: ‘파라다이스시티’와 ‘파라다이스시티 주차장’은 ‘파라다이스시티’라는 공통어가 있으므로 교집합 개수에 추가
    -ex2: ‘국립중앙박물관 특별전시관’과 ‘국립중앙박물관’은 ‘국립중앙박물관’이라는 공통어가 있으므로 교집합 개수에 추가
- ‘파주점’, ‘하남점’ 등 지점명이 공통어가 되는 경우 배제
    -ex1: ‘롯데프리미엄아울렛 파주점'이라는 장소가 있을 때, 마지막 단어의 마지막 글자가 '점'일 경우에 마지막 글자를 제거 (공통어 비교 시 '롯데프리미엄아울렛'만 비교)
- 유저가 방문한 장소에 군/구가 공통어가 되는 경우 배제
    -ex1: 유저가 방문한 '스타필드 고양'은 ’스타필드‘, ’고양‘으로 나누어지는데, '고양'이라는 군/구 명을 제거해서 ’고양 어울림누리‘ 같은 장소와 교차어로 포함되지 않도록 함
'''
places = list(set(X_testd['GUNGU']))
for i in range(len(places)):
    if places[i][-1] == '구' or places[i][-1] == '시' or places[i][-1] == '군':
        places[i] = places[i][:-1]


# In[77]:


#유저가 다녀온 관광지 중에서 만족도가 4이상인 관광지 목록
recall_10_list = []
visit_list = list(info['VISIT_AREA_NM'])
for i in tqdm(list(testd['TRAVEL_ID'].unique())):
    
    #추천한 방문지가 10개 미만이면 0
    if i in travel_id_list:
        recall_10_list.append(0)
        continue
    
    satisfied = testd[testd['TRAVEL_ID'] == i] #실제(y_actual) 관광객이 만족한 관광지
    satisfied.reset_index(drop = True, inplace = True) 
    
    '''
    #2회 이상 방문한 곳에 대해서만 확인
    for c in range(len(satisfied)):
        if satisfied['VISIT_AREA_NM'][c] not in visit_list:
            satisfied = satisfied.drop([c], axis = 0)
    satisfied.reset_index(drop = True, inplace = True)    
    if len(satisfied) == 0:
        recall_10_list.append(0)
        continue
        
    '''
    satisfied1 = satisfied[satisfied['DGSTFN'] >=4 ] #만족의 기준은 4이상 일때만 만족이라고 정의
    if len(satisfied1) == 0: # 유저가 만족한 관광지가 하나도 없으면 recall@10은 어차피 0
        recall_10_list.append(0)
        continue
    else:
        item_list = satisfied1['VISIT_AREA_NM']
                
                
    item_list = list(set(item_list))
    
#final_df의 추천지 10개랑 비교
    recommend_list = final_df[final_df['TRAVEL_ID'] == i]['recommend_result_place'] #모델 추천 관광지 30개

    summ = 0
    for n in item_list:
        word_list = list(n.split(' '))
        if word_list[-1][-1] == '점': #지점명 삭제
            del word_list[-1]
        for o in word_list:
            if o in places:#장소에 군/구 명 있으면 아무것도 하지 않고 스킵
                pass
            else:
                for p in recommend_list: #장소에 교차어 있으면 해당 장소는 방문했다고 인식하기
                    if o in str(p) :
                        summ += 1
    recall10_for_1user = summ / min(10, len(satisfied1)) #recall@10 산식
    if recall10_for_1user > 1:
        recall10_for_1user = 1
    recall_10_list.append(recall10_for_1user)


# In[78]:


now = time
print(now.strftime('%Y-%m-%d %H:%M:%S'))


# In[79]:


#recall@10 구하기 

recall_10 = np.mean(recall_10_list)
#sum(recall_10_list) / len(recall_10_list)

# In[80]:


recall_10


# In[ ]:




