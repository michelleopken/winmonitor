# WinMonitor

WinMonitor is a Python application that monitors the CPU and GPU temperatures on Windows machines. It provides alerts when the temperatures exceed specified thresholds, helping to prevent overheating and potential hardware damage.

## Features

- Monitors CPU and GPU temperatures using the Open Hardware Monitor library.
- Provides desktop notifications when temperatures exceed safe limits.
- Configurable temperature thresholds for CPU and GPU.

## Requirements

- Python 3.x
- `psutil` package
- `wmi` package
- `plyer` package
- [Open Hardware Monitor](https://openhardwaremonitor.org/) must be running in the background to provide temperature data.

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Install the required Python packages using pip:
   ```bash
   pip install psutil wmi plyer
   ```
3. Download and run [Open Hardware Monitor](https://openhardwaremonitor.org/).

## Usage

1. Clone this repository or download the `winmonitor.py` file.
2. Open a terminal and navigate to the directory containing `winmonitor.py`.
3. Run the script:
   ```bash
   python winmonitor.py
   ```

## Configuration

You can modify the CPU and GPU temperature thresholds by editing the `monitor_temperatures` function in `winmonitor.py`:

```python
monitor_temperatures(cpu_threshold=75, gpu_threshold=80)
```

Adjust the values for `cpu_threshold` and `gpu_threshold` as needed.

## License

This project is licensed under the MIT License.