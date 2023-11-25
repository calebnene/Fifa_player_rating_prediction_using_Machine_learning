# FIFA Player Ratings Estimation

This project consists of three main parts:
1. **Data Exploration and Analysis**
2. **Model Training**
3. **Streamlit App for Prediction**

## Part 1: Data Exploration and Analysis

EDA was performed on the raw dataset 'players_21.csv'. 
The jupyter notebook file where EDA and model training was done is 'player_rating.ipynb'
The cleaned dataset above was split into the goalkeepers and players datasets - 
'goalkeepers.csv' and 'players.csv' respectively. 

## Part 2: Model Training

The goalkeepers and players dataset were both trained using 3 different algorithms; Naive Bayes, Random Forest and Linear Regression algorithms.
The best model was Random Forest so that was saved under 'goalkeepers_RandomForest' and 'players_RandomForest' for the goalkeepers and players datasets respectvely and used for predictions. 
Since the features were scaled, the scaled parameters were also saved in order to be used during deployment. The files are 'goalkeepers_scaler_params.joblib' and 'players_scaler_params.joblib'

## Part 3: Streamlit App for Prediction
The streamlit app is multipage app consisting of the homepage and estimate ratings page both under the multipage_app folder.
Run the homepage.py file in your terminal using streamlit run. 

## Dependencies

- Python 3.7+
- Required Python packages (specified in `requirements.txt`)

## Getting Started

- Clone the repository: `git clone https://github.com/your-username/your-repository.git`
- Install dependencies: `pip install -r requirements.txt`
- Run the Streamlit app: `streamlit run Part3_Streamlit/app.py`

## Author

- Caleb Martey

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

