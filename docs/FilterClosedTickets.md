# 🔍 FilterClosedTickets Component

## Overview
The **FilterClosedTickets** component filters a list of support tickets, keeping only those that have a valid `close_date`.  
It ensures that only tickets with a correctly formatted and existing close date proceed to the next steps of the pipeline.

---

## 📌 Description
- Validates the presence and format of the `close_date` field.
- Uses Pandas for robust date parsing.
- Supports nested data structures via the `unwrap` helper.

---

## 🧩 Component Details

### ⚙️ Inputs
| Name      | Type | Description                                |
|-----------|------|--------------------------------------------|
| `tickets` | Data | Ticket data (possibly nested) to be filtered. |

### 📤 Outputs
| Name            | Type | Description                           |
|-----------------|------|---------------------------------------|
| `closed_tickets`| Data | List of tickets with valid `close_date`. |

---

## 🛠 Processing Logic

### 🔹 **unwrap(data)**
- Flattens nested `Data` objects, lists, and dictionaries into a clean list of ticket dictionaries.

### 🔹 **Filtering Rule**
A ticket is considered closed if:
- It has a field `close_date`.
- `close_date` can be successfully parsed to a valid date using `pandas.to_datetime`.

---

## ✅ Example Usage
### Example Input:

[
  {"ticket_description": "Resolved issue", "open_date": "2025-07-01", "close_date": "2025-07-02"},
  {"ticket_description": "Pending", "open_date": "2025-07-03", "close_date": ""},
  {"ticket_description": "Closed", "open_date": "2025-07-04", "close_date": "invalid"}
]
Example Output:
json
Copy
Edit
[
  {"ticket_description": "Resolved issue", "open_date": "2025-07-01", "close_date": "2025-07-02"}
]
🏗 Integration in Flow
1.This component is used after ValidateTickets.

2.It ensures only closed tickets proceed to:

. ExtractSentimentExamples

. Aggregation

. Further processing components.

📌 Using this component ensures that the flow processes only tickets with confirmed closure dates, making downstream analysis (e.g., sentiment, response time) accurate.
