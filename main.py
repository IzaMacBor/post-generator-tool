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
        margin-bottom: 20px;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .generated-post {
        background-color: #e8f4f8;
        border-left: 5px solid #1E88E5;
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #616161;
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
        st.image("https://via.placeholder.com/150x150.png?text=AI+Writer", use_container_width=True)
        st.markdown("### About")
        st.write("This tool uses Llama3.2, an open-source LLM, to analyze your writing style and generate new posts.")
        
        st.markdown("### How it works")
        st.write("1. Select your preferred topic")
        st.write("2. Choose the length of your post")
        st.write("3. Select your desired language")
        st.write("4. Click 'Generate' and watch the magic happen!")
        
        st.markdown("### Powered by")
        st.write("- Llama3.2 open-source LLM")
        st.write("- LangChain framework")
        st.write("- Groq Cloud")
    
    # Main content area
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Initialize FewShotPosts
    fs = FewShotPosts()
    tags = fs.get_tags()
    
    # Settings section
    st.markdown("### 🎛️ Post Settings")
    
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
        
    # Generate Button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button("✨ Generate Post")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Generate post
    if generate_button:
        with st.spinner():
            loading_animation()
            post = generate_post(selected_length, selected_language, selected_tag)
            
        # Display the generated post
        st.markdown("<div class='generated-post'>", unsafe_allow_html=True)
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
    st.markdown("<div class='footer'>Powered by Llama3.2 open-source LLM and LangChain • © 2025 Post Generator</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()