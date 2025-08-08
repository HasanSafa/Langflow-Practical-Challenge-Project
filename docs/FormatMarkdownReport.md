# 📝 FormatMarkdownReport Component

## Overview
The **FormatMarkdownReport** component takes aggregated ticket statistics and sentiment examples, then generates a **clean and well-structured Markdown report**.  
This formatted report is later sent by the email sender component.

---

## 📌 Description
This component merges:
- **Stats**: total ticket count, average response time, and sentiment counts.
- **Examples**: sample ticket descriptions grouped by sentiment.

The output is a **Markdown-formatted string** suitable for embedding directly into an email body or saving as a `.md` file.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name       | Type | Description                                                   |
|------------|------|---------------------------------------------------------------|
| `stats`    | Data | Dictionary with aggregated statistics (counts, avg response). |
| `examples` | Data | Dictionary or list containing sample ticket descriptions per sentiment. |

### 📤 Outputs
| Name     | Type | Description                                  |
|----------|------|----------------------------------------------|
| `report` | Data | A formatted Markdown string representing the final support ticket report. |

---

## 🛠 Processing Logic
1. Unwraps and normalizes both `stats` and `examples` inputs.  
2. Supports two formats for examples:
   - **Dict of Lists** (`{"Positive": [...], "Neutral": [...], "Negative": [...]}`)
   - **List of Dicts** (`[{"sentiment":"Positive","message":"..."},...]`)  
3. Creates sections for:
   - **Stats Summary**
   - **Sentiment Breakdown**
   - **Examples per Sentiment**

---

## ✅ Example Output

# 📨 Support Ticket Summary

**Total Tickets:** 1000  
**Average Response Time:** 5.56 days

---

## 🧠 Sentiment Breakdown
- **Positive:** 731
- **Neutral:** 132
- **Negative:** 137

---

## 🔍 Examples

### ✅ Positive Samples
- Thanks for the quick resolution of my request.
- Great job, the system is working perfectly after your intervention.
- I was very well assisted and managed to solve the issue easily.

### 😐 Neutral Samples
- The issue still persists despite multiple attempts to fix it.
- Is there an estimated time for the technical team's response?
- Please confirm receipt of my request.

### ❌ Negative Samples
- I’ve opened this ticket several times and nothing has been resolved.
- I'm dissatisfied with the delay in the team's response.
- This has been unresolved for weeks, very frustrating.

---

*Report generated automatically. For questions, reach out.*
🏗 Integration in Flow
.Input: Receives stats from AggregateStats and examples from ExtractSentimentExamples.

.Output: Connects to SendReportEmail to send the Markdown content as an email.

📌 This component ensures the final email is clear, professional, and easy to read for stakeholders.
