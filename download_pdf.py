import requests

url = "https://sample-files.com/downloads/documents/pdf/basic-text.pdf"

response = requests.get(url)

print("Status code:", response.status_code)

if response.status_code == 200:
    with open("basic-text.pdf", "wb") as file:
        file.write(response.content)

    print("PDF downloaded successfully!")
else:
    print("Failed to download PDF")
