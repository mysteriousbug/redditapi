import streamlit as st
# Inject custom CSS with animation
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url("https://github.com/mysteriousbug/redditapi/blob/main/backgroundimg.png");  # You can also use an image as a background
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
# Title
st.title("Reddit API")

# Text box for product paragraph
product_paragraph = st.text_area("Subreddit URL")

# Text box
additional_text = st.text_area("Additional Text (Optional)")

# Button
if st.button("Run Code"):
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
