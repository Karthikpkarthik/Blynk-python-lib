import network
import BlynkLib
import time

#Use your  WiFi credentials
SSID = 'underdogRox11'
PASSWORD = '123456789@'

# Blynk auth token from your project
BLYNK_AUTH = 'M3Ny8Gfugn2Snb9R_65h7e7xtDp_jL'

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
print('Connecting to WiFi...', end='')
while not wlan.isconnected():
    print('.', end='')
    time.sleep(1)
print(' Connected!')
print('Network config:', wlan.ifconfig())

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Main loop
while True:
    try:
        blynk.run()
        blynk.virtual_write(3, "Hello from ESP32!")
    except Exception as e:
        print("An error occurred:", e)
    time.sleep(0.1)

