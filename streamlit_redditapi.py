import streamlit as st
import json
import requests  # pip install requests

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
        
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("Reddit API")

# Text box for product description
product_description = st.text_area("Product Description", key="product_desc")

# Text box for subreddit URL(s)
subreddit_urls = st.text_area("Subreddit URL(s)", key="subreddit_urls")

# Integer input for the number of posts to scrape per subreddit
num_posts_to_scrape = st.number_input("Number of Posts to Scrape per Subreddit", min_value=1, step=1, key="num_posts")

# Button
if st.button("Run Code"):
    
    st.text("Fetching Comments...")

    # Simulate a job with progress
    import time
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(1)
        progress_bar.progress(i)

    st.text("Results Ready!")

    comments_data = [
        ["Post Title 1", "Comment 1", "URL 1"],
        ["Post Title 2", "Comment 2", "URL 2"]
    ]

    for comment_info in comments_data:
        post_title, comment, url = comment_info
        st.write(f"**Post Title:** {post_title}")
        st.write(f"**Comment:** {comment}")
        st.write(f"**URL:** {url}")
