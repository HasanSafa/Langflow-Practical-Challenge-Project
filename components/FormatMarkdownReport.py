from langflow.custom.custom_component.component import Component
from langflow.io import DataInput, Output
from langflow.schema.data import Data

class FormatMarkdownReport(Component):
    display_name = "Format Markdown Report"
    description = "Formats aggregated stats and examples into a nicely structured markdown report."
    icon = "markdown"
    name = "FormatMarkdownReport"

    inputs = [
        DataInput(name="stats", display_name="Stats", is_list=False),
        DataInput(name="examples", display_name="Examples", is_list=False),
    ]
    outputs = [
        Output(display_name="Markdown Report", name="report", method="format_report")
    ]

    def format_report(self) -> Data:
        stats = self.stats.value if hasattr(self.stats, "value") else self.stats
        examples_obj = self.examples.value if hasattr(self.examples, "value") else self.examples

        positive, neutral, negative = [], [], []

        # handle dict-of-lists
        if isinstance(examples_obj, dict):
            norm = {k.lower(): v for k, v in examples_obj.items()}
            positive = norm.get("positive", [])
            neutral  = norm.get("neutral", [])
            negative = norm.get("negative", [])

        # handle list-of-dicts
        elif isinstance(examples_obj, list):
            for item in examples_obj:
                if not isinstance(item, dict):
                    continue
                sent = item.get("sentiment", "").lower()
                text = item.get("message") or item.get("text") or item.get("example", "")
                if sent == "positive":
                    positive.append(text)
                elif sent == "neutral":
                    neutral.append(text)
                elif sent == "negative":
                    negative.append(text)

        # build each section separately
        pos_md = "\n".join(f"- {m}" for m in positive) or "No positive examples."
        neu_md = "\n".join(f"- {m}" for m in neutral)  or "No neutral examples."
        neg_md = "\n".join(f"- {m}" for m in negative) or "No negative examples."

        md = f"""
# 📨 Support Ticket Summary

**Total Tickets:** {stats.get("total_count", "N/A")}  
**Average Response Time:** {stats.get("avg_response", "N/A")} days

---

## 🧠 Sentiment Breakdown

- **Positive:** {stats.get("count_positive", 0)}
- **Neutral:** {stats.get("count_neutral", 0)}
- **Negative:** {stats.get("count_negative", 0)}

---

## 🔍 Examples

### ✅ Positive Samples

{pos_md}

### 😐 Neutral Samples

{neu_md}

### ❌ Negative Samples

{neg_md}

---

*Report generated automatically. For questions, reach out.*
""".strip()

        return Data(value=md)
