# Multi Countdown Timer with Sound Alert

from datetime import datetime, timedelta
import threading
import time
import sys

# Step 1: Prepare for sound alert
try:
    import winsound
    SOUND = True
except ImportError:
    SOUND = False

# Step 2: Get event name and date/time from user
def get_event():
    name = input("Enter a name/description for the countdown: ")
    try:
        date_str = input("Enter event date and time (YYYY-MM-DD HH:MM:SS): ")
        event_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        return name, event_dt
    except ValueError:
        print("Invalid date format. Please try again.")
        return None, None

# Step 3: Calculate time remaining
def time_remaining(event_dt):
    now = datetime.now()
    return event_dt - now

# Step 4: Play sound alert
def play_alert():
    if SOUND:
        winsound.Beep(1000, 800)
    else:
        sys.stdout.write('\a')
        sys.stdout.flush()

# Step 5: Countdown logic for one timer (to run in thread)
def countdown_worker(name, event_dt):
    while True:
        left = time_remaining(event_dt)
        if left.total_seconds() <= 0:
            print(f"\n{name}: Countdown Complete!")
            play_alert()
            break
        days = left.days
        hours, rem = divmod(left.seconds, 3600)
        mins, secs = divmod(rem, 60)
        print(f"{name}: {days}d {hours}h {mins}m {secs}s remaining.", end='\r')
        time.sleep(1)

# Step 6: Main program loop for multiple timers
def main():
    countdowns = []

    # Always ask for the first countdown
    print("Set up your first countdown:")
    while True:
        name, dt = get_event()
        if name and dt:
            countdowns.append((name, dt))
            break

    # Now offer to add further countdowns
    while True:
        add_more = input("Add another countdown? (y/n): ").lower().strip()
        if add_more == 'y':
            name, dt = get_event()
            if name and dt:
                countdowns.append((name, dt))
        else:
            break

    if not countdowns:
        print("No countdowns to run.")
        return
    print("\n--- Starting all countdowns ---")
    threads = []
    for name, dt in countdowns:
        t = threading.Thread(target=countdown_worker, args=(name, dt))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("\nAll countdowns complete!")

# Step 7: Start the program
if __name__ == "__main__":
    main()