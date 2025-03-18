
# Post Analyzer and Generator

This tool analyzes posts and helps generate new posts based on the writing style of the old posts.

## Set-up

To get started with the tool, follow these steps:

### 1. Obtain an API Key
- Visit [Groq API Console](https://console.groq.com/keys) to create and get your API_KEY.

### 2. Update .env File
- Inside the `.env` file, update the value of `GROQ_API_KEY` with the API_KEY you obtained in the previous step.

### 3. Install Dependencies
- Install the required Python dependencies by running the following command:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Run the Streamlit App
- After installing the dependencies, run the Streamlit app with the command:
  ```bash
  streamlit run main.py
  ```

This will start the app and you can begin analyzing and generating posts.

## Usage

Once the app is running, you can input your old posts and select the following options for the new post generation:

- **Text Length**: You can choose from:
  - Short
  - Medium
  - Long

- **Language**: Choose one of the following languages for the generated post:
  - English
  - Polish
  - Dutch

The tool will analyze the writing style of the old posts and generate a new post in the chosen language and length.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
