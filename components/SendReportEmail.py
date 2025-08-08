from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, StrInput, IntInput, Output
from langflow.schema.data import Data
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown2

class SendReportEmail(Component):
    display_name = "Send Final HTML Report"
    description = "Sends a styled HTML email from a markdown report."
    icon = "mail"
    name = "SendReportEmail"

    inputs = [
        DataInput(name="markdown_report", display_name="Markdown Report", is_list=False),
        StrInput(name="subject", display_name="Email Subject"),
        StrInput(name="smtp_server", display_name="SMTP Server"),
        IntInput(name="smtp_port", display_name="SMTP Port"),
        StrInput(name="sender_email", display_name="Sender Email"),
        StrInput(name="sender_password", display_name="Sender Password"),
        StrInput(name="recipient_email", display_name="Recipient Email"),
    ]

    outputs = [
        Output(display_name="Email Status", name="status", method="send_email")
    ]

    def send_email(self) -> Data:n
        md = (
            self.markdown_report.value
            if hasattr(self.markdown_report, "value")
            else self.markdown_report
        )
        html = markdown2.markdown(md)

        msg = MIMEMultipart("alternative")
        msg["Subject"] = self.subject
        msg["From"] = self.sender_email
        msg["To"] = self.recipient_email

        msg.attach(MIMEText(md, "plain", "utf-8"))
        msg.attach(MIMEText(html, "html", "utf-8"))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(
                    self.sender_email,
                    [self.recipient_email],
                    msg.as_string(),
                )
            return Data(value="✅ Email sent successfully with HTML report")
        except Exception as e:
            return Data(value=f"❌ Failed to send email: {e}")

