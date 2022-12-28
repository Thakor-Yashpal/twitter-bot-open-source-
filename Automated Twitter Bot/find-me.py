import pyttsx3
import platform
import subprocess

def find_my_phone():
  # Get the current operating system
  os = platform.system()

  # Find the IP address of the phone
  if os == "Windows":
    ip_address = subprocess.run(["ipconfig"], capture_output=True).stdout.decode("utf-8")
  elif os == "Darwin":
    ip_address = subprocess.run(["ifconfig"], capture_output=True).stdout.decode("utf-8")
  elif os == "Linux":
    ip_address = subprocess.run(["ifconfig"], capture_output=True).stdout.decode("utf-8")
  else:
    ip_address = "Unable to find IP address"

  # Use text-to-speech to announce the IP address
  engine = pyttsx3.init()
  engine.say("The IP address of your phone is: " + ip_address)
  engine.runAndWait()

find_my_phone()
