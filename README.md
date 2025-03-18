# 📊 Post Analyzer and Generator 🖋️

This powerful tool analyzes your existing posts and helps generate new content that matches your unique writing style using advanced AI technology.

## ✨ Features

- 📝 Analyze the writing style of your existing posts
- 🤖 Generate new content with similar tone and style
- 🌍 Support for multiple languages
- 📏 Flexible content length options
- 🚀 Powered by Llama3.2 open-source LLM

## 🛠️ Set-up

To get started with the tool, follow these steps:

### 1. Obtain an API Key 🔑
- Visit [Groq API Console](https://console.groq.com/keys) to create and get your API_KEY.

### 2. Update .env File ⚙️
- Inside the `.env` file, update the value of `GROQ_API_KEY` with the API_KEY you obtained in the previous step.

### 3. Install Dependencies 📦
- Install the required Python dependencies by running the following command:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Run the Streamlit App 🚀
- After installing the dependencies, run the Streamlit app with the command:
  ```bash
  streamlit run main.py
  ```

This will start the app and you can begin analyzing and generating posts right away!

## 🎮 Usage

Once the app is running, you can input your old posts and select the following options for the new post generation:

- **Text Length** 📏:
  - ⚡ Short
  - 📄 Medium
  - 📚 Long

- **Language** 🌐:
  - 🇺🇸 English
  - 🇵🇱 Polish
  - 🇳🇱 Dutch

The tool will analyze the writing style of your old posts and generate a new post in the chosen language and length that feels authentically "you".

## 💻 Technologies Used

- **Llama3.2**: State-of-the-art open-source LLM for natural language processing
- **LangChain**: Framework for developing applications powered by language models
- **Streamlit**: Interactive web application framework for data apps
- **Groq Cloud**: Ultra-fast inference API for LLM deployment

## 📋 Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## 📁 Project Structure

The project follows the directory structure outlined below:

```bash
project/
│
├── data/
│   ├── raw_data/            # Store your original post data here
│   └── processed_data/      # Preprocessed data for analysis
│
├── .gitignore               # Files to be ignored by git
├── README.md                # This documentation file
├── few_shot.py              # Few-shot learning implementation
├── llm_helper.py            # Helper functions for LLM interaction
├── main.py                  # Main Streamlit application
├── post_generator.py        # Post generation logic
├── preprocess.py            # Data preprocessing utilities
└── requirements.txt         # List of all dependencies needed to run the project
```

## 🤝 Contribution

Feel free to contribute to this project by submitting issues or pull requests!
