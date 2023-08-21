# WhatsApp Group Analyzer

The WhatsApp Group Analyzer project consists of Python scripts designed to facilitate the comparison of users between WhatsApp groups and a community. It utilizes the Selenium library for web automation to interact with the WhatsApp Web interface.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- Python 3.x
- Chrome browser
- ChromeDriver: Ensure that the version of ChromeDriver matches your Chrome browser version.

You can run pip install to ensure the prerequisites are installed:
```bash
pip install -r requirements.txt
```
## Setup

1. Download and install ChromeDriver: https://sites.google.com/chromium.org/driver/
2. Clone this repository or download the two Python scripts: `analyzer.py` and `whatsapp_comparison.py`.

## Usage

### Step 2: Configure Groups and Community

In `whatsapp_comparison.py`, find the following section:

```python
# List of groups
groups = [
    "Group1",
    "Group2",
    "Group3"
]

mainName = "Community"
getFromCommunity = False
```
Replace the example group names with the names of the WhatsApp groups you want to compare. Adjust the list as needed. Than change the `mainName` to the main group or community name that you would like to names to be fetched. Change `getFromCommunity` to True if name belongs to a community rather than group.

### Step 3: Running the Scripts

1. Open a terminal and navigate to the directory containing the scripts.
2. Run the whatsapp_comparison.py script:

```bash
python3 whatsapp_comparison.py
```

1. Scan the QR code using your WhatsApp mobile app as prompted.
2. After scanning the QR code, press Enter in the terminal.
The script will then proceed to gather user data from the specified groups and community and create a CSV file named data.csv containing the comparison results.

## Result
The generated data.csv file will have rows representing users from the community and columns representing each group. A value of 1 in a cell indicates that the user is a member of the corresponding group, while 0 indicates that they are not.

## License
This project is licensed under the MIT License

## Acknowledgments
This script is for educational and informational purposes only. Use it responsibly and in accordance with WhatsApp's terms of use.
The scripts utilize the Selenium library to interact with the WhatsApp Web interface. Any changes to the WhatsApp Web structure may impact the functionality of the scripts.
