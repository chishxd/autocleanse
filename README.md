# 🧹 AutoCleanSE

A fast, modular, **dataset-agnostic CLI tool** to clean and summarize messy CSV/Excel files.

> Built with Python, powered by Pandas. No cloud, no bloat — just clean data, fast.

---

## ⚙️ Features

- Drop fully empty rows and columns
- Remove duplicate rows
- Auto-infer and fix data types
- Trim whitespace, normalize strings
- Generate cleaning reports (JSON)
- CLI-first with sane defaults
- Built using `pandas`, `typer`, and `rich`

---

## 🚀 Installation (via Poetry)

```bash
git clone https://github.com/chishxd/autocleanse
cd autocleanse
poetry install
````

---

## 🧪 Usage

```bash
poetry run autocleanse clean sample_data/dirty.csv --output cleaned.csv --report report.json
```

### Common Options

| Flag          | Description                            |
| ------------- | -------------------------------------- |
| `--output`    | Save cleaned dataset to this file      |
| `--report`    | Generate a cleaning report (JSON)      |
| `--drop-null` | Drop rows/columns with all null values |
| `--dedup`     | Remove exact duplicate rows            |
| `--dry-run`   | Show planned changes without saving    |

---

## 📊 Sample Report Output

```json
{
  "input_file": "dirty.csv",
  "rows_before": 1300,
  "rows_after": 1180,
  "null_columns": {
    "email": "34.5%",
    "address": "9.8%"
  },
  "duplicate_rows_removed": 50,
  "inferred_types": {
    "age": "int",
    "joined": "datetime"
  }
}
```

---

## Roadmap

* [ ] CLI MVP with core cleaning
* [ ] YAML config for reusable cleaning rules
* [ ] Optional HTML report (via Jinja2)
* [ ] SQLite export option
* [ ] Streamlit / FastAPI Web UI wrapper
* [ ] GitHub Action template

---

## 🤝 Contributing

Open issues or PRs if you'd like to contribute. This project is FOSS-first and built for students, analysts, and indie devs.

---

## 🧠 License

MIT — free to use, modify, and ship.

---

Made with caffeine and command-line love by [@chishxd](https://github.com/chishxd)