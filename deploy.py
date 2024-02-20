import streamlit as st
from scripts.prediction import make_prediction
from scripts.data import clean_text

def main():
    st.title("Customer Support Bot")

    # Initialize the chat history
    if "message" not in st.session_state:
        st.session_state.message = []

    # Display chat history from the session history
    for message in st.session_state.message:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    if query := st.chat_input("Ask something"):
        with st.chat_message('user'):
            st.markdown(query)
        st.session_state.message.append({'role': 'user', 'content': query})

        response = make_prediction(query)
        with st.chat_message('assistant'):
            st.markdown(response)
        st.session_state.message.append({'role': 'assistant', 'content': response})


if __name__=="__main__":
    main()