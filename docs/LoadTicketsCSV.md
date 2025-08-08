# 📂 LoadTicketsCSV & ValidateTickets Components

## Overview
These two custom components handle loading and validating support ticket data from a CSV file.  
They ensure that the data is normalized, required fields are present, and response times are calculated before further processing in the Langflow pipeline.

---

## 🧩 **1. LoadTicketsCSV**

### 📌 **Description**
Reads a CSV file, maps columns, fills missing emails, normalizes date formats, and calculates response times.

### ⚙️ **Inputs**
| Name        | Type     | Description                                                                 | Default Value |
|-------------|----------|-----------------------------------------------------------------------------|---------------|
| `file_path` | String   | Path to the CSV file containing tickets data.                               | `C:/Users/HP/Downloads/tickets.csv` |
| `column_map`| JSON Str | JSON mapping of CSV column names to required fields (`open_date`, `close_date`, `ticket_description`, `email`). | `{"open_date":"open_date","close_date":"close_date","description":"ticket_description","email":"email"}` |

### 📤 **Outputs**
| Name          | Type | Description                           |
|---------------|------|---------------------------------------|
| `tickets_data`| Data | A list of ticket dictionaries ready for further processing. |

### 🛠 **Processing Steps**
1. Reads CSV from the provided path.
2. Renames columns according to the `column_map`.
3. Validates that all required columns exist.
4. Converts `open_date` and `close_date` to datetime objects.
5. Fills missing email addresses with `no-reply@example.com`.
6. Computes `response_time` as the difference (in days) between `close_date` and `open_date`.

---

## 🧩 **2. ValidateTickets**

### 📌 **Description**
Filters out tickets that do not have the minimal required fields.

### ⚙️ **Inputs**
| Name      | Type | Description                       |
|-----------|------|-----------------------------------|
| `tickets` | Data | List of ticket dictionaries to validate. |

### 📤 **Outputs**
| Name         | Type | Description                           |
|--------------|------|---------------------------------------|
| `validated`  | Data | List of valid tickets that passed the checks. |

### 🛠 **Validation Rules**
- Ticket must have:
  - `ticket_description`
  - `open_date`
  - `email`

---

## ✅ Example Usage
# Example input CSV
open_date,close_date,ticket_description,email
2025-07-01,2025-07-03,"Issue resolved quickly","user@example.com"
2025-07-02,2025-07-05,"No response from support",""

# Output after LoadTicketsCSV
[
  {
    "open_date": "2025-07-01",
    "close_date": "2025-07-03",
    "ticket_description": "Issue resolved quickly",
    "email": "user@example.com",
    "response_time": 2
  },
  {
    "open_date": "2025-07-02",
    "close_date": "2025-07-05",
    "ticket_description": "No response from support",
    "email": "no-reply@example.com",
    "response_time": 3
  }
]
1.LoadTicketsCSV → loads and preprocesses the CSV data.

2.ValidateTickets → ensures only valid tickets continue to the next components.

📌 This component is essential for ensuring data integrity before sentiment analysis and aggregation in the Langflow Challenge 2025 pipeline.
