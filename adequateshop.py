import os
import requests
import time

# URL and output directory
BASE_URL = "http://restapi.adequateshop.com/api/Traveler?page="
OUTPUT_DIR = "traveler_responses"

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Log file to record results
log_file_path = "test_results.log"
with open(log_file_path, "w", encoding="utf-8") as log_file:
    log_file.write("Page\tStatus Code\tResponse Time\n")

# Fetch 100 pages
for page in range(100):
    url = f"{BASE_URL}{page}"
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time

        # Log the results
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"{page}\t{response.status_code}\t{response_time:.2f}\n")

        # Check if the response is successful and save content
        if response.status_code == 200 and response_time < 1:
            file_path = os.path.join(OUTPUT_DIR, f"page_{page}.xml")
            with open(file_path, "w", encoding="utf-8") as xml_file:
                xml_file.write(response.text)

        else:
            print(f"Page {page}: Unexpected status or timeout (Code: {response.status_code}, Time: {response_time:.2f}s)")

    except Exception as e:
        print(f"Error fetching page {page}: {e}")

print("Test completed. Check the log file and output directory for details.")
