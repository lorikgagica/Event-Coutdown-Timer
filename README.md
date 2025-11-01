# ⏲️ Multi Countdown Timer

A Python console app to manage and run multiple simultaneous countdowns.  
Each countdown can be named and set to a different future date and time.  
An audible alert lets you know when each countdown finishes!

---

## ✨ Features

- **Add as many countdowns as you like** — each with a custom name and target time.
- **All countdowns run simultaneously** and are displayed in real time.
- **Sound alert** when each countdown reaches zero (works on Windows, beeps in other terminals).
- **Easy menu:** You are prompted for a first countdown, then you can add more as you wish.

---

## 🚀 How to Use

1. Make sure Python is installed (Windows users get a beep alert; others get a bell).
2. Save your script as `countdown.py`.
3. Run the app in your terminal/command prompt: `python countdown.py`
4. Enter the name and target date/time for your first countdown:
    - **Example:**  
      `Enter a name/description for the countdown: Pizza`  
      `Enter event date and time (YYYY-MM-DD HH:MM:SS): 2025-11-01 21:00:00`
5. After the first, you’ll be asked "Add another countdown? (y/n)" as many times as you want.
6. All countdowns will start and be shown together.

---

## 💡 Example Session

Set up your first countdown:
Enter a name/description for the countdown: Pizza
Enter event date and time (YYYY-MM-DD HH:MM:SS): 2025-11-01 21:00:00
Add another countdown? (y/n): y
Enter a name/description for the countdown: Laundry
Enter event date and time (YYYY-MM-DD HH:MM:SS): 2025-11-01 21:10:00
Add another countdown? (y/n): n

--- Starting all countdowns ---
Pizza: 0d 0h 44m 55s remaining.
Laundry: 0d 0h 54m 55s remaining.

Pizza: Countdown Complete!
Laundry: Countdown Complete!
All countdowns complete!

---

## 👂 Sound Support

- On Windows, a beep is played at the end of each countdown.
- On macOS/Linux, your terminal bell will sound.

---

## 📄 License

MIT License — free to use and share.

---

Never forget a task, call, or treat in the oven!
