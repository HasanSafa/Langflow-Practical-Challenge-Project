from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

def flatten_to_dicts(data):
    if hasattr(data, "value"):
        return flatten_to_dicts(data.value)
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        result = []
        for item in data:
            result.extend(flatten_to_dicts(item))
        return result
    return []

class AggregateStats(Component):
    display_name = "Aggregate Ticket Stats"
    description = "Aggregates sentiment counts, average response time, and sample tickets."
    icon = "chart-bar"
    name = "AggregateStats"

    inputs = [
        DataInput(name="tickets", display_name="Classified Tickets", info="List of ticket dicts", is_list=True),
    ]

    outputs = [
        Output(display_name="Stats", name="stats", method="aggregate"),
    ]

    def aggregate(self) -> Data:
        tickets_list = flatten_to_dicts(self.tickets)

        total = len(tickets_list)
        positive = [t for t in tickets_list if t.get("sentiment") == "Positive"]
        negative = [t for t in tickets_list if t.get("sentiment") == "Negative"]
        neutral = [t for t in tickets_list if t.get("sentiment") == "Neutral"]

        response_times = [t.get("response_time", 0) for t in tickets_list if "response_time" in t]
        avg_response = sum(response_times) / len(response_times) if response_times else 0

        stats = {
            "total_count": total,
            "count_positive": len(positive),
            "count_negative": len(negative),
            "count_neutral": len(neutral),
            "avg_response": round(avg_response, 2),
            "sample_positive": [p.get("ticket_description", "")[:60] for p in positive[:3]],
            "sample_negative": [n.get("ticket_description", "")[:60] for n in negative[:3]],
            "sample_neutral": [nu.get("ticket_description", "")[:60] for nu in neutral[:3]],
        }
        return Data(value=stats)
