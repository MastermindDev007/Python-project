import webbrowser
import pyautogui
import time
import os

# Function to send multiple messages to a specific WhatsApp number
def send_message_to_number(phone_number, message, repeat_count):
    # Step 1: Open WhatsApp Web with the target phone number
    webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}")

    # Step 2: Wait for WhatsApp Web to load and chat to be ready (adjust if needed)
    print("Waiting for WhatsApp Web to load...")
    time.sleep(20)  # Adjust based on your internet speed and system performance

    # Step 3: Send the message multiple times by typing and pressing Enter
    for _ in range(repeat_count):
        pyautogui.typewrite(message)  # Type the message
        pyautogui.press("enter")  # Press 'Enter' to send the message
        time.sleep(0.5)  # Add a small delay between each message

    # Step 4: Close the browser window after sending messages
    print("Closing WhatsApp Web...")
    pyautogui.hotkey('ctrl', 'w')  # This will close the current browser tab
    time.sleep(1)  # Give time for the browser to close properly


# Example usage
phone_number = "+91 9925723400"  # Replace with the target phone number, include country code
message = "Hi "  # The message you want to send
repeat_count = 10  # Number of times you want to send the message

send_message_to_number(phone_number, message, repeat_count)
