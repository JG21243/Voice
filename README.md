# **perp3.py**

This is a simple Streamlit application that allows users to query a galaxy database using natural language. The application sends the user's query to an API endpoint and displays the response.

## **How to Use**

1. Run the Streamlit application.
2. Enter your query in the text area. For example, "How many stars are there in our galaxy?".
3. Click the 'Send Query' button to send the request.

## **Code Overview**

The application uses the Streamlit library for the user interface and the requests library to send HTTP requests.

The user's query is sent to the `https://api.perplexity.ai/chat/completions` endpoint with a POST request. The request includes a JSON payload that contains the user's query and some additional information.

If the request is successful (HTTP status code 200), the response from the server is displayed in the Streamlit application. If the request fails, an error message is displayed.

## **Requirements**

- Python 3.6 or higher
- Streamlit
- requests

## Installation

To install the required libraries, use the terminal to run the following command:
```bash
pip install streamlit requests
```

To run the application, use the following command:
```bash
streamlit run perp3.py
```

## **Note**

Please ensure you have the necessary permissions and API keys to access the `https://api.perplexity.ai/chat/completions` endpoint.