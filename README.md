# AutoCleanSE (Auto Cleaner & Statistical Explorer)

![Project Status](https://img.shields.io/badge/status-in%20development-yellowgreen)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A Python command-line tool to automate the initial, tedious steps of data cleaning and exploration for any given dataset. This project is being built as part of an MSBTE AI/ML diploma curriculum.

## The Problem

Every data science project begins with the same repetitive tasks: loading the data, figuring out its shape, checking for errors, identifying missing values, and getting a basic statistical summary. `AutoCleanSE` aims to automate this entire process with a single command.

## Current Features

- **Load CSV Data:** Robustly loads a CSV file into a pandas DataFrame.
- **Generate Data Profile:** Provides a comprehensive summary of the dataset, including:
    - Shape (rows and columns)
    - Column names and data types
    - Percentage of missing values per column
    - Descriptive statistics for numerical columns
    - Unique value counts for categorical columns

## Installation & Setup

To get started, clone this repository and set up the environment using the commands below.

<details>
<summary><b>For Linux & macOS</b></summary>

```shell
# Clone the repository (if you haven't already)
# git clone https://github.com/chishxd/autocleanse.git
# cd autocleanse

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install pandas

# Download sample data
mkdir -p data
wget -O data/titanic_train.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
```
</details>

<details>
<summary><b>For Windows (PowerShell)</b></summary>

```powershell
# Clone the repository (if you haven't already)
# git clone https://github.com/chishxd/autocleanse.git
# cd autocleanse

# Create a Python virtual environment
py -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install pandas

# Download sample data
mkdir data
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv" -OutFile "data/titanic_train.csv"
```
</details>

## Usage

Run the profiler on the command line by passing the path to your CSV file as an argument. If no path is provided, it will default to the Titanic dataset.

```bash
python autocleanse.py data/titanic_train.csv
```

### Example Output

```text
[SUCCESS] Data loaded from data/titanic_train.csv

--- Data Profile ---
Shape (rows, columns): (891, 12)

Column Names:
  - PassengerId
  - Survived
  ...

Data Types:
PassengerId      int64
Survived         int64
...
dtype: object

Missing Values per Column:
PassengerId     0.00
Survived        0.00
...
Age            19.87
Cabin          77.10
Embarked        0.22
Name: Unnamed: 0, dtype: float64

--- End of Profile ---
```

## Project Roadmap

- [ ] **Feature:** Handle Missing Data (Imputation & Removal)
- [ ] **Feature:** Data Visualization (Histograms, Correlation Matrix)
- [ ] **Enhancement:** Export Profile Report to JSON/HTML

## Performance

The script's performance was tested on a large, synthetic 5-million-row dataset. The analysis showed the data cleaning process to be primarily **CPU-bound**. See the full experiment log here: `([link to your new Forge note](https://chishxd.github.io/diploma-notes/5th-Semester/The-Projects/Project-AutoCleanSE/03-OS-Performance-Testing-at-Scale))`.

## License

Distributed under the MIT License. See `LICENSE` for more information.
