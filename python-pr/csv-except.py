import requests
import csv

url = input("Enter Your Url: ")

try:
    resp = requests.get(url)
    with open('status.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL_ADDR", "STATUS" , "server"])
        writer.writerow([url,resp.status_code, resp.headers.get('Server', 'Unkown')])
    print("CSV File Created Successfully")
except requests.exceptions.RequestEceptions as e:
    print(f"Server unreachable or requests failed: {e}")
except Exception as e:
    print(f"an error occured: {e}")