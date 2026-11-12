import requests

url = "https://ipapi.co/8.8.8.8/json/"

try:
    resp = requests.get(url, headers={"User-Agent": "CTI-Script/1.1"} , timeout=5)

    if resp.status_code == 200:
        data = resp.json()

        ip = data.get("ip")
        city = data.get("city")
        country = data.get("country")
        org = data.get("org")

        print(f"Target IP: {ip}")
        print(f"Target City: {city}")
        print(f"Target Country: {country}")
        print(f"Target organisation: {org}")
        # print(data) check types keys
    else:
        print(f"HTTP Error: {resp.status_code}")
except Exception as e:
    print(f"Something unknown: {e}")