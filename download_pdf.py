# download_pdf.py

import requests

# Direct PDF link (no need for browser automation)
url = "https://stock.audi.bg/pdf/offer/A-2024-0234633-BG.pdf"

# Download the file
response = requests.get(url)
response.raise_for_status()  # Raise error if download fails

# Save it locally
with open("audi-offer.pdf", "wb") as f:
    f.write(response.content)

print("✅ PDF downloaded successfully")
