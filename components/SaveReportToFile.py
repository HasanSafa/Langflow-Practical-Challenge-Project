from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

class SaveReportToFile(Component):
    display_name = "Save Report to File"
    description = "Saves the generated markdown report to a local file."
    icon = "save"
    name = "SaveReportToFile"

    inputs = [DataInput(name="report", display_name="Markdown Report", is_list=False)]

    outputs = [Output(display_name="File Path", name="file_path", method="save")]

    def save(self) -> Data:
        report = self.report.value if hasattr(self.report, "value") else self.report
        file_path = "monthly_report.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(report)
        return Data(value=file_path)
