"# T20-Cricket-Score-Predictor"
Cricket Score Predictor
This project is a web application developed using Streamlit and Python, aimed at predicting cricket scores in real-time based on various input parameters such as batting team, bowling team, current score, overs done, wickets out, runs scored in the last 5 overs, and city where the match is played.

Features:
Input Selection: Users can select the batting team, bowling team, city where the match is being played, current score, overs done, wickets out, and runs scored in the last 5 overs.
Prediction: Upon selecting the input parameters and clicking the "Predict Score" button, the application predicts the expected score for the given match.
Dynamic Calculation: The predicted score is dynamically calculated based on the selected input parameters, taking into account the number of balls left, wickets left, and the current run rate.
Technologies Used:
Python: The backend logic of the application is written in Python, utilizing libraries such as Pandas, NumPy, and Scikit-learn for data manipulation and machine learning.
Streamlit: Streamlit is used to create the web application interface, allowing users to interactively input parameters and view the predicted scores.
XGBoost: The XGBoost machine learning algorithm is used to train the predictive model, which is then loaded into the application for real-time predictions.
Pickle: The trained model is serialized and stored using Pickle, allowing it to be loaded efficiently within the application.
Installation:
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run the application using streamlit run app.py.
Usage:
Select the desired input parameters from the dropdown menus and input fields.
Click the "Predict Score" button to view the predicted score for the match.
Feel free to contribute to the project by suggesting improvements, reporting bugs, or adding new features!
