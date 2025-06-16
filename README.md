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
