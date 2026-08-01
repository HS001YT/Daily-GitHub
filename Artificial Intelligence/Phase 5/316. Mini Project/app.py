import os
import joblib
import numpy as np

from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model


# ==========================================================
# Flask App
# ==========================================================

app = Flask(__name__)


# ==========================================================
# Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

OTHER_FILES = os.path.join(
    BASE_DIR,
    "other_files"
)


# ==========================================================
# Load Model
# ==========================================================

MODEL_PATH = os.path.join(
    OTHER_FILES,
    "student_model.keras"
)

model = load_model(
    MODEL_PATH
)

print("Deep Learning Model Loaded")


# ==========================================================
# Load Preprocessor
# ==========================================================

PREPROCESSOR_PATH = os.path.join(
    OTHER_FILES,
    "preprocessor.pkl"
)

preprocessor = joblib.load(
    PREPROCESSOR_PATH
)

print("Preprocessor Loaded")


# ==========================================================
# Home Page
# ==========================================================

@app.route("/")

def home():

    return render_template(
        "index.html"
    )

# ==========================================================
# Prediction
# ==========================================================

@app.route(

    "/predict",

    methods=["POST"]

)

def predict():

    try:

        hours_studied = float(

            request.form["hours_studied"]

        )

        attendance = float(

            request.form["attendance"]

        )

        previous_scores = float(

            request.form["previous_scores"]

        )

        sleep_hours = float(

            request.form["sleep_hours"]

        )

        tutoring_sessions = float(

            request.form["tutoring_sessions"]

        )

        physical_activity = float(

            request.form["physical_activity"]

        )

        internet_access = request.form[

            "internet_access"

        ]

        motivation_level = request.form[

            "motivation_level"

        ]

        teacher_quality = request.form[

            "teacher_quality"

        ]

        family_income = request.form[

            "family_income"

        ]

        parental_involvement = request.form["parental_involvement"]
        access_to_resources = request.form["access_to_resources"]
        extracurricular_activities = request.form["extracurricular_activities"]
        school_type = request.form["school_type"]
        peer_influence = request.form["peer_influence"]
        learning_disabilities = request.form["learning_disabilities"]
        parental_education_level = request.form["parental_education_level"]
        distance_from_home = request.form["distance_from_home"]
        gender = request.form["gender"]

    except Exception:

        return render_template(

            "index.html",

            prediction="Invalid Input"

        )

    import pandas as pd

    input_data = pd.DataFrame(
    [
        {
            "Hours_Studied": hours_studied,
            "Attendance": attendance,
            "Parental_Involvement": request.form["parental_involvement"],
            "Access_to_Resources": request.form["access_to_resources"],
            "Extracurricular_Activities": request.form["extracurricular_activities"],
            "Sleep_Hours": sleep_hours,
            "Previous_Scores": previous_scores,
            "Motivation_Level": motivation_level,
            "Internet_Access": internet_access,
            "Tutoring_Sessions": tutoring_sessions,
            "Family_Income": family_income,
            "Teacher_Quality": teacher_quality,
            "School_Type": request.form["school_type"],
            "Peer_Influence": request.form["peer_influence"],
            "Physical_Activity": physical_activity,
            "Learning_Disabilities": request.form["learning_disabilities"],
            "Parental_Education_Level": request.form["parental_education_level"],
            "Distance_from_Home": request.form["distance_from_home"],
            "Gender": request.form["gender"]
        }
    ]
    )

    processed_data = preprocessor.transform(

        input_data

    )

    prediction = model.predict(

        processed_data,

        verbose=0

    )[0][0]

    prediction = round(

        float(prediction),

        2

    )

    if prediction >= 90:

        performance = "Outstanding"

    elif prediction >= 75:

        performance = "Excellent"

    elif prediction >= 60:

        performance = "Good"

    elif prediction >= 40:

        performance = "Average"

    else:

        performance = "Needs Improvement"

    return render_template(

        "index.html",

        prediction=prediction,

        performance=performance

    )

# ==========================================================
# Run Flask
# ==========================================================

if __name__ == "__main__":

    app.run(

        debug=True

    )
