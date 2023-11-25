import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

# Reading the training dataset
goalkeepers = pd.read_csv("C:/Users/cnama/Desktop/IIPGH_project/goalkeepers.csv")
players = pd.read_csv("C:/Users/cnama/Desktop/IIPGH_project/players.csv")

def main():

    st.set_page_config(
        page_title='FIFA Player Ratings Estimator',
        page_icon='⚽',
        layout='wide'
    )

    # Header
    st.title('FIFA PLAYER RATINGS :soccer:')

    # Add some space for aesthetics
    st.write('')

    # Sidebar with a success alert
    st.sidebar.success('Select a page')

    # Main content
    st.write('Welcome to the FIFA Player Ratings Estimator!')

    st.write("This website is designed to help estimate a player's overall rating based on the RandomForest Algorithm:")

    st.subheader('Dataset used for training the model \nAbout the dataset:')

    st.markdown('The original raw dataset was obtained from (https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset?select=players_21.csv)')

    st.write('The data was cleaned and EDA was performed. The initial dataset was then split into one for Goalkeepers and Players to make training the model easier.')
    

    # View Goalkeeper Dataset
    gdataset = st.selectbox('View Goalkeeper Dataset', ['Select one view option', 'Tabular Form', 'Visual Form'])

    if gdataset == 'Tabular Form':
        st.write('A part of the dataset:')
        st.table(goalkeepers.head())
        st.write('Some Analysis on the dataset:')
        st.table(goalkeepers.describe())

    elif gdataset == 'Visual Form': 
        # Goalkeepers plot
        num_bins_goalkeepers = st.slider('Number of Bins for Goalkeepers Histogram', min_value=5, max_value=50, value=20)

        fig1, ax1 = plt.subplots(figsize=(8, 4))  # Adjust width and height as needed
        goalkeepers['overall'].plot(kind='hist', ax=ax1, bins=num_bins_goalkeepers)
        ax1.set_xlabel('Overall Rating')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Goalkeepers Overall Ratings Distribution')

        # Display the Goalkeepers plot
        st.pyplot(fig1)
        plt.show()

    # View Player Dataset
    pdataset = st.selectbox('View Player Dataset', ['Select one view option', 'Tabular Form', 'Visual Form'])

    if pdataset == 'Tabular Form':
        st.write('A part of the dataset:')
        st.table(players.head())
        st.write('Some Analysis on the dataset:')
        st.table(players.describe())

    elif pdataset == 'Visual Form': 
        num_bins_players = st.slider('Number of Bins for Players Histogram', min_value=5, max_value=50, value=20)

        # Players plot
        fig2, ax2 = plt.subplots(figsize=(8, 4))  # Adjust width and height as needed
        players['overall'].plot(kind='hist', ax=ax2, bins=num_bins_players)
        ax2.set_xlabel('Overall Rating')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Players Overall Ratings Distribution')

        # Display the Players plot
        st.pyplot(fig2)
        plt.show()

    # Footer with a custom background color
    st.markdown(
        """
        <style>
            footer {
                background-color: #3498db;
                padding: 10px;
                color: white;
                text-align: center;
                font-size: 14px;
            }
        </style>
        <footer>
            Made by <strong>Caleb Martey</strong>
        </footer>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
