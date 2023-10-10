import streamlit as st
import json
import requests  

# CSS code
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        body {{
            font-family: 'Roboto', sans-serif;
            animation: pulse 5s infinite;
        }}
        .custom-text-box {{
            height: 100px; /* Adjust the height as needed */
        }}
        .output-box {{
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
        }}
        
    </style>
    """,
    unsafe_allow_html=True,
)

data = {
    "comment1": {
        "comment_text": "This is the first comment",
        "post": "Post 1",
        "url": "URL 1"
    },
    "comment2": {
        "comment_text": "This is the second comment",
        "post": "Post 2",
        "url": "URL 2"
    },
    "comment3": {
        "comment_text": "This is the third comment",
        "post": "Post 3",
        "url": "URL 3"
    }
}


# Title
st.title("Reddit API")

# Text box for product description
product_description = st.text_area("Product Description", key="product_desc")

# Text box for subreddit URL(s)
subreddit_urls = st.text_area("Subreddit URL(s)", key="subreddit_urls")

# Text box for subreddit(s) to ignore
ignore_subreddits = st.text_area("Subreddit(s) to Ignore", key="ignore_subreddits")

# Integer input for the number of posts to scrape per subreddit
num_posts_to_scrape = st.number_input("Number of Posts to Scrape per Subreddit", min_value=1, step=1, key="num_posts")

# Integer/Float input the epoch time, in seconds
time_cutoff_seconds = st.number_input("Epoch Time (in seconds)", min_value=0.0, key="time_cutoff_seconds")

# Button
if st.button("Run Code"):
    
    st.text("Fetching Comments...")

    # Simulate a job with progress
    import time
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)

    d = momo()

    st.text("Results Ready!")

    for comment_key, comment_data in data.items():
    comment_text = comment_data.get("comment_text", "N/A")
    post = comment_data.get("post", "N/A")
    url = comment_data.get("url", "N/A")

    # Display values in the HTML div
    st.markdown(f"<div class='output-box'>Comment: {comment_text} <br>Post: {post} <br>URL: {url}</div>", unsafe_allow_html=True)
