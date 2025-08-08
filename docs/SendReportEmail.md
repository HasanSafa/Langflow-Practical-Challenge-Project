# 📧 SendReportEmail Component

## Overview
The **SendReportEmail** component is responsible for sending the **final report via email**.  
It accepts a Markdown-formatted report, converts it to **styled HTML**, and sends it through an SMTP server to the specified recipient.

---

## 📌 Description
This component:
- Converts the provided Markdown report into HTML.
- Creates a multipart email with both **plain text** and **HTML** content.
- Sends the email securely using **TLS** through the given SMTP server.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name             | Type  | Description                                   |
|------------------|-------|-----------------------------------------------|
| `markdown_report`| Data  | The formatted Markdown report to send.        |
| `subject`        | str   | The subject line for the email.               |
| `smtp_server`    | str   | The SMTP server address (e.g., `smtp.gmail.com`). |
| `smtp_port`      | int   | The SMTP server port (e.g., `587`).           |
| `sender_email`   | str   | The sender's email address.                   |
| `sender_password`| str   | The sender's app-specific password.           |
| `recipient_email`| str   | The recipient's email address.                |

---

### 📤 Outputs
| Name     | Type | Description                                  |
|----------|------|----------------------------------------------|
| `status` | Data | A message indicating whether the email was sent successfully or failed. |

---

## 🛠 Processing Logic
1. Retrieve the Markdown content from input.  
2. Convert the Markdown to **HTML** using `markdown2`.  
3. Build a **MIMEMultipart** email with both plain text and HTML parts.  
4. Connect to the SMTP server using TLS.  
5. Authenticate with the sender’s credentials.  
6. Send the email to the recipient.  
7. Return a success or failure message.

---

## ✅ Example Usage
**Input Example:**
- `markdown_report`: (Markdown text generated from `FormatMarkdownReport`)
- `subject`: `"Monthly Support Ticket Report – 2025-07"`
- `smtp_server`: `"smtp.gmail.com"`
- `smtp_port`: `587`
- `sender_email`: `"myemail@gmail.com"`
- `sender_password`: `"app_password"`
- `recipient_email`: `"stakeholder@example.com"`

**Output Example:**
{
  "value": "✅ Email sent successfully with HTML report"
}
🏗 Integration in Flow
.Connect markdown_report to the output of FormatMarkdownReport.

.Provide SMTP credentials and recipient information.

.The output status can be used for logging or error handling.

📌 Use an App Password (not your main password) when using Gmail for SMTP.
