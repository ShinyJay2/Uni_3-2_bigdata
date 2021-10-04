#!/usr/bin/env python
# coding: utf-8

# In[759]:


import pandas as pd
import numpy as np


# In[760]:


df_2001_1 = pd.read_excel("C:/Users/User/Desktop/빅데이터과제1/2001년01분기.xlsx")
df_2001_2 = pd.read_excel("C:/Users/User/Desktop/빅데이터과제1/2001년02분기.xlsx")
df_2001_3 = pd.read_excel("C:/Users/User/Desktop/빅데이터과제1/2001년03분기.xlsx")
df_2001_4 = pd.read_excel("C:/Users/User/Desktop/빅데이터과제1/2001년04분기.xlsx")


# In[1076]:


df_2001 = pd.concat([df_2001_1, df_2001_2, df_2001_3, df_2001_4], ignore_index = True).copy()


# In[1077]:


df_2001.shape


# In[1078]:


df_2001 = df_2001.drop(['주소'], axis=1)


# In[1079]:


df_2001


# In[1080]:


df_2001['지역']=df_2001['지역'].str.extract(r'(\w{2})')


# In[1081]:


df_2001 = df_2001[~df_2001['측정소명'].str.contains('폐쇄')]


# In[1082]:


df_2001.tail()


# In[1083]:


list_obst = df_2001['측정소명'].unique()
print(list_obst)


# In[1084]:


def observe(obst):
    df_stats = df_2001[df_2001['측정소명'] == obst]
    df_stats = df_stats.replace(-999, np.nan)
    
    return df_stats 


# In[1085]:


def means(obst):
    df_stats = df_2001[df_2001['측정소명'] == obst]
    df_stats = df_stats.replace(-999, np.nan)
    
    return df_stats.mean()


# In[1086]:


name_column_list = []
ingridient = '측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10'

for i in range(11):
    name_column_list.append('측정소코드')
    name_column_list.append('측정일시')
    name_column_list.append('SO2')
    name_column_list.append('CO')
    name_column_list.append('O3')
    name_column_list.append('NO2')
    name_column_list.append('PM10')
    
print(name_column_list)


# In[1366]:


def jan(obst):
    df_stats = observe(obst)
    
    df_1 = df_stats.loc[df_stats['측정일시'].between(2001010101, 2001013124)]
    df_1.fillna(df_1.mean())
    df_1_fin = df_1.mean()
    df_1_fin = pd.DataFrame(df_1_fin, columns=[obst])
    
    if (obst == '설성면') or (obst == '북부동') or (obst == '치평동') or (obst == '삼산동') or (obst == '휴천동') or (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_1_fin = df_1_fin.drop(['지역', '측정소명'])
        df_1_fin.index = ['1_측정소코드', '1_측정일시', '1_SO2', '1_CO', '1_O3', '1_NO2', '1_PM10']
        
    else:
        df_1_fin.index = ['1_측정소코드', '1_측정일시', '1_SO2', '1_CO', '1_O3', '1_NO2', '1_PM10']
    
    return df_1_fin


# In[1367]:


def feb(obst):
    df_stats = observe(obst)
    
    df_2 = df_stats.loc[df_stats['측정일시'].between(2001020101, 2001023124)]
    df_2.fillna(df_2.mean())
    df_2_fin = df_2.mean()
    df_2_fin = pd.DataFrame(df_2_fin, columns=[obst])
    
    if (obst == '설성면') or (obst == '삼산동') or (obst == '휴천동') or (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_2_fin = df_2_fin.drop(['지역', '측정소명'])
        df_2_fin.index = ['2_측정소코드', '2_측정일시', '2_SO2', '2_CO', '2_O3', '2_NO2', '2_PM10']
        
    else:
        df_2_fin.index = ['2_측정소코드', '2_측정일시', '2_SO2', '2_CO', '2_O3', '2_NO2', '2_PM10']
    
    return df_2_fin


# In[1368]:


def mar(obst):
    df_stats = observe(obst)
    
    df_3 = df_stats.loc[df_stats['측정일시'].between(2001030101, 2001033124)]
    df_3.fillna(df_3.mean())
    df_3_fin = df_3.mean()
    df_3_fin = pd.DataFrame(df_3_fin, columns=[obst])
    
    if (obst == '삼산동') or (obst == '휴천동') or (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_3_fin = df_3_fin.drop(['지역', '측정소명'])
        df_3_fin.index = ['3_측정소코드', '3_측정일시', '3_SO2', '3_CO', '3_O3', '3_NO2', '3_PM10']
        
    else:
        df_3_fin.index = ['3_측정소코드', '3_측정일시', '3_SO2', '3_CO', '3_O3', '3_NO2', '3_PM10']
    
    return df_3_fin


# In[1369]:


def apr(obst):
    df_stats = observe(obst)
    
    df_4 = df_stats.loc[df_stats['측정일시'].between(2001040101, 2001043124)]
    df_4.fillna(df_4.mean())
    df_4_fin = df_4.mean()
    df_4_fin = pd.DataFrame(df_4_fin, columns=[obst])
    
    if (obst == '삼산동') or (obst == '휴천동') or (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_4_fin = df_4_fin.drop(['지역', '측정소명'])
        df_4_fin.index = ['4_측정소코드', '4_측정일시', '4_SO2', '4_CO', '4_O3', '4_NO2', '4_PM10']
        
    else:
        df_4_fin.index = ['4_측정소코드', '4_측정일시', '4_SO2', '4_CO', '4_O3', '4_NO2', '4_PM10']
    
    return df_4_fin


# In[1370]:


def may(obst):
    df_stats = observe(obst)
    
    df_5 = df_stats.loc[df_stats['측정일시'].between(2001050101, 2001053124)]
    df_5.fillna(df_5.mean())
    df_5_fin = df_5.mean()
    df_5_fin = pd.DataFrame(df_5_fin, columns=[obst])
    
    if (obst == '휴천동') or (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_5_fin = df_5_fin.drop(['지역', '측정소명'])
        df_5_fin.index = ['5_측정소코드', '5_측정일시', '5_SO2', '5_CO', '5_O3', '5_NO2', '5_PM10']
        
    else:
        df_5_fin.index = ['5_측정소코드', '5_측정일시', '5_SO2', '5_CO', '5_O3', '5_NO2', '5_PM10']
    
    return df_5_fin


# In[1371]:


def jun(obst):
    df_stats = observe(obst)
    
    df_6 = df_stats.loc[df_stats['측정일시'].between(2001060101, 2001063124)]
    df_6.fillna(df_6.mean())
    df_6_fin = df_6.mean()
    df_6_fin = pd.DataFrame(df_6_fin, columns=[obst])
    
    if (obst == '부곡동1') or (obst == '중앙로') or (obst == '청천면'):
        df_6_fin = df_6_fin.drop(['지역', '측정소명'])
        df_6_fin.index = ['6_측정소코드', '6_측정일시', '6_SO2', '6_CO', '6_O3', '6_NO2', '6_PM10']
        
    else:
        df_6_fin.index = ['6_측정소코드', '6_측정일시', '6_SO2', '6_CO', '6_O3', '6_NO2', '6_PM10']
    
    return df_6_fin


# In[1372]:


def jul(obst):
    df_stats = observe(obst)
    
    df_7 = df_stats.loc[df_stats['측정일시'].between(2001070101, 2001073124)]
    df_7.fillna(df_7.mean())
    df_7_fin = df_7.mean()
    df_7_fin = pd.DataFrame(df_7_fin, columns=[obst])
    
    if (obst == '청천면'):
        df_7_fin = df_7_fin.drop(['지역', '측정소명'])
        df_7_fin.index = ['7_측정소코드', '7_측정일시', '7_SO2', '7_CO', '7_O3', '7_NO2', '7_PM10']
        
    else:
        df_7_fin.index = ['7_측정소코드', '7_측정일시', '7_SO2', '7_CO', '7_O3', '7_NO2', '7_PM10']
    
    return df_7_fin


# In[1373]:


def aug(obst):
    df_stats = observe(obst)
    
    df_8 = df_stats.loc[df_stats['측정일시'].between(2001080101, 2001083124)]
    df_8.fillna(df_8.mean())
    df_8_fin = df_8.mean()
    df_8_fin = pd.DataFrame(df_8_fin, columns=[obst])
    df_8_fin.index = ['8_측정소코드', '8_측정일시', '8_SO2', '8_CO', '8_O3', '8_NO2', '8_PM10']
    
    return df_8_fin


# In[1374]:


def sep(obst):
    df_stats = observe(obst)
    
    df_9 = df_stats.loc[df_stats['측정일시'].between(2001090101, 2001093124)]
    df_9.fillna(df_9.mean())
    df_9_fin = df_9.mean()
    df_9_fin = pd.DataFrame(df_9_fin, columns=[obst])
    df_9_fin.index = ['9_측정소코드', '9_측정일시', '9_SO2', '9_CO', '9_O3', '9_NO2', '9_PM10']
    
    return df_9_fin


# In[1375]:


def oct(obst):
    df_stats = observe(obst)
    
    df_10 = df_stats.loc[df_stats['측정일시'].between(2001100101, 2001103124)]
    df_10.fillna(df_10.mean())
    df_10_fin = df_10.mean()
    df_10_fin = pd.DataFrame(df_10_fin, columns=[obst])
    df_10_fin.index = ['10_측정소코드', '10_측정일시', '10_SO2', '10_CO', '10_O3', '10_NO2', '10_PM10']
    
    return df_10_fin


# In[1376]:


def nov(obst):
    df_stats = observe(obst)
    
    df_11 = df_stats.loc[df_stats['측정일시'].between(2001110101, 2001113124)]
    df_11.fillna(df_11.mean())
    df_11_fin = df_11.mean()
    df_11_fin = pd.DataFrame(df_11_fin, columns=[obst])
    df_11_fin.index = ['11_측정소코드', '11_측정일시', '11_SO2', '11_CO', '11_O3', '11_NO2', '11_PM10']
    
    return df_11_fin


# In[1377]:


def dec(obst):
    df_stats = observe(obst)
    
    df_12 = df_stats.loc[df_stats['측정일시'].between(2001120101, 2001123124)]
    df_12.fillna(df_12.mean())
    df_12_fin = df_12.mean()
    df_12_fin = pd.DataFrame(df_12_fin, columns=[obst])
    df_12_fin.index = ['12_측정소코드', '12_측정일시', '12_SO2', '12_CO', '12_O3', '12_NO2', '12_PM10']
    
    return df_12_fin


# In[1378]:


aug('청천면')


# In[1379]:


dec('중구')


# In[1380]:


def obst_fin(obst):
    df_stats = observe(obst)
    df_1 = df_stats.loc[df_stats['측정일시'].between(2001010101, 2001013124)]
    df_1 = df_1.fillna(df_1.mean())
    
    df_2 = df_stats.loc[df_stats['측정일시'].between(2001020101, 2001023124)]
    df_2 = df_2.fillna(df_2.mean())
    
    df_3 = df_stats.loc[df_stats['측정일시'].between(2001030101, 2001033124)]
    df_3 = df_3.fillna(df_3.mean())
    
    df_4 = df_stats.loc[df_stats['측정일시'].between(2001040101, 2001043124)]
    df_4 = df_4.fillna(df_4.mean())
    
    df_5 = df_stats.loc[df_stats['측정일시'].between(2001050101, 2001053124)]
    df_5 = df_5.fillna(df_5.mean())
    
    df_6 = df_stats.loc[df_stats['측정일시'].between(2001060101, 2001063124)]
    df_6 = df_6.fillna(df_6.mean())
    
    df_7 = df_stats.loc[df_stats['측정일시'].between(2001070101, 2001073124)]
    df_7 = df_7.fillna(df_7.mean())
    
    df_8 = df_stats.loc[df_stats['측정일시'].between(2001080101, 2001083124)]
    df_8 = df_8.fillna(df_8.mean())
    
    df_9 = df_stats.loc[df_stats['측정일시'].between(2001090101, 2001093124)]
    df_9 = df_9.fillna(df_9.mean())
    
    df_10 = df_stats.loc[df_stats['측정일시'].between(2001100101, 2001103124)]
    df_10 = df_10.fillna(df_10.mean())
    
    df_11 = df_stats.loc[df_stats['측정일시'].between(2001110101, 2001113124)]
    df_11 = df_11.fillna(df_11.mean())
    
    df_12 = df_stats.loc[df_stats['측정일시'].between(2001120101, 2001123124)]
    df_12 = df_12.fillna(df_12.mean())
    
    df_full_data = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])
    
    return df_full_data


# In[1381]:


obst_fin('중구')


# In[1382]:


list_obst


# In[1383]:


column_list = ['지역', '측정소명', '측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10']


# In[1384]:


df_2001_new = pd.DataFrame()

for i in list_obst:
    df_2001_new = df_2001_new.append(obst_fin(i))
    
df_2001_new    


# In[1385]:


def merge_month(obst):
    df_2001_mean = pd.concat([jan(obst), feb(obst), mar(obst), apr(obst), may(obst), jun(obst), jul(obst), aug(obst), sep(obst), oct(obst), nov(obst), dec(obst)])
    return df_2001_mean


# In[1386]:


merge_month('중구')


# In[1394]:


obst_list = ['중구', '한강대로', '종로구', '청계천', '용산구', '광진구', '성동구', '중랑구', '동대문구',
       '동대문', '청량리', '성북구', '도봉구', '은평구', '서대문구', '마포구', '신촌로', '강서구',
       '구로구', '영등포구', '영등포로', '동작구', '관악구', '강남구', '서초구', '도산대로', '송파구',
       '강동구', '금천구', '강북구', '양천구', '노원구', '신풍동', '인계동', '광교동', '단대동',
       '정자1동', '의정부동', '안양6동', '부림동', '호계동', '철산동', '고잔동', '원시동', '본오동',
       '원곡동', '별양동', '과천동', '교문동', '정왕동', '시화공단', '금곡동', '비전동', '행신동',
       '김량장동', '설성면', '사우동', '당동', '방산면', '광복동', '초량동', '태종대', '전포동',
       '온천동', '대연동', '학장동', '덕천동', '청룡동', '장림동', '연산동', '회원동', '봉암동',
       '대송동', '성남동', '부곡동(울산)', '여천동(울산)', '야음동', '신정2동', '신정동', '덕신리',
       '무거동', '상봉동', '명서동', '웅남동', '가음정동', '경화동', '동상동', '저구리', '북부동',
       '화산리', '상남리', '서석동', '농성동', '치평동', '두암동', '운암동', '송정1동', '중앙동(전주)',
       '용당동', '광무동', '주삼동', '월내동', '장천동', '중동', '태인동', '나불리', '이도동',
       '고산리', '남산동', '수창동', '이현동', '평리동', '대명동', '노원동', '신암동', '만촌동',
       '장흥동', '죽도동', '대도동', '성건동', '신음동', '남문동', '공단동', '원평동', '형곡동',
       '지품면', '태하리', '읍내동', '문창동', '구성동', '대흥동1', '송정동(봉명동)', '사천동',
       '성황동', '독곶리', '동문동', '파도리', '중앙동(원주)', '명륜동', '옥천동', '간성읍', '장락동',
       '삼천동', '팔복동', '신풍동2', '소룡동', '개정동', '남중동', '운암면', '신흥', '송림',
       '구월동', '숭의', '석바위', '부평', '연희', '고잔', '석남', '송해', '소사본동', '내동',
       '중2동', '석모리', '삼산동', '휴천동', '부곡동1', '중앙로', '청천면']

df_2001_mean = pd.DataFrame()

append_list = []

for i in obst_list:
    append_list.append(merge_month(i))
    
    
df_2001_mean = pd.concat(append_list, axis = 1)
    
df_2001_mean


# In[1395]:


df_2001_mean.to_excel('C:/Users/User/Desktop/2001년월별_평균.xlsx')


# In[1396]:


df_2001_new.to_excel('C:/Users/User/Desktop/2001년_데이터.xlsx')


# In[ ]:




