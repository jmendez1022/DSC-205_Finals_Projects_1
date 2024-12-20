import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import folium
st.title('Student Loans Deliquency and Defaults')
st.markdown('---')

st.header('Amount of Debt to # of Borrowers')

link_2 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4ltcLM-PwQcunJBA-rPGY5f_GLi5eZVi8PS6n-lpjMqdSSWnJVu7UVCpvNDVzG-FVMdPh8earJpt1/pub?output=csv"
data_3 = pd.read_csv(link_2)

x = data_3['Year']
y1 = data_3['Debt (In trillions)']
y2 = data_3['Federal_Student_Borrowers_In hundred Millions']


fig, ax = plt.subplots()

ax.plot(x, y1, marker='o', color='green', label='Debt In trillions')
ax.plot(x, y2, marker='o', color='red', label = "# of Borrowers In Hundred Millions")


ax.set_xlabel('Years')
ax.set_ylabel('Values')
ax.set_title('Number of Debt to Student Borrowers')

ax.legend()

st.pyplot(fig)

st.markdown('---')
st.header('Student Loan Deliquency Rate by State')
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSNe3p3E6MOF-F2uzAucnPmOaYJsH9iBTa7NXrbSSvIbZj4LEo5v5NboBT_14sbrsrNRnwPIRPZLcQ7/pub?output=csv"

df = pd.read_csv(URL)
df.columns = df.columns.str.strip()

print(df.columns)  

geo_url = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
state_geo = f"{geo_url}/us-states.json"

m = folium.Map(location=[40, -95], zoom_start=4)

choro = folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=df,
    columns=["State", "Delinquency_percentage_rate"],
    key_on="feature.properties.name",
    fill_color="YlGn",  
    fill_opacity=0.7,
    line_opacity=0.2,
    line_color='white',  
    legend_name="Delinquency Percentage",
)
choro.add_to(m)

tooltip = 'Click me'
for index, row in df.iterrows():
    folium.Marker(
        location=[row['lat'], row['long']], 
        popup=f"{row['State']}, {row['Delinquency_percentage_rate']}%", 
        tooltip=tooltip
    ).add_to(m)

m.save("choropleth_map.html")
st.components.v1.html(open("choropleth_map.html", "r").read(), height=600)

st.markdown('---')

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFMvS6Jrqn7g_S6x1-O7ADC5vapKdcd_LEeccS6GGPCNm-MI3kVOw9EzR2ehd22PPaJ-VPHozhkJsd/pub?output=csv"
data = pd.read_csv(url)
st.title("Student Loan Default Rate by Institution")

fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.set_xlabel('Years')
ax1.set_ylabel('Percentage')
ax1.set_title('Public College Default Rate')
ax1.hist(data['Year'], bins=20, weights=data["Public "], color='red', alpha=0.5)

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.set_xlabel('Years')
ax2.set_ylabel('Percentage')
ax2.set_title('Private Non Profit College Default Rate')
ax2.hist(data['Year'], bins=20, weights=data["Private_Non_Profit"], color='blue', alpha=0.5)


fig3 = plt.figure()
ax3 = fig3.add_subplot()
ax3.set_xlabel('Years')
ax3.set_ylabel('Percentage')
ax3.set_title('Private For Profit College Default Rate')
ax3.hist(data['Year'], bins=20, weights=data["Private_for_profit"], color='green', alpha=0.5)


tab1, tab2, tab3 = st.tabs(["Public Defualt %", "Private Non-Profit Defualt %", "Private For Profit Defualt %"])

with tab1:
   st.pyplot(fig1)

with tab2:
   st.pyplot(fig2)

with tab3:
    st.pyplot(fig3)

st.markdown('---')

st.title('Amount of Defaults by Ethnicity')

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRFc5Pj4yRcauW4U2TGtKsS3IGtMKqVzoqDnG1wv0ZwtLE9gvm91n46Y6hfVWRy7Oo30qnjtxeQdyFU/pub?output=csv')
df.columns = df.columns.str.strip()

st.write("Unique values in Race/Ethnicity column:", df['Race/Ethncity'].unique())


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Defaults by Race')
st.dataframe(df, width=600, height=200)

selected = st.radio('Select Ethnicity', df['Race/Ethncity'].unique())


filtered_df = df[df['Race/Ethncity'] == selected]



st.write("Average default rate:", filtered_df['Defaulted'].mean())

fig, ax = plt.subplots(figsize=(10, 6))


ax.bar(selected, filtered_df['Defaulted'])
ax.set_xlabel('Race/Ethnicity')
ax.set_ylabel('Default Rate (%)')
ax.set_title(f'Default Rate for {selected}')


ax.set_ylim(0, 25)


st.pyplot(fig)














