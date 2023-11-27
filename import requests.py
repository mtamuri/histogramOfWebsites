import requests
import time
import csv

def check_google_response_time():
    start_time = time.perf_counter()
    response = requests.get("https://www.google.com")
    end_time = time.perf_counter()
    response_time = end_time - start_time

    with open('google_response_times.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([response_time])

if __name__ == "__main__":
    for _ in range(3):
        check_google_response_time()
        time.sleep(5)
