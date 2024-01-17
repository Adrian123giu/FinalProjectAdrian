from flask import Flask, jsonify
import requests
import pytest


class EndpointTester:
    def __init__(self, endpoint, base_url="https://jsonplaceholder.typicode.com"):
        self.endpoint = endpoint
        self.base_url = base_url

    @pytest.mark.parametrize("param_name, expected_status",
                             [("posts", 200), ("comments", 200), ("todos", 200), ("users", 200)])
    def test(self, param_name, expected_status):
        response = requests.get(f"{self.base_url}{self.endpoint}")

        assert response.status_code == expected_status, f"Failed to fetch data from {self.base_url}{self.endpoint}. Status code: {response.status_code}"

        data = response.json()

        assert len(data) > 0, f"No data received from {self.base_url}{self.endpoint}"
        return data


class APITestingApp:
    def __init__(self):
        self.app = Flask(__name__)

        self.BASE_URL = "https://jsonplaceholder.typicode.com"

        self.ENDPOINTS = ["/posts", "/comments", "/todos", "/users"]

        for endpoint in self.ENDPOINTS:
            tester = EndpointTester(endpoint, self.BASE_URL)
            self.app.add_url_rule(endpoint, f"endpoint_{endpoint}",
                                  view_func=lambda tester='tester': self.test_endpoint(tester))

            self.app.add_url_rule('/', 'index', self.index)

    def index(self):
        return "API Testing Script using Flask with Python"

    def test_endpoint(self, tester):
        data = tester.test("posts", 200)
        return jsonify(data)

    def run(self):
        # Run the Flask app on http://127.0.0.1:5000/
        self.app.run(debug=False)


if __name__ == '__main__':
    api_testing_app = APITestingApp()
    api_testing_app.run()
    # Run the tests and generate an HTML report
    pytest.main(['-v', '--html=report.html'])

# http://127.0.0.1:5000/posts
# http://127.0.0.1:5000/comments
# http://127.0.0.1:5000/todos
# http://127.0.0.1:5000/users