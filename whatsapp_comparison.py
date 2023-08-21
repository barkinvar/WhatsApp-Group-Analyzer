from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import analyzer

# Set up Chrome options to use a specific user data directory
options = Options()
options.add_argument("user-data-dir=/tmp/tarun")

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then hit Enter")
input()

# List of groups
groups = [
    "Group1",
    "Group2",
    "Group3"
]

mainName = "Community"
getFromCommunity = False

# Get names from the community
if getFromCommunity:
    names = sorted(analyzer.getNamesFromCommunity(driver, mainName))
# Get names from the group
else:
    names = sorted(analyzer.getNamesFromGroup(driver, mainName))

# Create an empty DataFrame with columns from groups and index from names
df = pd.DataFrame(columns=groups, index=names)
df = df.fillna(0)

# Loop through groups and names to populate the DataFrame
for group in groups:
    specNames = analyzer.getNamesFromGroup(driver, group)
    for name in names:
        if name in specNames:
            df.loc[name, group] = 1

# Write the DataFrame to a CSV file
df.to_csv("data.csv", header="Main Group: " + mainName)

driver.quit()
