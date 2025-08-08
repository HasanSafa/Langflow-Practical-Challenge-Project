from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

def unwrap(data):
    if hasattr(data, "value"):
        return unwrap(data.value)
    if isinstance(data, list):
        result = []
        for item in data:
            result.extend(unwrap(item))
        return result
    if isinstance(data, dict):
        return [data]
    return []

class ExtractSentimentExamples(Component):
    display_name = "Extract Sentiment Examples"
    description = "Extracts sample ticket descriptions grouped by sentiment."
    icon = "list"
    name = "ExtractSentimentExamples"

    inputs = [
        DataInput(name="tickets", display_name="Classified Tickets", info="List of ticket dicts", is_list=True),
    ]

    outputs = [
        Output(display_name="Examples", name="examples", method="extract_examples"),
    ]

    def extract_examples(self) -> Data:
        tickets_list = unwrap(self.tickets)

        examples = {"Positive": [], "Neutral": [], "Negative": []}
        for t in tickets_list:
            sentiment = t.get("sentiment", "Neutral")
            text = t.get("ticket_description", "")
            if sentiment in examples and len(examples[sentiment]) < 3:
                examples[sentiment].append(text)

        return Data(value=examples)
