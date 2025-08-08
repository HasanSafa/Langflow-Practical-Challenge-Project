# 📝 ExtractSentimentExamples Component

## Overview
The **ExtractSentimentExamples** component extracts up to three sample ticket descriptions for each sentiment category:  
`Positive`, `Neutral`, and `Negative`.  

---

## 📌 Description
This component receives classified tickets (with a `sentiment` field) and outputs a dictionary containing representative examples for each sentiment. These samples are later used to enrich the final report with real user feedback.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name      | Type | Description                                                   |
|-----------|------|---------------------------------------------------------------|
| `tickets` | Data | List of classified ticket dictionaries (with `sentiment` and `ticket_description`). |

### 📤 Outputs
| Name      | Type | Description                                                        |
|-----------|------|--------------------------------------------------------------------|
| `examples`| Data | Dictionary mapping sentiment categories to a list of up to 3 examples each. |

---

## 🛠 Processing Logic
1. Unwraps input data into a flat list of ticket dictionaries.  
2. Iterates through tickets and groups descriptions based on `sentiment`.  
3. Limits the number of examples to **3 per sentiment category**.

---

## ✅ Example Output

{
  "Positive": [
    "Thanks for the quick resolution of my request.",
    "Great job, the system is working perfectly.",
    "I was very well assisted and managed to solve the issue easily."
  ],
  "Neutral": [
    "The issue still persists despite multiple attempts to fix it.",
    "Is there an estimated time for the technical team's response?",
    "Please confirm receipt of my request."
  ],
  "Negative": [
    "I’ve opened this ticket several times and nothing has been resolved.",
    "I'm dissatisfied with the delay in the team's response.",
    "This has been unresolved for weeks, very frustrating."
  ]
}
🏗 Integration in Flow
1.Input: Comes from SentimentAnalysisVADER.

2.Output: Feeds into FormatMarkdownReport so that examples are included in the final email body.

📌 This component ensures the final report contains real user feedback samples to give stakeholders context beyond just numbers.
