# 💾 SaveReportToFile Component

## Overview
The **SaveReportToFile** component is responsible for **persisting the generated Markdown report** as a local file.  
It takes the formatted report from the `FormatMarkdownReport` component and writes it to a `.md` file.

---

## 📌 Description
This component saves the provided report into a file named **`monthly_report.md`** in the current working directory.  
It ensures the report is stored locally so it can be reviewed, attached, or archived.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name     | Type | Description                       |
|----------|------|-----------------------------------|
| `report` | Data | The Markdown content to be saved. |

### 📤 Outputs
| Name       | Type | Description                                    |
|------------|------|------------------------------------------------|
| `file_path`| Data | The path to the saved file (`monthly_report.md`).|

---

## 🛠 Processing Logic
1. Extracts the Markdown content from the input.  
2. Opens (or creates) a file named `monthly_report.md` in write mode.  
3. Writes the report content using UTF-8 encoding.  
4. Returns the file path.

---

## ✅ Example Usage
When this component receives the following report:
📨 Support Ticket Summary
Total Tickets: 1000
...

It creates a file named `monthly_report.md` containing the same content and outputs:

{
  "value": "monthly_report.md"
}
🏗 Integration in Flow
.Input: Connect this component to the output of FormatMarkdownReport.

.Output: The resulting file path can be used for logging, further processing, or attachments.

📌 This component overwrites the file if it already exists.
