import psutil
import time
import wmi
from plyer import notification

def check_temperature():
    # Initialize the WMI interface
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")

    # Query the sensor data
    temperature_info = w.Sensor()

    cpu_temp = None
    gpu_temp = None

    # Extract CPU and GPU temperatures
    for sensor in temperature_info:
        if sensor.SensorType == 'Temperature':
            if 'CPU' in sensor.Name:
                cpu_temp = sensor.Value
            if 'GPU' in sensor.Name:
                gpu_temp = sensor.Value

    return cpu_temp, gpu_temp

def alert_user(component, temperature):
    notification.notify(
        title="Overheating Alert!",
        message=f"{component} temperature is too high: {temperature}°C",
        app_name="WinMonitor",
        timeout=10
    )

def monitor_temperatures(cpu_threshold=75, gpu_threshold=80):
    while True:
        cpu_temp, gpu_temp = check_temperature()

        if cpu_temp and cpu_temp > cpu_threshold:
            print(f"CPU temperature is too high: {cpu_temp}°C")
            alert_user("CPU", cpu_temp)

        if gpu_temp and gpu_temp > gpu_threshold:
            print(f"GPU temperature is too high: {gpu_temp}°C")
            alert_user("GPU", gpu_temp)

        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    monitor_temperatures()