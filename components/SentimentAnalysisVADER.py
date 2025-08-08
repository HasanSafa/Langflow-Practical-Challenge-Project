from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

class SentimentAnalysisVADER(Component):
    display_name = "Sentiment Analysis (VADER)"
    description = "Classifies ticket sentiments using NLTK VADER based on the 'ticket_description' field."
    icon = "face-smile"
    name = "SentimentAnalysisVADER"

    inputs = [
        DataInput(name="tickets", display_name="Tickets Data", info="List of ticket dictionaries", is_list=True),
    ]

    outputs = [
        Output(display_name="Classified Tickets", name="classified_tickets", method="analyze_sentiment"),
    ]

    def analyze_sentiment(self) -> Data:
        from nltk.sentiment.vader import SentimentIntensityAnalyzer
        sia = SentimentIntensityAnalyzer()

        raw_input = self.tickets
        tickets_list = raw_input.value if hasattr(raw_input, "value") else raw_input

        if not tickets_list:
            self.status = "No tickets received for sentiment analysis"
            return Data(value=[])

        normalized = []
        for item in tickets_list:
            if hasattr(item, "value"):
                item = item.value
            if isinstance(item, list):
                normalized.extend(item)
            elif isinstance(item, dict):
                normalized.append(item)

        result = []
        for ticket in normalized:
            text = ticket.get("ticket_description", "").strip()
            if not text:
                ticket["sentiment"] = "Unknown"
            else:
                score = sia.polarity_scores(text)["compound"]
                if score >= 0.05:
                    ticket["sentiment"] = "Positive"
                elif score <= -0.05:
                    ticket["sentiment"] = "Negative"
                else:
                    ticket["sentiment"] = "Neutral"
            result.append(ticket)

        self.status = f"Classified {len(result)} tickets"
        return Data(value=result)
