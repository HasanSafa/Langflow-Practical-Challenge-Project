from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

class LogSummary(Component):
    display_name = "Log Summary"
    description = "Logs stats to console for debugging."
    icon = "terminal"
    name = "LogSummary"

    inputs = [DataInput(name="stats", display_name="Stats", is_list=False)]

    outputs = [Output(display_name="Log Result", name="log", method="log")]

    def log(self) -> Data:
        stats = self.stats.value if hasattr(self.stats, "value") else self.stats
        print("[LOG] Summary Stats:", stats)
        return Data(value="Stats logged successfully.")
