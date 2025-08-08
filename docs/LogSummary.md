# 🖥 LogSummary Component

## Overview
The **LogSummary** component is a simple debugging utility that prints the aggregated ticket statistics to the console.  
It helps developers **verify the stats output** before sending the report or passing it to other components.

---

## 📌 Description
This component is mainly for **development and troubleshooting**.  
It takes the aggregated statistics (`stats`) and logs them using a console print statement.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name   | Type | Description                             |
|--------|------|-----------------------------------------|
| `stats`| Data | Dictionary containing ticket statistics.|

### 📤 Outputs
| Name  | Type | Description                                      |
|-------|------|--------------------------------------------------|
| `log` | Data | Message confirming that stats were logged.       |

---

## 🛠 Processing Logic
1. Extracts `stats` from the input.  
2. Logs the stats in the format:
[LOG] Summary Stats: {stats}
3. Returns a confirmation message `"Stats logged successfully."`

---

## ✅ Example Usage
When this component receives:
{
"total_count": 1000,
"count_positive": 731,
"count_negative": 137,
"count_neutral": 132,
"avg_response": 5.56
}
It prints:

[LOG] Summary Stats: {'total_count': 1000, 'count_positive': 731, 'count_negative': 137, 'count_neutral': 132, 'avg_response': 5.56}
And outputs:

{
  "value": "Stats logged successfully."
}
🏗 Integration in Flow
.Input: Connects to the output of AggregateStats.

.Output: Can be ignored or chained to other debug components.

📌 Use this component only for debugging. It does not alter or format data.
