from typing import Dict, List


def average_sentiment(messages: List[Dict]) -> float:
    """Calculate the average sentiment of the given messages."""
    if not messages:
        return 0
    average= sum(1 if msg["label"] == "POSITIVE" else -1 for msg in messages) / len(messages)
    return round(average, 2)


def segment_indices(total_messages: int) -> Dict[str, List[int]]:
    """Generate indices for beginning, middle, and end segments."""
    if total_messages == 0:
        return {"beginning": [], "middle": [], "end": []}

    third = total_messages // 3
    beginning = list(range(0, third))
    middle = list(range(third, 2 * third))
    end = list(range(2 * third, total_messages))

    return {"beginning": beginning, "middle": middle, "end": end}


def format_conversation_output(features: Dict, sentiments: List[Dict], topics: List[str]) -> Dict:
    """Formats the conversation analysis output for different teams."""

    total_user_messages = features.get("user_messages", 0)
    indices = segment_indices(total_user_messages)

    sentiment_evolution = {
        "beginning": average_sentiment([sentiments[i] for i in indices["beginning"]]),
        "middle": average_sentiment([sentiments[i] for i in indices["middle"]]),
        "end": average_sentiment([sentiments[i] for i in indices["end"]])
    }

    output = {
        "team_assigning_values": {
            "user_messages": total_user_messages,
            "bot_messages": features.get("bot_messages", 0),
            "average_user_message_length": features.get("average_user_message_length", 0),
            "average_bot_message_length": features.get("average_bot_message_length", 0),
        },
        "team_recommending_content": {
            "top_keywords": topics[:5] if topics else [],
        },
        "team_supporting_users": {
            "sentiment_average": (
                sum(1 if senti["label"] == "POSITIVE" else -1 for senti in sentiments)
                / len(sentiments)
                if sentiments
                else 0
            ),
            "sentiment_distribution": {
                "positive": sum(1 for senti in sentiments if senti["label"] == "POSITIVE"),
                "negative": sum(1 for senti in sentiments if senti["label"] == "NEGATIVE"),
                "neutral": sum(1 for senti in sentiments if senti["label"] == "NEUTRAL"),
            },
            "sentiment_evolution": sentiment_evolution
        },
    }

    return output
