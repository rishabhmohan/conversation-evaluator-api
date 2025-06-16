from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import JSONResponse
import json
from models import (
    extract_conversation_features,
    analyze_conversation_sentiment,
    perform_conversation_topic_modeling,
)
from utils import (
    format_conversation_output,
)

app = FastAPI(
    title="Evaluate conversations API",
    description="API to evaluate user's conversations and extract insights for various teams.",
    version="1.0.0",
)


@app.post("/evaluate_conversation", response_class=JSONResponse)
async def evaluate_conversation(conversation_data: list = Body(...)):
    """Endpoint to process conversations JSON."""
    try:
        results = []
        for conv in conversation_data:
            messages = conv.get("messages_list", [])
            ref_conversation_id = conv.get("ref_conversation_id")
            ref_user_id = conv.get("ref_user_id")

            features = extract_conversation_features(messages)
            sentiments = analyze_conversation_sentiment(messages)
            topics = perform_conversation_topic_modeling(messages)
            formatted_output = format_conversation_output(features, sentiments, topics)

            conversation_metadata = {
                "ref_conversation_id": ref_conversation_id,
                "ref_user_id": ref_user_id,
                "total_messages": features.get("total_messages", 0),
            }
            results.append(
                {
                    "conversation_metadata": conversation_metadata,
                    "analysis_results": formatted_output,
                }
            )
        return JSONResponse(content={"conversations": results})
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON format.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
