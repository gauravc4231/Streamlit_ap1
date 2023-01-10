import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.text("Welcome to Streamlit")


df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(df)

st.bar_chart(df)

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)