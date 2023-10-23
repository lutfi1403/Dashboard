# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# %%
day=pd.read_csv("Day_New.csv")

# %%
hour=pd.read_csv("Hour_New.csv")

# %%
st.title('Trend Penyewaan Sepeda')

# %%
with st.sidebar:
   st.header('Dashbord Bike Sharing Dataset')
   st.image("https://drive.google.com/drive/folders/1LTrlFz1dtDf8vtEs1foMkbb90Vr-x6kg/Logo.png")
   
# %%
st.subheader('Distribusi Perhitungan Berdasarkan jam Pada Hari kerja')


f,ax = plt.subplots(figsize=(16, 8))
sns.pointplot(data=hour[['hr',
                           'cnt',
                           'workingday']],
              x='hr',
              y='cnt',
              hue='workingday',
                 ax=ax)  
st.pyplot(f)

# %%
st.subheader('Distribusi Perhitungan Berdasarkan jam Pada Hari Libur')


f,ax = plt.subplots(figsize=(16, 8))
sns.pointplot(data=hour[['hr',
                           'cnt',
                           'holiday']],
              x='hr',
              y='cnt',
              hue='holiday',
                 ax=ax)  
st.pyplot(f)

# %%
st.subheader('Distribusi Perhitungan Jam Berdasarkan Musim')


f,ax = plt.subplots(figsize=(16, 8))
sns.pointplot(data=hour[['hr',
                           'cnt',
                           'season']],
              x='hr',
              y='cnt',
              hue='season',
                 ax=ax)  
st.pyplot(f)
# %%
st.text('''Dari hasil Exploratory Data dan visualisasi dapat kita simpulkan bahwa trend penyewaan 
sepeda setiap jam berdasarkan musim terbanyak itu pada pukul 08.00 dan 17.00 kemudian 
penyewaan tersedikit yakni PUKUL 04.00 dan 23.00, kemudian untuk penyewaan sepeda pada 
hari akhir pekan atau bukan hari libur itu terbanyak pada pukul 08.00 dan 17.00. sedangkan 
pada hari bukan akhir pekan atau hari libur lebih tinggi penyewaanya pada pukul 08.00 
dan penyewaan pada hari akhir pekan atau bukan hari libur itu lebih konstant''')