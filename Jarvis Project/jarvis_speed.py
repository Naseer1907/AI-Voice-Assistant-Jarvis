# jarvis_speed.py
import speedtest

def get_speed():
    wifi = speedtest.Speedtest()
    download = wifi.download() / 1048576  # Convert to Mbps
    upload = wifi.upload() / 1048576
    return download, upload
