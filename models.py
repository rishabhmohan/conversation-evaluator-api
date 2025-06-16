import logging
from typing import List, Dict
from transformers import pipeline
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sentiment Analysis Pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Topic Modeling Components for Conversations
conversation_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words="english")
conversation_lda_model = LatentDirichletAllocation(n_components=5, random_state=1)


def extract_conversation_features(messages: List[Dict]) -> Dict:
    """Extracts features from conversation messages."""
    try:
        user_messages = [
            msg["message"] for msg in messages if msg["screen_name"] != "StoryBot"
        ]
        bot_messages = [
            msg["message"] for msg in messages if msg["screen_name"] == "StoryBot"
        ]

        avg_user_length = (
            np.mean([len(msg.split()) for msg in user_messages]) if user_messages else 0
        )
        avg_bot_length = (
            np.mean([len(msg.split()) for msg in bot_messages]) if bot_messages else 0
        )

        features = {
            "total_messages": len(messages),
            "user_messages": len(user_messages),
            "bot_messages": len(bot_messages),
            "average_user_message_length": round(avg_user_length, 2),
            "average_bot_message_length": round(avg_bot_length, 2),
        }
        return features
    except Exception as e:
        logger.error(f"Error extracting conversation features: {e}")
        return {}


def analyze_conversation_sentiment(messages: List[Dict]) -> List[Dict]:
    """Analyzes sentiment of user messages in conversations."""
    try:
        user_messages = [
            msg["message"] for msg in messages if msg["screen_name"] != "StoryBot"
        ]
        if not user_messages:
            logger.warning("No user messages available for sentiment analysis.")
            return []
        sentiments = sentiment_pipeline(user_messages)
        return sentiments
    except Exception as e:
        logger.error(f"Error analyzing conversation sentiment: {e}")
        return []


def perform_conversation_topic_modeling(messages: List[Dict]) -> List[str]:
    """Performs topic modeling on user messages in conversations and extracts top keywords for the entire
     conversation."""
    try:
        user_messages = [
            msg["message"] for msg in messages if msg["screen_name"] != "StoryBot"
        ]
        if not user_messages:
            logger.warning("No user messages available for topic modeling.")
            return []

            # Vectorize the user messages
        tf = conversation_vectorizer.fit_transform(user_messages)
        if tf.shape[1] == 0:
            logger.warning(
                "No terms remain after vectorization. Skipping topic modeling."
            )
            return []

        # Fit the LDA model
        conversation_lda_model.fit(tf)

        # Aggregate keywords for the entire conversation
        term_topic_matrix = conversation_lda_model.components_
        feature_names = conversation_vectorizer.get_feature_names_out()

        # Sum the term-topic matrix to get the overall importance of each term
        term_importance = np.sum(term_topic_matrix, axis=0)
        top_keyword_indices = term_importance.argsort()[-10:][
            ::-1
        ]  # Get top 10 keywords
        top_keywords = [feature_names[i] for i in top_keyword_indices]

        return top_keywords
    except ValueError as ve:
        logger.error(f"Conversation Topic Modeling Error: {ve}")
        return []
    except Exception as e:
        logger.error(f"Unexpected error in conversation topic modeling: {e}")
        return []
