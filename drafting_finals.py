import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
    
