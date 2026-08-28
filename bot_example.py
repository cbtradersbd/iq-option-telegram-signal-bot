# IQ Option Telegram Signal Dispatcher
import requests

API_URL = "https://api1.api.cbtraderbd.xyz/docs"

def send_alert(signal):
    print(f"🚀 [SIGNAL ALERT] Pair: {signal['pair']} | Direction: {signal['direction']} | Expiry: {signal['expiry']}")

if __name__ == "__main__":
    sample_signal = {"pair": "EURUSD-OTC", "direction": "CALL (UP)", "expiry": "1 MIN", "accuracy": "92%"}
    send_alert(sample_signal)
