✅ README.md
markdown
Kopiuj
Edytuj
# ukb-matzieb-datacodingDownloader

Simple Python tool to download and display `data_coding` metadata tables from the UK Biobank Showcase.

This project was created to easily fetch and inspect the meaning of categorical codings used across phenotypic fields in the UK Biobank dataset.

---

## 📦 Project Structure

ukb-matzieb-datacodingDownloader/ ├── main.py # Minimal test script for the function ├── setup_venv.sh # Script to set up virtual environment and project structure ├── requirements.txt # Python dependencies ├── results/ │ └── data-coding/ # Folder for saving downloaded metadata (optional) └── utils/ ├── init.py └── ukb_functions.py # Core function: get_data_coding_ukb

yaml
Kopiuj
Edytuj

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ukb-matzieb-datacodingDownloader.git
cd ukb-matzieb-datacodingDownloader
2. Set up virtual environment and install dependencies
bash
Kopiuj
Edytuj
chmod +x setup_venv.sh
./setup_venv.sh
This will:

create a .venv/ virtual environment,

install required packages (pandas, requests, beautifulsoup4, openpyxl),

create a basic .gitignore,

prepare utils/__init__.py and result folders.

3. Run test example
bash
Kopiuj
Edytuj
source .venv/bin/activate
python main.py
This will download metadata for data_coding=2 (as a basic test) and print the top rows.

🧠 Function Overview
Function name: get_data_coding_ukb

Location: utils/ukb_functions.py

Parameters:
data_coding (str or int) – ID of the data_coding to retrieve

number_attempts (default=5) – how many times to retry on failure

time_duration (default=5) – seconds between retries

Returns:
pandas.DataFrame – data coding table with values and meanings (or None if failed)

🧪 Example
python
Kopiuj
Edytuj
from utils.ukb_functions import get_data_coding_ukb

df = get_data_coding_ukb(100292)

if df is not None:
    print(df.head())
else:
    print("No data returned.")
📋 Requirements
See requirements.txt. Minimal dependencies:

pandas

requests

beautifulsoup4

openpyxl

✍️ Author
Mateusz Zięba
Doctoral student at the Institute of Pharmacology, Polish Academy of Sciences
Focus: Computational genomics & UK Biobank analysis

📄 License
This project is open source. Use it freely for research purposes.

