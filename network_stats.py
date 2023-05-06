import speedtest
import tkinter as tk
from tkinter import ttk, messagebox
import threading

def get_speedtest_results():
    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()
    download_speed = speedtester.download() / 1_000_000  # Convert to Mbps
    upload_speed = speedtester.upload() / 1_000_000  # Convert to Mbps
    ping = speedtester.results.ping
    return download_speed, upload_speed, ping

def display_speedtest_results():
    try:
        download_speed, upload_speed, ping = get_speedtest_results()
        results_text.set(f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps\nPing: {ping:.2f} ms")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while running the speed test: {e}")

def run_speedtest():
    start_button.config(state=tk.DISABLED)
    progress_bar.pack(pady=10)
    progress_bar.start()
    display_speedtest_results()
    progress_bar.stop()
    progress_bar.pack_forget()
    start_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Network Speed Test")
root.geometry("400x300")

results_text = tk.StringVar()

title_label = tk.Label(root, text="Network Speed Test", font=("Helvetica", 24))
title_label.pack(pady=20)

results_label = tk.Label(root, textvariable=results_text, font=("Helvetica", 18))
results_label.pack(pady=10)

progress_bar = ttk.Progressbar(root, mode="indeterminate", length=300)

start_button = tk.Button(root, text="Start Speed Test", font=("Helvetica", 14), command=lambda: threading.Thread(target=run_speedtest).start())
start_button.pack(pady=20)

root.mainloop()
