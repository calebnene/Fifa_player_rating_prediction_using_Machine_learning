import streamlit as st 
import joblib 
from sklearn.preprocessing import StandardScaler
import numpy as np 

# Load the scaler parameters from the file
#players_scaler_params = joblib.load("C:/Users/cnama/Desktop/IIPGH_project/players_scaler_params.joblib")
#goalkeepers_scaler_params = joblib.load("C:/Users/cnama/Desktop/IIPGH_project/goalkeepers_scaler_params.joblib")


# Create a new scaler and set its parameters
new_players_scaler = StandardScaler()
new_goalkeepers_scaler = StandardScaler()

#new_players_scaler.mean_ = players_scaler_params['players_mean']
#new_players_scaler.scale_ = players_scaler_params['players_scale']

#new_goalkeepers_scaler.mean_ = goalkeepers_scaler_params['goalkeepers_mean']
#new_goalkeepers_scaler.scale_ = goalkeepers_scaler_params['goalkeepers_scale']


model_players = joblib.load("players_RandomForest")
model_goalkeepers = joblib.load("goalkeepers_RandomForest")

def predict_goalkeeper(value_eur, wage_eur, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_positioning, goalkeeping_reflexes, goalkeeping_speed):
    scaled_params = new_goalkeepers_scaler.transform([[value_eur, wage_eur, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_positioning, goalkeeping_reflexes, goalkeeping_speed]])
    prediction = model_goalkeepers.predict(scaled_params)
    return prediction

def predict_player(value_eur, wage_eur, shooting, passing, dribbling, average_attacking_ability_features, average_skill_ability_features, average_movement_ability_features, average_power_ability_features, average_mentality_ability_features, average_midfield_ability_features, average_defending_ability_features):
    scaled_params = new_players_scaler.transform([[value_eur, wage_eur, shooting, passing, dribbling, average_attacking_ability_features, average_skill_ability_features, average_movement_ability_features, average_power_ability_features, average_mentality_ability_features, average_midfield_ability_features, average_defending_ability_features]])
    prediction = model_players.predict(scaled_params)
    return prediction


def otherpage():

    st.title('Rating Estimation')
    st.write('-------------------------------------------')
    player_type = st.radio('Select Player Type', ['Goalkeeper', 'Player'])
    st.write('-------------------------------------------')

    if player_type == 'Goalkeeper':
        value_eur = st.number_input('Goalkeepers Value (EUR)', key='value_eur', min_value=0, step=1000)
        wage_eur = st.number_input('Wage (EUR)', key='wage_eur', min_value=0, step=1000)
        goalkeeping_diving = st.slider('Diving Ability', key='goalkeeping diving_ability', min_value=0, max_value=100, value=50)
        goalkeeping_handling = st.slider('Handling Ability', key='goalkeeping handling_ability', min_value=0, max_value=100, value=50)
        goalkeeping_kicking = st.slider('Kicking Ability', key='goalkeeping kicking_ability', min_value=0, max_value=100, value=50)
        goalkeeping_positioning = st.slider('Positioning Ability', key='goalkeeping positioning_ability', min_value=0, max_value=100, value=50)
        goalkeeping_reflexes = st.slider('Reflex Ability', key='goalkeeping reflexes_ability', min_value=0, max_value=100, value=50)
        goalkeeping_speed = st.slider('Speed', key='goalkeeping_speed_ability', min_value=0, max_value=100, value=50)

        if st.button('Predict Rating'):
            prediction = predict_goalkeeper(value_eur, wage_eur, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_positioning, goalkeeping_reflexes, goalkeeping_speed)
            st.markdown(f"<p style='font-size:24px; color:#3498db; font-weight:bold;'>Predicted Goalkeeper Rating: {int(prediction)}</p>", unsafe_allow_html=True)

    else:
        value_eur = st.number_input('Players Value (EUR)', key='value_eur', min_value=0, step=1000)
        wage_eur = st.number_input('Wage (EUR)', key='wage_eur', min_value=0, step=1000)
        shooting = st.slider('Shooting', key='shooting', min_value=0, max_value=100, value=50)
        passing = st.slider('Passing', key='passing', min_value=0, max_value=100, value=50)
        dribbling = st.slider('Dribbling', key='dribbling', min_value=0, max_value=100, value=50)
        average_attacking_ability_features = st.slider('Performance in Forward', key='average_striking_abilities', min_value=0, max_value=100, value=50)
        average_skill_ability_features = st.slider('Skill Rating', key='average_skill_features', min_value=0, max_value=100, value=50)      
        average_movement_ability_features = st.slider('Movement Ability', key='average_movement_features', min_value=0, max_value=100, value=50)
        average_power_ability_features = st.slider('Player Power', key='average_power_features', min_value=0, max_value=100, value=50)
        average_mentality_ability_features = st.slider('Mentality', key='average_mentality_features', min_value=0, max_value=100, value=50)
        average_midfield_ability_features = st.slider('Performance in Midfield', key='average_midfield_abilities', min_value=0, max_value=100, value=50)
        average_defending_ability_features = st.slider('Performance in Defense', key='average_defending_abilities', min_value=0, max_value=100, value=50)       


        if st.button('Predict Rating'):
            prediction = predict_player(value_eur, wage_eur, shooting, passing, dribbling, average_attacking_ability_features, average_skill_ability_features, average_movement_ability_features, average_power_ability_features, average_mentality_ability_features, average_midfield_ability_features, average_defending_ability_features)
            st.markdown(f"<p style='font-size:24px; color:#3498db; font-weight:bold;'>Predicted Player Rating: {int(prediction)}</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    otherpage()
