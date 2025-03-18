import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import time
import random

# Page configuration
st.set_page_config(
    page_title="AI Post Generator",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 30px;
    }
    .sub-header {
        font-size: 24px;
        color: #424242;
        text-align: center;
        margin-bottom: 20px;
    }
    .generated-post {
        background-color: #e8f4f8;
        border-left: 5px solid #1E88E5;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    /* Center the generate button and keep footer at the bottom */
    .generate-button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .footer {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        font-size: 14px;
        color: #424242;
    }
</style>
""", unsafe_allow_html=True)

# Options for length and language with emojis
length_options = ["✓ Short", "✓✓ Medium", "✓✓✓ Long"]
language_options = ["🇺🇸 English", "🇵🇱 Polish", "🇳🇱 Dutch"]

# Loading animation with simple progress bar
def loading_animation():
    progress_bar = st.progress(0)
    
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.05)
    
    progress_bar.empty()

# Main app layout
def main():
    # Header
    st.markdown("<h1 class='main-header'>✍️ AI Post Generator</h1>", unsafe_allow_html=True)
    
    # App description
    st.markdown("<p class='sub-header'>Generate high-quality posts in your unique writing style</p>", unsafe_allow_html=True)
    
    # Sidebar with information
    with st.sidebar:
        st.markdown("### About")
        st.write("This tool uses Llama3.2, an open-source LLM, to analyze your writing style and generate new posts.")
        
        st.markdown("### How it works")
        st.write("1. Select your preferred topic")
        st.write("2. Choose the length of your post")
        st.write("3. Select your desired language")
        st.write("4. Click 'Generate Post' and watch the magic happen!")
        
        st.markdown("### Powered by")
        st.write("- Llama3.2 open-source LLM")
        st.write("- LangChain framework")
        st.write("- Groq Cloud")
    
        st.markdown("### More info")
        st.write("""  
        To learn more about how it works or to explore additional details, visit the GitHub repository. 
        """)
        st.write("[GitHub Repository](https://github.com/IzaMacBor/post-generator-tool.git)")

    # Main content area
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Initialize FewShotPosts
    fs = FewShotPosts()
    tags = fs.get_tags()
    
    # Settings section
    st.markdown("### 🛠️ Post Settings")
    
    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Dropdown for Topic (Tags)
        selected_tag = st.selectbox("🏷️ Topic", options=tags)
        
    with col2:
        # Dropdown for Length
        selected_length = st.selectbox("📏 Length", options=length_options)
        # Remove the emoji prefix for processing
        selected_length = selected_length.split(" ")[1]
        
    with col3:
        # Dropdown for Language
        selected_language = st.selectbox("🌐 Language", options=language_options)
        # Remove the emoji prefix for processing
        selected_language = selected_language.split(" ")[1]
        
    # Generate Button centered
    st.markdown('<div class="generate-button-container">', unsafe_allow_html=True)
    generate_button = st.button("✨ Generate Post")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Generate post
    if generate_button:
        with st.spinner():
            loading_animation()
            post = generate_post(selected_length, selected_language, selected_tag)
            
        # Display the generated post
        st.markdown("### 📝 Your Generated Post")
        st.write(post)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.download_button(
                label="📥 Download",
                data=post,
                file_name=f"generated_post_{selected_tag}_{selected_language}.txt",
                mime="text/plain"
            )
        with col2:
            st.button("📋 Copy to Clipboard")
        with col3:
            st.button("🔄 Regenerate")
        with col4:
            st.button("👍 Like This Post")

# Footer 
st.markdown('<div class="footer">Created by Izabela Mac-Borkowska</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
