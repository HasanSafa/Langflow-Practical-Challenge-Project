import pandas as pd
import os
import json
from langflow.custom.custom_component.component import Component
from langflow.io import StrInput, DataInput, Output
from langflow.schema.data import Data

class LoadTicketsCSV(Component):
    display_name = "Load Tickets CSV"
    description = "Reads a CSV, fills missing emails, normalizes dates and desc."
    icon = "file"
    name = "LoadTicketsCSV"

    inputs = [
        StrInput(
            name="file_path",
            display_name="CSV File Path",
            value="C:/Users/HP/Downloads/tickets.csv",
        ),
        StrInput(
            name="column_map",
            display_name="Column Map (json)",
            value='{"open_date":"open_date","close_date":"close_date","description":"ticket_description","email":"email"}',
        ),
    ]
    outputs = [
        Output(display_name="Tickets Data", name="tickets_data", method="build_output"),
    ]

    def build_output(self) -> Data:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"CSV not found: {self.file_path}")
        df = pd.read_csv(self.file_path)
        cmap = json.loads(self.column_map)
        df.rename(columns=cmap, inplace=True)
        for col in ["open_date", "close_date", "ticket_description", "email"]:
            if col not in df.columns:
                raise ValueError(f"Missing column: {col}")
        df["open_date"] = pd.to_datetime(df["open_date"])
        df["close_date"] = pd.to_datetime(df["close_date"])
        df["email"].fillna("no-reply@example.com", inplace=True)
        df["response_time"] = (df["close_date"] - df["open_date"]).dt.days
        return Data(value=df.to_dict(orient="records"))


class ValidateTickets(Component):
    display_name = "Validate Tickets"
    description = "Keep tickets with minimal required fields."
    icon = "check"
    name = "ValidateTickets"

    inputs = [
        DataInput(name="tickets", display_name="Tickets", is_list=True),
    ]
    outputs = [
        Output(display_name="Validated Tickets", name="validated", method="validate"),
    ]

    def validate(self) -> Data:
        tickets = self.tickets.value if hasattr(self.tickets, "value") else self.tickets
        valid = [
            t for t in tickets
            if t.get("ticket_description") and t.get("open_date") and t.get("email")
        ]
        return Data(value=valid)

