from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pypsa
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


n = pypsa.Network()
st.text(n)

with st.sidebar:
    menu = st.button('Generators')
    menu = st.button('Lines')
    menu = st.button('bla')
    menu = st.button('Download Network')

if menu is None:
    menu = 'Generators'


for i in range(10):
    n.add('Generator', name='my_gen_'+str(i), p_nom = np.random.rand()*200+50, p_min_pu=np.random.rand()*0.5, p_max_pu = 1-np.random.rand()*0.1, carrier=['wind', 'PV', 'hydro', 'gas', 'coal'][np.random.randint(0,5)])

st.text(menu)
if menu == 'Generators':
    st.dataframe(n.generators)
    selected_gen = st.selectbox('Select generator to change', n.geneartors.index.tolist())

    if selected_gen is not None:
        gen = n.generators.loc[selected_gen, :]
        st.number_input('p_nom', value=gen.p_nom)
        st.number_input('p_min_pu', value=gen.p_nom)
        st.number_input('p_max_pu', value=gen.p_nom)

        st.button('Submit')
    
        



if False:
    with st.echo(code_location='below'):
        total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
        num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

        Point = namedtuple('Point', 'x y')
        data = []

        points_per_turn = total_points / num_turns

        for curr_point_num in range(total_points):
            curr_turn, i = divmod(curr_point_num, points_per_turn)
            angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
            radius = curr_point_num / total_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            data.append(Point(x, y))

        st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
            .mark_circle(color='#0068c9', opacity=0.5)
            .encode(x='x:Q', y='y:Q'))
