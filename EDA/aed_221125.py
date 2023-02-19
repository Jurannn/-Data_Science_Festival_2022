#!/usr/bin/env python
# coding: utf-8

# In[72]:


import geopandas as gpd
import pydeck as pdk
import numpy as np
import pandas as pd
import datetime
from datetime import datetime


# In[8]:


#한글 폰트 사용
from matplotlib import font_manager,rc
import matplotlib
import matplotlib.pyplot as plt

#폰트 경로
font_path = "C:/Windows/Fonts/H2GTRM.TTF"

#폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()

#font 설정
matplotlib.rc('font',family=font_name)


# ### 전체

# In[24]:


aed = pd.read_csv(r"C:\Users\USER\Desktop\데사페\AED동대문구.csv", encoding='utf-8')


# In[26]:


aed_loc = aed.loc[:,('위도', '경도')]
aed_loc.rename(columns = {'위도':'lat', '경도':'lng'}, inplace = True)
aed_loc


# In[28]:


aed_24 = pd.read_csv(r"C:\Users\USER\Desktop\데사페\AED동대문구_24.csv", encoding='utf-8')
aed_24_loc = aed_24.loc[:,('위도', '경도')]
aed_24_loc.rename(columns = {'위도':'lat', '경도':'lng'}, inplace = True)
aed_24_loc


# In[30]:


layer_ALL = pdk.Layer(
    'ScatterplotLayer',
    aed_loc,
    get_position='[lng, lat]',
    get_radius=200,
    get_fill_color='[255, 255, 255]',
    pickable=True,
    auto_highlight=True
)


layer_24 = pdk.Layer(
    'ScatterplotLayer',
    aed_24_loc,
    get_position='[lng, lat]',
    get_radius=200,
    get_fill_color='[255, 0, 0]',
    pickable=True,
    auto_highlight=True
)

center = [127.0400, 37.5744]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r = pdk.Deck(layers=[layer_ALL, layer_24], initial_view_state=view_state)
r.to_html()


# In[31]:


layer_24 = pdk.Layer(
    'ScatterplotLayer',
    aed_24_loc,
    get_position='[lng, lat]',
    get_radius=200,
    get_fill_color='[255, 0, 0]',
    pickable=True,
    auto_highlight=True
)

center = [127.0400, 37.5744]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

r24 = pdk.Deck(layers=[layer_24], initial_view_state=view_state)
r24.to_html()


# In[58]:


occur = pd.read_csv(r"C:\Users\USER\Desktop\데사페\전체_발생건수.csv", encoding='cp949')


# In[82]:


seoul = occur[occur['시도별(1)'] == '서울']
seoul = seoul.drop([seoul.index[3], seoul.index[-1]])
seoul


# In[ ]:





# In[92]:


snum= seoul.T[3::2]
snum = snum.reset_index()
snum


# In[88]:


snum.dtypes


# In[93]:


date = []
for i in range(len(snum)):
    str_datetime = snum['index'][i]
    format = '%Y'
    date.append(datetime.strptime(str_datetime, format))


# In[94]:


snum['date'] = date


# In[103]:


for i in [15,16,17,19,20,21,22,23,24,25,26,27]:
    snum[i] = snum[i].astype(int)


# In[106]:


snum


# In[123]:


x = snum.iloc[:, -1]
y1 = snum.iloc[:, 1]
y2 = snum.iloc[:, 2]
y3 = snum.iloc[:, 3]


# In[126]:


plt.plot(x, y1, label = '서울시 연간 심정지환자 발생 수')
plt.plot(x, y2, label = '서울시 연간 남성 심정지환자 발생 수')
plt.plot(x, y3, label = '서울시 연간 여성 심정지환자 발생 수')
plt.legend()
plt.show()


# In[128]:


sper = seoul.T[2::2]
sper


# In[141]:


ratio = list(sper.iloc[-1, 1:3].astype(float))
labels = list(sper.iloc[0, 1:3])

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()


# In[136]:


list(sper.iloc[-1, 3:].astype(float))


# In[139]:


list(sper.iloc[0, 3:])


# In[140]:


ratio = list(sper.iloc[-1, 3:].astype(float))
labels = list(sper.iloc[0, 3:])

plt.pie(ratio, labels=labels, autopct='%.1f%%')
plt.show()


# In[ ]:




