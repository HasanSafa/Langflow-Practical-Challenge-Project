# 📨 Monthly Support Ticket Report – Langflow Challenge 2025

## 📌 Overview
This project implements an **end-to-end automated flow** using **Langflow** to generate a **monthly support ticket report**.  
The flow loads ticket data, classifies them by sentiment, aggregates statistics, and sends a formatted email to stakeholders.

---

## 🎯 Features
- **Load tickets from CSV**
- **Classify sentiment using NLTK VADER**
- **Aggregate statistics** (Total tickets, Average Response Time, Sentiment counts)
- **Send formatted email report** using SMTP
- **Include sample ticket descriptions per sentiment category** for clarity

---

## 🏗 Flow Components
1. [**LoadTicketsCSV**](docs/load_tickets.md) – Reads ticket data from CSV and calculates response time.  
2. [**SentimentAnalysisVADER**](docs/sentiment_vader.md) – Classifies each ticket sentiment as Positive, Neutral, or Negative.  
3. [**AggregateStats**](docs/aggregate_stats.md) – Aggregates counts and average response time, and selects sample tickets.  
4. [**SendReportEmail**](docs/send_report.md) – Sends the monthly report email in the required format.

---

## 🚀 Usage
1. Open **Langflow** locally.  
2. Import all custom components (`.py`) from the `components/` folder.  
3. Build the flow in this order:  
LoadTicketsCSV → SentimentAnalysisVADER → AggregateStats → SendReportEmail
4. Place `tickets.csv` in the correct path and configure SMTP settings (email & app password) in the SendReportEmail component.  
5. Run the flow and the report will be sent to your inbox.

---

## 📂 Project Structure
LangflowApp/
├── components/            
│   ├── load_tickets.py
│   ├── sentiment_vader.py
│   ├── aggregate_stats.py
│   └── send_report.py
├── docs/                  
│   ├── load_tickets.md
│   ├── sentiment_vader.md
│   ├── aggregate_stats.md
│   └── send_report.md
├── tickets.csv             
├── requirements.txt
├── .gitignore              
├── README.md
└── langflow practical challenge project.json 


---

## 🛠 Requirements
- Python 3.10+  
- Langflow  
- Libraries:  
  - `pandas`  
  - `nltk`  

Install dependencies:
```bash
pip install -r requirements.txt
NLTK VADER Setupbash
>>> import nltk
>>> nltk.download('vader_lexicon')
```
Sample Email Output

# Support Ticket Summary for 2025-07
**Total Tickets:** 1000  
**Average Response Time:** 5.56 days  

## Sentiment Breakdown
- Positive: 731
- Neutral: 132
- Negative: 137

### Examples:
- Positive Samples:
  • Thanks for the quick resolution of my request.  
  • Great job, the system is working perfectly after your intervention.  
  • I was very well assisted and managed to solve the issue easily.  
- Neutral Samples:
  • The issue still persists despite multiple attempts to fix it.  
  • Is there an estimated time for the technical team's response?  
- Negative Samples:
  • I’ve opened this ticket several times and nothing has been resolved yet.  
  • I'm dissatisfied with the delay in the team's response.  

📞 Contact
For questions, reach out to:
hasansafa000

✨ This project is fully ready and aligned with the Langflow Challenge 2025 requirements! ✨
