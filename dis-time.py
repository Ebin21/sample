import time
import datetime
import os

# Function to clear the console screen
# def clear_screen():
#     # Use 'cls' for Windows and 'clear' for macOS/Linux
#     os.system('cls' if os.name == 'nt' else 'clear')

print("Live Date and Time (Press Ctrl+C to stop):")
try:
    while True:
        # Get the current date and time
        now = datetime.datetime.now()
        # Format the date and time as a string (e.g., "2024-02-14 07:31:00")
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the time, overwriting the previous line using carriage return '\r'
        # and flushing the output immediately
        print(f"\r{formatted_time}", end="", flush=True)
        
        # Pause the loop for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    # Handle the user interruption (Ctrl+C)
    print("\nProgram stopped by user.")

