import streamlit as st

st.set_page_config(page_title="Deployment Demo", page_icon="🚀")

st.title("Simple Streamlit App for Deployment 🚀")

st.write("This is a basic app designed to demonstrate deployment workflows.")

st.info("If you see this, the app is running successfully!")

if st.button("Click me!"):
    st.balloons()
