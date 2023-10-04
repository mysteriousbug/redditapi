import streamlit as st
# Inject custom CSS with animation
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        body {{
            font-family: 'Roboto', sans-serif;
            animation: pulse 5s infinite;
            background-size: 100% 100%;
            background-image: url('https://images.app.goo.gl/bG2QyLPmHfyBnfux5');  # Replace with your image URL
            background-repeat: no-repeat;
        }}
        @keyframes pulse {{
            0% {{
                opacity: 0.7;
            }}
            50% {{
                opacity: 0.5;
            }}
            100% {{
                opacity: 0.7;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
# Title
st.title("Reddit API")

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
