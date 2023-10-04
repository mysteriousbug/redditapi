import streamlit as st

# Title
st.title("Product Explanation Form")

# Text box for product paragraph
product_paragraph = st.text_area("Product Paragraph")

# Text box
additional_text = st.text_area("Additional Text (Optional)")

# Button
if st.button("Start Job"):
    # You can place your job logic here
    st.text("Job Started...")

    # Simulate a job with progress
    import time
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.1)
        progress_bar.progress(i)

    st.text("Job Completed!")

# This will display any comments or outputs from your job
st.text("Comments:")

# Display comments here (replace with your actual comments)
st.text("Comment 1")
st.text("Comment 2")
