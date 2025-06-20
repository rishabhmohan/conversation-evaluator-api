# Conversation Evaluator API  
  
## Overview  
This API evaluates user's conversations and extracts insights for various teams. It processes raw conversation data sent as JSON objects and performs feature extraction, sentiment analysis, topic modeling
  
## Features  
- Extract conversation features  
- Analyze conversation sentiment  
- Perform conversation topic modeling

  
## Steps  
  
### 1. Initialization  
  
- Import necessary libraries and modules.  
- Create a FastAPI app instance.  
  
### 2. Endpoint Definition  
  
- Define a POST endpoint `/evaluate_conversation`.  
  
### 3. Request Handling  
  
- Accept a JSON body with conversation data.  
  
### 4. Loop Through Conversations  
  
- Extract messages, conversation ID, and user ID.  
- Perform feature extraction, sentiment analysis, and topic modeling.  
- Format the output and collect metadata.  
- Append the processed data to `results`.  
  
### 5. Response Handling  
  
- Return the results as a JSON response.  
- Handle JSON decoding errors and other exceptions.
- 
## Installation  
  
1. Clone the repository:  
    ```bash  
    git clone https://github.com/yourusername/conversation-evaluator-api.git  
    cd conversation-evaluator-api  
    ```  
  
2. Install the required dependencies:  
    ```bash
    conda create -n conv python=3.11
    conda activate conv
    pip install -r requirements.txt  
    ```  
  
## Running the API  
  
1. Start the FastAPI server:  
    ```bash  
    uvicorn main:app --reload  
    ```  
  
2. The API will be available at `http://127.0.0.1:8000`.  
  
## Usage  
  
### Endpoint: Evaluate Conversation  
  
**URL:** `/evaluate_conversation`  
  
**Method:** `POST`  
  
**Request Body:** JSON Array of conversation objects. Each conversation object should contain  `messages_list`.  
  
**Example Request:**  
```json  
[
  {
    "messages_list": [
      {
        "ref_conversation_id": 98696,
        "ref_user_id": 782,
        "transaction_datetime_utc": "2023-10-01T10:15:00Z",
        "screen_name": "ChattyPenguin",
        "message": "Hello StoryBot, I\u2019m having a tough time with this app. My fingers aren\u2019t what they used to be. Can you help me?"
      },
      {
        "ref_conversation_id": 98696,
        "ref_user_id": 1,
        "transaction_datetime_utc": "2023-10-01T10:20:00Z",
        "screen_name": "StoryBot",
        "message": "Hello ChattyPenguin! I\u2019m here to help. Can you tell me what issues you're experiencing with the app?"
      },
]
```
## Other ideas
1. Emotion Detection: Emotion frequency and transition over the conversation
2. Identify and measure the presence of topics related to resilience e.g. coping strategies, personal growth
3. Prompt-Intent classification
4. Using contextual Sentence Transformers embeddings for LDA; Use BERTopic
5. Engagement metrics (from discussions and activities json files)

## Evolution over time
1. Combine Named Entity Recognition with sentiment analysis to understand the user's sentiments towards specific entities (e.g., people, places, topics).
2. Detect trends in user's emotions or beliefs by analyzing the temporal aspect of the conversations
3. Personalization: If users always talk about similar topics, prompt them to different topics to keep them interested/motivated or personalized solutions for their health nd resilience

## Challenges and Best practices
System design
1. Scalabilty - For batch processing, we can use AWS Batch for comprehensive analysis and reporting. if real-time analysis, we can use autoscaling/serverless or API gateway
2. Latency - use caching if possible. Optimize ML models for inference

Data privacy
1. Encryption: Ensure data is encrypted, securely stored and anonymized before it is processed adhering to laws and regulations. Conduct compliance checks
2. Transparency: Obtain user consent for training ML models on customers data
3. Use statistical indicators to detect bias

Explainability: Ensure that ML models are interpretable and their decisions can be explained in a health context where users need to trust the system

Feedback loop: Continuously learn from user interactions to improve the model





