import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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



