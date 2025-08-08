# 📊 AggregateStats Component

## Overview
The **AggregateStats** component computes statistics from classified tickets, including:
- Total ticket count
- Sentiment distribution
- Average response time
- Sample ticket descriptions for each sentiment category

---

## 📌 Description
This component takes as input a list of tickets already classified by sentiment and outputs aggregated metrics to be used in the final report.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name      | Type | Description                                         |
|-----------|------|-----------------------------------------------------|
| `tickets` | Data | List of ticket dictionaries with `sentiment` and `response_time` fields. |

### 📤 Outputs
| Name   | Type | Description                                      |
|--------|------|--------------------------------------------------|
| `stats`| Data | Dictionary containing aggregated statistics and sentiment samples. |

---

## 🛠 Processing Logic
1. Flattens nested or wrapped input data into a list of dictionaries.  
2. Counts tickets by sentiment (`Positive`, `Negative`, `Neutral`).  
3. Calculates **average response time** from the `response_time` field.  
4. Extracts up to **3 sample ticket descriptions** per sentiment (first 60 characters).

---

## ✅ Example Output
{
  "total_count": 1000,
  "count_positive": 731,
  "count_negative": 137,
  "count_neutral": 132,
  "avg_response": 5.56,
  "sample_positive": ["Thanks for the quick resolution...", "Great job, the system...", "I was very well assisted..."],
  "sample_negative": ["I’ve opened this ticket several times...", "I'm dissatisfied with the delay...", "Still not resolved after many attempts..."],
  "sample_neutral": ["The issue still persists despite...", "Is there an estimated time...", "Please confirm receipt of my request..."]
}
🏗 Integration in Flow
Input: Comes from SentimentAnalysisVADER.

Output: Feeds into:

FormatMarkdownReport

SendReportEmail

📌 This component ensures the email report includes both numerical statistics and representative ticket samples.
