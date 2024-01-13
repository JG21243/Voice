import streamlit as st
import requests

def query_galaxy_interface():
    """
    Function to display a Streamlit app for querying the galaxy.

    Returns:
        None
    """
    # Streamlit app title
    st.title('Galaxy Query Interface')

    # Input field for the user to enter the query
    query = st.text_area('Enter your query', "Please answers the questions below, thinking step by step:")
    # Add a newline after each question
    QUESTIONS = """
    Question 1:  verify that each part of the citation provided below is (i) accurate and  (ii) complete  (e.g., it provides all the necessary elements required for a legal citation).

    Question 2: Is the citation below formatted correctly according to the applicable Bluebook citation system (21st Edition) rules ? 

    Question 3: Does this case, actually exist based on its availability from a reliable source? If yes, provide a summary of the case.

    CITATION: City of New York v. 330 Continental, 60 A.D.3d 226 (N.Y. App. Div. 2008)?
    """
    citation = ""  # Define the "citation" variable with an empty string

    # Button to send the request
    if st.button('Send Query'):
        process_query(query)

def process_query(query):
    """
    Process the given query by sending a request to an API and displaying the response.

    Args:
        query (str): The query to be sent to the API.

    Returns:
        None
    """
    if query:
        response = send_request_to_api(query)
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
    else:
        st.error('Please enter a query.')


def send_request_to_api(query):
    """
    Sends a request to the Perplexity API to get completions for a given query.

    Args:
        query (str): The user's query.

    Returns:
        requests.Response: The response object containing the API response.
    """
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "pplx-70b-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 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"
    }

    return requests.post(url, json=payload, headers=headers, timeout=40)

# Run the app
query_galaxy_interface()
