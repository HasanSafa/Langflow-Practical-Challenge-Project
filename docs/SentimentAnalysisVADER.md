# 😃 SentimentAnalysisVADER Component

## Overview
The **SentimentAnalysisVADER** component classifies support tickets into **Positive**, **Neutral**, or **Negative** sentiments.  
It uses **NLTK's VADER SentimentIntensityAnalyzer** to analyze the `ticket_description` field of each ticket.

---

## 📌 Description
- Processes each ticket’s description and assigns a sentiment label.
- Supports nested or wrapped `Data` objects.
- Returns enriched tickets with an added `sentiment` field.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name      | Type | Description                                    |
|-----------|------|------------------------------------------------|
| `tickets` | Data | List of tickets containing at least a `ticket_description` field. |

### 📤 Outputs
| Name                | Type | Description                                |
|---------------------|------|--------------------------------------------|
| `classified_tickets`| Data | Tickets with an additional `sentiment` field. |

---

## 🛠 Processing Logic
1. Extracts ticket descriptions from input data.
2. Uses `SentimentIntensityAnalyzer` to calculate the sentiment score (`compound`).
3. Classifies based on thresholds:
   - **Positive** if `score >= 0.05`
   - **Negative** if `score <= -0.05`
   - **Neutral** otherwise
4. If the description is missing or empty, sentiment is set to **Unknown**.

---

## ✅ Example Usage
### Example Input:

[
  {"ticket_description": "Great service, thank you!", "open_date": "2025-07-01"},
  {"ticket_description": "The issue is still unresolved.", "open_date": "2025-07-02"},
  {"ticket_description": "", "open_date": "2025-07-03"}
]
Example Output:
json
Copy
Edit
[
  {"ticket_description": "Great service, thank you!", "open_date": "2025-07-01", "sentiment": "Positive"},
  {"ticket_description": "The issue is still unresolved.", "open_date": "2025-07-02", "sentiment": "Negative"},
  {"ticket_description": "", "open_date": "2025-07-03", "sentiment": "Unknown"}
]
🏗 Integration in Flow
1.Input: Takes tickets from ValidateTickets or FilterClosedTickets.

2.Output: Passes classified tickets to:

. AggregateTicketStats

. ExtractSentimentExamples

📌 This component ensures every ticket is assigned a clear sentiment, enabling accurate reporting and analysis.
