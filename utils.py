from typing import Dict, List


def format_conversation_output(
    features: Dict, sentiments: List[Dict], topics: List[str]
) -> Dict:
    """Formats the conversation analysis output for different teams."""
    output = {
        "team_assigning_values": {
            "user_messages": features.get("user_messages", 0),
            "bot_messages": features.get("bot_messages", 0),
            "average_user_message_length": features.get(
                "average_user_message_length", 0
            ),
            "average_bot_message_length": features.get("average_bot_message_length", 0),
        },
        "team_recommending_content": {
            "top_keywords": topics[:5] if topics else [],
        },
        "team_supporting_users": {
            "sentiment_average": (
                sum([1 if senti["label"] == "POSITIVE" else -1 for senti in sentiments])
                / len(sentiments)
                if sentiments
                else 0
            ),
            "sentiment_distribution": {
                "positive": sum(
                    1 for senti in sentiments if senti["label"] == "POSITIVE"
                ),
                "negative": sum(
                    1 for senti in sentiments if senti["label"] == "NEGATIVE"
                ),
                "neutral": sum(
                    1 for senti in sentiments if senti["label"] == "NEUTRAL"
                ),
            },
        },
    }
    return output
