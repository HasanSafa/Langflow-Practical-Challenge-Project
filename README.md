# 📨 Monthly Support Ticket Report – Langflow Challenge 2025

## 📌 Overview
This project implements an **end-to-end automated pipeline** using **Langflow** to generate a **monthly support ticket report**.  
The flow loads ticket data, validates it, filters closed tickets, classifies sentiments, aggregates statistics, extracts examples, formats them into a markdown report, saves the report locally, and finally sends a styled HTML email to stakeholders.

---

## 🎯 Features
- ✅ **Load & Validate Tickets** from CSV with column normalization  
- ✅ **Filter Closed Tickets** based on valid close_date  
- ✅ **Sentiment Classification** using **NLTK VADER**  
- ✅ **Aggregate Statistics** (Counts, Avg Response Time, Sample Texts)  
- ✅ **Extract Sample Examples** per sentiment category  
- ✅ **Generate Markdown Report** with well-structured sections  
- ✅ **Save Report to File** locally (`monthly_report.md`)  
- ✅ **Send Final HTML Email Report** using SMTP

---

## 🏗 Flow Components
| Component | Description |
|-----------|-------------|
| **LoadTicketsCSV** | Reads CSV, fills missing emails, normalizes dates, calculates response time |
| **ValidateTickets** | Ensures all tickets contain required fields |
| **FilterClosedTickets** | Keeps only tickets with valid close dates |
| **SentimentAnalysisVADER** | Classifies sentiment (Positive, Neutral, Negative) |
| **AggregateStats** | Aggregates counts and calculates average response time |
| **ExtractSentimentExamples** | Collects up to 3 sample messages per sentiment |
| **FormatMarkdownReport** | Formats aggregated data and examples into Markdown |
| **LogSummary** | Logs stats to the console for debugging |
| **SaveReportToFile** | Saves the final Markdown report locally |
| **SendReportEmail** | Sends the Markdown report as styled HTML via SMTP |

---

## 📡 Node Connection Flow (Langflow)

LoadTicketsCSV → ValidateTickets → FilterClosedTickets → SentimentAnalysisVADER
SentimentAnalysisVADER → AggregateStats → LogSummary
SentimentAnalysisVADER → ExtractSentimentExamples
AggregateStats + ExtractSentimentExamples → FormatMarkdownReport
FormatMarkdownReport → SaveReportToFile
FormatMarkdownReport → SendReportEmail

### ✅ The flow is built exactly as shown in the Langflow UI screenshot:

. flow_screenshot_structure

---
```
## 📂 Project Structure

LangflowApp/
├── components/
│ ├── LoadTicketsCSV.py
│ ├── ValidateTickets.py
│ ├── FilterClosedTickets.py
│ ├── SentimentAnalysisVADER.py
│ ├── AggregateStats.py
│ ├── ExtractSentimentExamples.py
│ ├── FormatMarkdownReport.py
│ ├── LogSummary.py
│ ├── SaveReportToFile.py
│ └── SendReportEmail.py
├── docs/
│ ├── LoadTicketsCSV.md
│ ├── ValidateTickets.md
│ ├── FilterClosedTickets.md
│ ├── SentimentAnalysisVADER.md
│ ├── AggregateStats.md
│ ├── ExtractSentimentExamples.md
│ ├── FormatMarkdownReport.md
│ ├── LogSummary.md
│ ├── SaveReportToFile.md
│ └── SendReportEmail.md
├── tickets.csv
├── requirements.txt
├── .gitignore
├── README.md
├── flow_screenshot_structure
└── langflow_practical_challenge_project.
```
---

## 🚀 Usage

1️⃣ **Install dependencies**
pip install -r requirements.txt
2️⃣ Setup NLTK VADER

import nltk
nltk.download('vader_lexicon')
3️⃣ Open Langflow, import all components from components/, and arrange the nodes as per the connection flow above.

4️⃣ Configure SMTP credentials in SendReportEmail:

SMTP Server: smtp.gmail.com

Port: 587

Sender Email & App Password

Recipient Email

5️⃣ Run the flow – The system will:

Load tickets

Generate a Markdown report

Save it locally (monthly_report.md)

Send a formatted HTML email to the recipient

📊 Sample Output (Markdown Report)
# 📨 Support Ticket Summary

**Total Tickets:** 1000  
**Average Response Time:** 5.56 days  

---

## 🧠 Sentiment Breakdown
- Positive: 731
- Neutral: 132
- Negative: 137

---

## 🔍 Examples
### ✅ Positive Samples
- Thanks for the quick resolution of my request.  
- Great job, the system is working perfectly.  

### 😐 Neutral Samples
- The issue still persists despite multiple attempts.  

### ❌ Negative Samples
- I’m dissatisfied with the delay in the response.  

---

*Report generated automatically*
📞 Contact:
For questions, reach out via Discord: hasansafa000

✨ This project fully meets the Langflow Challenge 2025 requirements with advanced custom components and end-to-end automation! ✨

