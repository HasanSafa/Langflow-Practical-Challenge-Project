from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data
import pandas as pd

def unwrap(data):
    if data is None:
        return []
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

class FilterClosedTickets(Component):
    display_name = "Filter Closed Tickets"
    description = "Filters only tickets that have a valid close_date field."
    icon = "filter"
    name = "FilterClosedTickets"

    inputs = [
        DataInput(name="tickets", display_name="Tickets Data", info="List of ticket dicts", is_list=True),
    ]

    outputs = [
        Output(display_name="Closed Tickets", name="closed_tickets", method="filter_closed"),
    ]

    def filter_closed(self) -> Data:
        tickets_list = unwrap(self.tickets)

        def is_valid_date(value):
            try:
                pd.to_datetime(value)
                return True
            except:
                return False

        closed = [t for t in tickets_list if is_valid_date(t.get("close_date"))]
        return Data(value=closed)
