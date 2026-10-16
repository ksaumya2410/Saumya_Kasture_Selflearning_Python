
import time
import schedule
from plyer import notification


# Function to display a desktop notification
def send_break_alert(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )


# Schedule hydration reminders every 10 seconds for testing
schedule.every(10).seconds.do(
    send_break_alert,
    title="Hydration Alert",
    message="Drink some water and stay hydrated!"
)

# Schedule posture reminders every 20 seconds
schedule.every(20).seconds.do(
    send_break_alert,
    title="Posture Check",
    message="Sit straight, relax your shoulders, and take a short break."
)


# Continuous background listener
print("Desktop Health & Break Reminder Daemon started.")
print("Hydration reminder: every 10 seconds (testing).")
print("Posture reminder: every 20 seconds.")
print("Press Ctrl+C to stop the program.")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReminder daemon stopped safely. Stay healthy!")
