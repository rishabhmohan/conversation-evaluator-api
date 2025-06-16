# Conversation Evaluator API  
  
## Overview  
This API evaluates user's conversations and extracts insights for various teams. It processes raw conversation data sent as JSON objects and performs feature extraction, sentiment analysis, topic modeling
  
## Features  
- Extract conversation features  
- Analyze conversation sentiment  
- Perform conversation topic modeling  
  
## Installation  
  
1. Clone the repository:  
    ```bash  
    git clone https://github.com/yourusername/conversation-evaluator-api.git  
    cd conversation-evaluator-api  
    ```  
  
2. Install the required dependencies:  
    ```bash  
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
  
**Request Body:** JSON Array of conversation objects. Each conversation object should contain `ref_conversation_id`, `ref_user_id`, and `messages_list`.  
  
**Example Request:**  
```json  
[  
    {  
        "ref_conversation_id": "123",  
        "ref_user_id": "456",  
        "messages_list": [  
            {"message": "Hello", "metadata": {"timestamp": "2023-01-01T00:00:00Z"}},  
            {"message": "Hi there", "metadata": {"timestamp": "2023-01-01T00:01:00Z"}}  
        ]  
    },  
    {  
        "ref_conversation_id": "789",  
        "ref_user_id": "101",  
        "messages_list": [  
            {"message": "How are you?", "metadata": {"timestamp": "2023-01-02T00:00:00Z"}},  
            {"message": "I am good", "metadata": {"timestamp": "2023-01-02T00:01:00Z"}}  
        ]  
    }  
]
```
## Other ideas
1. Emotion Detection
2. Topic/emotion transition over the conversation
3. Prompt-Intent classification
4. Using contextual Sentence Transformers embeddings for LDA; Use BERTopic

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
3. Use statistical indciators to detect bias

Explainbility: Ensure that ML models are interpretable and their decisions can be explained in a health context where users need to trust the system

Feedback loop: Continuously learn from user interactions to improve the model





