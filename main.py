import streamlit as st
import random

st.set_page_config(layout='wide')
st.session_state['team1'] = []
st.session_state['team2'] = []
st.session_state['team3'] = []
st.session_state['team4'] = []

players = [
            'Samantha',
            'Matt (Director)',
            'Miles',
            'Sarah',
            'Jamie',
            'Rallou',
            'Dee',
            'Elkana',
            'Grace',
            'Josh',
            'George',
            'Matt H',
            'Dyon',
            'Alex',
            'Jasdeep',
            'Jacque',
            'Marcus',
            'Lyle',
            'Georgia',
            'Jess',
            'Sharron',
            'Jay',
            'Charley',
            'Krishn',
            'Eileen',
            'Julian'
        ]

not_here = st.multiselect('Anyone not here?', options=players)
if not_here:
    for _ in not_here:
        players.remove(_)

random.shuffle(players)
make_teams = st.button('Make teams!')

j_index = players.index('Julian')
players.insert(0, players.pop(j_index))
e_index = players.index('Eileen')
players.insert(1, players.pop(e_index))
s_index = players.index('Samantha')
players.insert(2, players.pop(s_index))

def chunks(l, n):
    results = {}
    for i in range(0, n):
        results[i] = l[i::n]
    return results
        
results = chunks(players, 4)
team1 = results[0]
random.shuffle(team1)
team2 = results[1]
random.shuffle(team2)
team3 = results[2]
random.shuffle(team3)
team4 = results[3]
random.shuffle(team4)
col1, col2, col3, col4 = st.columns([1,1,1,1])
col1.write('Team 1')
col2.write('Team 2')
col3.write('Team 3')
col4.write('Team 4')

import time

def show_player_index(index):
    try:
        with col1:
            st.write(team1[index])
        with col2:
            st.write(team2[index])
        with col3:
            st.write(team3[index])
        with col4:
            st.write(team4[index])
    except:
        pass
if make_teams:
    for _ in range(len(team1)):
        show_player_index(_)
        st.balloons()
        time.sleep(5)
        