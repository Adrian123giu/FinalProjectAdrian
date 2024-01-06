from flask import Flask, jsonify
import requests

class EndpointTester:
    def __init__(self, endpoint, base_url="https://jsonplaceholder.typicode.com"):
        self.endpoint = endpoint
        self.base_url = base_url

    def test(self):
        # Make a GET request to the API
        response = requests.get(f"{self.base_url}{self.endpoint}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            # If the request was not successful, return an error message
            return {"error": f"Failed to fetch data from {self.base_url}{self.endpoint}", "status_code": response.status_code}

class APITestingApp:
    def __init__(self):
        self.app = Flask(__name__)

        # Define the base URL of the API
        self.BASE_URL = "https://jsonplaceholder.typicode.com"

        # Define the endpoints you want to test
        self.ENDPOINTS = ["/posts", "/comments", "/todos", "/users"]

        # Dynamically add routes for each endpoint
        for endpoint in self.ENDPOINTS:
            tester = EndpointTester(endpoint, self.BASE_URL)
            self.app.add_url_rule(endpoint, endpoint.replace('/', '_')[1:], lambda t=tester: self.test_endpoint(t))

    def index(self):
        return "API Testing Script using Flask with Python"

    def test_endpoint(self, tester):
        data = tester.test()
        return jsonify(data)

    def run(self):
        # Run the Flask app on http://127.0.0.1:5000/
        self.app.run(debug=True)

if __name__ == '__main__':
    api_testing_app = APITestingApp()
    api_testing_app.run()

# http://127.0.0.1:5000/posts
# http://127.0.0.1:5000/comments
# http://127.0.0.1:5000/todos
# http://127.0.0.1:5000/users