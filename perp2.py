import streamlit as st
import requests

# Streamlit app title
st.title('API Request Interface')

# Hardcoded API key (ensure it's correct and valid)
api_key = "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"

# Input field for the user to enter the query
query = st.text_area('Enter your query', "Please answers the questions below, thinking step by step:

QUESTIONS:
Question 1:  verify that each part of the citation provided below is (i) accurate and  (ii) complete  (e.g., it provides all the necessary elements required for a legal citation).

Question 2: Is the citation below formatted correctly according to the applicable Bluebook citation system (21st Edition) rules ? 

Question 3: Does this case, actually exist based on its availability from a reliable source? If yes, provide a summary of the case.

CITATION: City of New York v. 330 Continental, 60 A.D.3d 226 (N.Y. App. Div. 2008)?")

# Button to send the request
if st.button('Send Request'):
    if query:
        url = "https://api.perplexity.ai/chat/completions"

        payload = {
            "model": "mistral-7b-instruct",  # Adjusted model based on your successful request
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
            "authorization": f"Bearer {api_key}"
        }

        try:
            # Make the POST request to the API
            response = requests.post(url, json=payload, headers=headers)

            # Display the response
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error(f"Failed to fetch data: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error('Please enter a query.')

