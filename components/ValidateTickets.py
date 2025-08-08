from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

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

class ValidateTickets(Component):
    display_name = "Validate Tickets"
    description = "Ensures all tickets contain required fields with values."
    icon = "check"
    name = "ValidateTickets"

    inputs = [DataInput(name="tickets", display_name="Tickets", is_list=True)]

    outputs = [Output(display_name="Validated Tickets", name="validated", method="validate")]

    def validate(self) -> Data:
        tickets = unwrap(self.tickets)

        def is_valid(ticket):
            if not isinstance(ticket, dict):
                return False
            required_fields = ["ticket_description", "open_date"]
            return all(field in ticket and ticket[field] not in [None, ""] for field in required_fields)

        valid_tickets = [t for t in tickets if is_valid(t)]
        return Data(value=valid_tickets)

