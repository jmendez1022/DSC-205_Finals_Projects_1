import pandas as pd
import folium
import streamlit as st

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSNe3p3E6MOF-F2uzAucnPmOaYJsH9iBTa7NXrbSSvIbZj4LEo5v5NboBT_14sbrsrNRnwPIRPZLcQ7/pub?output=csv"
df = pd.read_csv(URL)

df.columns = df.columns.str.strip()


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
    line_opacity=0.1,
    legend_name="Delinquency Percentage",
)
choro.add_to(m)


tooltip = 'Click me'
for index, row in df.iterrows():
    folium.Marker(location=[row['lat'], row['long']], 
                  popup=f"{row['State']},{['Delinquency_percentage_rate']}%", 
                  tooltip=tooltip).add_to(m)


m.save("choropleth_map.html")


st.components.v1.html(open("choropleth_map.html", "r").read(), height=600)
