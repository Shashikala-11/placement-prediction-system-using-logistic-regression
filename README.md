# Placement Predictor

A lightweight Flask app that predicts student placement (Placed / Not Placed) using a trained Logistic Regression model. This repository contains the model, a simple web UI, and an API endpoint for making predictions.

## Features

- Web UI to enter CGPA and IQ and receive a placement prediction.
- Predict endpoint (`/predict`) accepts form submissions.
- Model persisted as `model/model.pkl` so the app can be served without retraining.

## Demo Video Link

- YouTube: https://youtu.be/C1y1yUthcWE?si=x6Lxy4_LGaVRG3gG

## Files

- `app.py` — Flask application and prediction route.
- `templates/index.html` — HTML form and result display.
- `static/styles.css` — Stylesheet for the UI.
- `model/model.pkl` — Saved trained model used for predictions.
- `placement.csv` — Dataset used for training (if present).
- `requirements.txt` — Python dependencies for the project.

## Requirements

Install dependencies into a virtual environment. Example packages are listed in `requirements.txt`.

## Setup (local)

1. Create and activate a virtual environment (Windows example):

```powershell
python -m venv myenv
myenv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Flask app:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Usage

- Web UI: Open `http://127.0.0.1:5000/` and submit `CGPA` and `IQ` values.
- Programmatic (curl) example using form data:

```bash
curl -X POST http://127.0.0.1:5000/predict -d "cgpa=8.2&iq=110"
```

The response will render the UI with a success or error message showing the prediction.

## Notes

- Model file is expected at `model/model.pkl`. Replace it if you retrain.
- The project uses a simple logistic regression model and a two-feature input `[cgpa, iq]`.

## Credits

Created as a compact demo to showcase a model deployment with Flask.

---

If you'd like, I can add a quick `README` badge, example screenshots, or a Dockerfile next.
