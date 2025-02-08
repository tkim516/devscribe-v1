from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 
        '''# Home Run Predictor Documentation

            ## Overview

            The **Home Run Predictor** is a Streamlit application designed to predict the likelihood of hitting a home run based on various game and player-specific parameters. Utilizing machine learning models, the application allows users to input different launch conditions and see the prediction results alongside relevant game scenarios.

            ## Features

            - **User-Friendly Interface**: A simple and interactive web interface powered by Streamlit.
            - **Multiple Machine Learning Models**: Users can choose between different models (AdaBoost, Random Forest, Decision Tree) for making predictions.
            - **Dynamic Scenario Information**: Displays contextual information about the game, including team names, stadium details, and pitch specifics.
            - **Interactive Inputs**: Users can specify launch speed, angle, and bearing direction to simulate potential home runs.

            ## Prerequisites

            Ensure you have the following dependencies installed:

            ```bash
            pip install streamlit pandas scikit-learn
            ```

            Additionally, ensure that the following CSV files are present in the repository:

            - `train.csv`: Contains game data for training the model.
            - `park_dimensions.csv`: Contains the dimensions of various baseball parks.
            - `ada.pickle`, `dt.pickle`, `rf.pickle`, `xgb.pickle`: Pickled machine learning models that will be loaded for inference.

            ## File Structure

            The main application file is located in:

            ```
            temp_repo/Home.py
            ```

            ## Application Workflow

            1. **Data Loading**: The application begins by loading game and park dimension data from CSV files.
            2. **Data Preprocessing**:
            - Merges relevant datasets and drops unnecessary columns.
            - Encodes categorical variables for model input.
            3. **Model Loading**: Machine learning models are loaded from pickle files.
            4. **User Interaction**: 
            - Users select a model and input launch parameters to predict home run success.
            - The application displays results based on user inputs and current game conditions.

            ## Key Functions

            - `get_encoded_row_from_df(i)`: Retrieves an encoded row from the cleaned DataFrame based on the provided index.
            - `get_scenario_info(i)`: Gathers scenario-specific information from the merged DataFrame for display.

            ## Predictions

            Upon submission of the inputs:
            - The selected model will predict whether a home run will occur and provide a confidence score.
            - Feedback is given through animations and messages indicating success or failure.

            ## Potential Improvements

            1. **Model Performance**: Consider experimenting with additional machine learning models or hyperparameter tuning to improve prediction accuracy.
            2. **User Input Validation**: Implement validation checks for user inputs (e.g., ensuring that launch speed and angle are within reasonable ranges).
            3. **Enhanced Visualization**: Incorporate visual aids, such as graphs showing historical batting performance data or pitch types, to provide users with more context.
            4. **Mobile Responsiveness**: Ensure that the application is optimized for mobile devices to improve accessibility.
            5. **Error Handling**: Add error handling for file loading and data processing to make the application more robust against missing files or incompatible data formats.
            6. **Documentation and Comments**: Improve inline comments and documentation for better understanding of the codebase, especially for complex functions.
            7. **Expand Game Tips**: Provide more detailed game strategies based on statistical analysis, which may help users make more informed decisions.
            8. **Session Management**: Enhance session state management to allow users to track their performance over multiple attempts without losing context.

            ## Conclusion

            The Home Run Predictor application serves as an engaging tool for baseball fans and players alike, offering insights into the potential for hitting home runs based on various input parameters. By implementing the suggested improvements, the application can evolve into a more powerful resource for users interested in baseball analytics."!'''})

if __name__ == '__main__':
    app.run(debug=True)