import psutil
import time

def monitor_system(interval=0.5):
    print("Starting performance monitor...\n")
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=None)
            mem_info = psutil.virtual_memory().percent

            print(f"CPU Usage: {cpu_percent:5.1f}%   |   Memory Usage: {mem_info:5.1f}%")

            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_system()
