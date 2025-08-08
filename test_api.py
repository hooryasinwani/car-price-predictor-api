import pytest
import json
from api import app #importing the Flask app object from api.py file

@pytest.fixture
def client():
    """Creating a test client for the Flask app."""
    with app.test_client() as client:
        yield client

def test_predict_endpoint_success(client):
    """
    Testing the /predict endpoint for a successful response.
    GIVEN a Flask application configured for testing
    WHEN a POST request with valid data is made to /predict
    THEN checking that the response is valid, contains the right keys, and is a number.
    """
    #Setting up the data for the test
    test_data = {
        "Brand": "Toyota",
        "Model": "Camry",
        "Year": 2020,
        "Engine_Size": 2.5,
        "Fuel_Type": "Petrol",
        "Transmission": "Automatic",
        "Mileage": 30000,
        "Owner_Count": 1
    }

    #Making the request to the API
    response = client.post('/predict',
                           data=json.dumps(test_data),
                           content_type='application/json')

    #Checking if the response is what we expect
    assert response.status_code == 200
    assert response.content_type == 'application/json'

    response_data = json.loads(response.data)
    assert 'predicted_price' in response_data
    assert isinstance(response_data['predicted_price'], (int, float))


def test_predict_endpoint_bad_data(client):
    """
    Testing the /predict endpoint with incomplete data.
    GIVEN a Flask application configured for testing
    WHEN a POST request with missing data is made to /predict
    THEN checking for a 400 Bad Request response.
    """
  
    test_data = {
        "Brand": "Toyota",
        "Model": "Camry",
        # "Year" is missing
        "Engine_Size": 2.5,
        "Fuel_Type": "Petrol",
        "Transmission": "Automatic",
        "Mileage": 30000,
        "Owner_Count": 1
    }


    response = client.post('/predict',
                           data=json.dumps(test_data),
                           content_type='application/json')

 
    assert response.status_code == 400

def test_predict_endpoint_wrong_method(client):
    """
    Testing the /predict endpoint with a GET request.
    GIVEN a Flask application configured for testing
    WHEN a GET request is made to /predict
    THEN checking for a 405 Method Not Allowed response.
    """

    response = client.get('/predict')

  
    assert response.status_code == 405


    