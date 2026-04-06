import streamlit as st

# App Title
st.set_page_config(page_title="PaaS Demo App", layout="centered")

st.title("🚀 Platform as a Service Demo")
st.write("This application is deployed using a PaaS platform (Streamlit Cloud).")

# Input Section
st.subheader("User Interaction Module")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)

# Processing Logic
if st.button("Generate Response"):
    if name:
        st.success(f"Hello {name}! You are {age} years old.")
        st.info("This response is generated from a cloud-hosted PaaS application.")
    else:
        st.warning("Please enter your name.")

# Additional Feature (to look more real)
st.subheader("Upload a File")
uploaded_file = st.file_uploader("Upload any file")

if uploaded_file:
    st.write("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")