# WhatsApp Chat Analyzer

This is a Streamlit-based web application that analyzes WhatsApp chat data. It provides various insights, including message statistics, timelines, activity maps, word clouds, and emoji analysis.

## Features

- **Top Statistics**: Total messages, words, media shared, and links shared.
- **Timelines**: Monthly and daily timelines of messages.
- **Activity Maps**: Analysis of the most active days and months.
- **Heatmap**: Weekly activity heatmap.
- **User Analysis**: Most active users in the chat.
- **Word Cloud**: Visualization of the most common words.
- **Emoji Analysis**: Breakdown of emoji usage.

## How to Run Locally

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/whatsapp-chat-analyzer.git
    cd whatsapp-chat-analyzer
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    streamlit run app.py
    ```

## How to Deploy on Render

1. Create a Render account at [Render](https://render.com/).

2. Connect your GitHub repository to Render and deploy it. Follow the instructions provided by Render for setting up your project. You can view the deployed app here: [Your Render App](https://whatsapp-chat-analyzer-73mh.onrender.com/).

## Files and Directories

- `app.py`: Main application script.
- `helper.py`: Helper functions for analysis.
- `preprocessor.py`: Preprocessing functions for chat data.
- `requirements.txt`: List of dependencies.


