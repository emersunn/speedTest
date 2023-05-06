# Network Speed Test

Are you tired of web-based speed tests? Try this simple and user-friendly Python script that utilizes the Speedtest CLI to check your network stats, and displays the results in a GUI using the Tkinter library.

## Features

- Download speed, upload speed, and ping measurement
- Easy-to-use graphical interface
- No need to rely on web-based speed test services

## Dependencies

- Python 3.6 or higher
- `speedtest-cli` package
- `Tkinter` library (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the `network_stats.py` file.
2. Install the `speedtest-cli` package using the following command:

   ```
   pip install speedtest-cli
   ```

## Usage

1. Run the `network_stats.py` script using the terminal:

   ```
   python network_stats.py
   ```

2. A GUI window will open, showing a "Start Speed Test" button. Click the button to start the speed test.
3. The download speed, upload speed, and ping will be displayed in the window after the test is completed.
