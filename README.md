# Car Price Prediction API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### About This Project

As a sophomore  CS major at George Mason University , I developed this project to build hands-on experience with the full lifecycle of a machine learning application. My goal was to go beyond a simple script and understand how to properly package, containerize, and deploy a web service. This project demonstrates my journey from a local Python model to a fully functional, cloud-hosted REST API.

---

### Live Demo

The API is live and can be accessed at the following URL:

**[https://car-price-predictor-api-19tt.onrender.com](https://car-price-predictor-api-19tt.onrender.com)**

---

### Features

* RESTful API endpoint for real-time price predictions.
* Built with a Linear Regression model trained using Scikit-learn.
* Containerized with Docker for consistent, reproducible deployments.
* Deployed on the cloud via Render.

---

### Tech Stack

* **Backend:** Python, Flask
* **Data Science:** Pandas, Scikit-learn
* **Containerization:** Docker
* **Deployment:** Render

---

### Local Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/hooryasinwanix/car-price-predictor-api.git](https://github.com/hooryasinwanix/car-price-predictor-api.git)
    cd car-price-predictor-api
    ```

2.  **Set up a virtual environment (recommended):**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```sh
    python api.py
    ```
    The application will be running at `http://127.0.0.1:5001`.

---

### API Usage

The API has a single endpoint for predictions.

#### POST /predict

Send a `POST` request to this endpoint with a JSON payload containing the car's features to receive a price prediction.

**Example using `curl`:**

1.  Create a `payload.json` file:
    ```json
    {
        "Brand": "Toyota",
        "Model": "Camry",
        "Year": 2020,
        "Engine_Size": 2.5,
        "Fuel_Type": "Petrol",
        "Transmission": "Automatic",
        "Mileage": 30000,
        "Owner_Count": 1
    }
    ```

2.  Send the request:
    ```sh
    curl -X POST [http://127.0.0.1:5001/predict](http://127.0.0.1:5001/predict) \
    -H "Content-Type: application/json" \
    -d @payload.json
    ```

**Expected Response:**

```json
{
  "predicted_price": 13442.63
}
