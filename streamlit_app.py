from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pypsa
import numpy as np

"""
# Welcome to Network Crunsher!

Edit your network below!
"""




with st.sidebar:
    b_gen = st.button('Generators')
    b_lines = st.button('Lines')
    b_bla = st.button('bla')
    b_download = st.button('Download Network')

if 'menu' not in globals():
    menu = 'Download'
if b_gen:
    menu = 'Generators'
if b_lines:
    menu = 'Lines'
if b_bla:
    menu = 'Bla'
if b_download:
    menu = 'Download'

@st.cache()
def create_network():
    n = pypsa.Network()
    
    n.add('Bus', 'bus')
    for i in range(10):
        n.add('Generator', bus='bus', name='my_gen_'+str(i), p_nom = np.random.rand()*200+50, p_min_pu=np.random.rand()*0.5, p_max_pu = 1-np.random.rand()*0.1, carrier=['wind', 'PV', 'hydro', 'gas', 'coal'][np.random.randint(0,5)])
    return n

n = create_network()


st.text('#This is Menu '+menu)

if menu == 'Generators':
    st.dataframe(n.generators)
    selected_gen = st.selectbox('Select generator to change', n.generators.index.tolist())

    if selected_gen is not None:
        gen = n.generators.loc[selected_gen, :]
        st.number_input('p_nom', value=gen.p_nom)
        st.number_input('p_min_pu', value=gen.p_nom)
        st.number_input('p_max_pu', value=gen.p_nom)

        st.button('Submit')
    
elif menu == 'Download':
    pass
    #st.download_button('Download Network', data=n)



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
