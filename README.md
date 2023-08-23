# Rate Limiter and Test Documentation

## Introduction
"MyProject" is a Django-based web application designed to demonstrate a rate limiter and a test runner. This documentation provides a comprehensive guide to understanding and using the application.

### Rate Limiter
The rate limiter ensures that a user (identified by their IP address) can't make more than a certain number of requests in a given time period. If a user exceeds this limit, they receive a "Rate limit exceeded" response.

#### Endpoints:
```/rate-limiter-demo/: A demo endpoint that returns a simple JSON response. This endpoint is rate-limited.```
### Test Runner
The test runner allows users to run tests for the application directly from the web interface.
#### Endpoints:
```/run-tests/: A page with a button that, when pressed, runs the tests for the application and displays the results.```

## Setup and Installation
1. Clone the repository: ```git clone [repository_url]```
2. Navigate to the project directory: ```cd myproject```
3. Set up a virtual environment: ```python -m venv myenv```
4. Activate the virtual environment:
    - Windows: ```myenv\Scripts\activate```
    - macOS/Linux: ```source myenv/bin/activate```
5. Install the required packages: ```pip install -r requirements.txt```

## Running the Application
1. Ensure you're in the project directory and the virtual environment is activated.
2. Run the server: ```python manage.py runserver```
3. Open a browser and navigate to http://127.0.0.1:8000/

## Tests
The application comes with tests to ensure the rate limiter's functionality.

- To run the tests, navigate to /run-tests/ in your web browser and click the "Run Tests" button.
- Test results will be displayed on the same page.