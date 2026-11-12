import argparse
import csv
import requests


def urlhaus_fetch(output_file):
  url = "https://urlhaus-api.abuse.ch/v1/urls/recent/"

  # Headers dictionary with correct Auth-Key
  headers = {
      "Auth-Key": "",
      "User-Agent": "CTI-Script/1.0",
  }

  print(f"[*] Fetching recent malicious URLs feed from URLhaus...")

  try:
    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("query_status") == "ok":
      url_list = data.get("urls", [])

      with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["SERVICE_URL", "STATUS_URL", "HOST", "DATE"])

        count = 0
        for entry in url_list:
          writer.writerow([
              entry.get("url"),
              entry.get("url_status"),
              entry.get("host"),
              entry.get("date_added"),
          ])
          count += 1

      print(
          f"[+] Success! CSV file created. Total URLs saved: {count} to"
          f" '{output_file}'"
      )
    else:
      print(f"[-] API Error: {data.get('query_status')}")

  except requests.exceptions.RequestException as e:
    print(f"⚠️ Server unreachable or request failed: {e}")
  except Exception as e:
    print(f"⚠️ An error occurred: {e}")


if __name__ == "__main__":
  parser = argparse.ArgumentParser(
      description=(
          "URLhaus Threat Intelligence Fetcher - Pulls recent malicious URLs"
          " and exports to CSV"
      )
  )
  parser.add_argument(
      "-o",
      "--output",
      default="url-haus.csv",
      help=(
          "Specify the output CSV filename (default: url-haus.csv) [e.g., -o"
          " threat_feed.csv]"
      ),
  )

  args = parser.parse_args()
  urlhaus_fetch(args.output)