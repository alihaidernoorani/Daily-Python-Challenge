from datetime import datetime, timedelta
import pygame
import os
import time

# Initialize pygame mixer
pygame.mixer.init()

# Function to validate time format
def validate_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False

# List to store alarms
alarms = []

# Get MP3 file from user
while True:
    alarm_sound = input("Enter the path to your alarm sound (MP3 file): ").strip()
    if os.path.isfile(alarm_sound) and alarm_sound.lower().endswith('.mp3'):
        try:
            pygame.mixer.music.load(alarm_sound)
            print(f"Loaded alarm sound: {alarm_sound}")
            break
        except pygame.error:
            print("Failed to load the MP3 file. Try again.")
    else:
        print("Invalid file. Please provide a valid MP3 file.")

# Set alarms
while True:
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    if validate_time(alarm_time):
        alarms.append(alarm_time)
    else:
        print("Invalid time format. Please enter time in HH:MM:SS format.")
        continue
    
    another_alarm = input("Do you want to set another alarm (Yes/no)? ").strip().lower()
    if another_alarm != 'yes':
        break

# Alarm loop
print("⏳ Waiting...")
while alarms:
    current_time = datetime.now().strftime('%H:%M:%S')
    for alarm in alarms[:]:
        if current_time == alarm:
            print("⏰ Time's up! Wake up! 🔔")
            pygame.mixer.music.play()
            
            snooze = input("Do you want to snooze the alarm (Yes/no)? ").strip().lower()
            if snooze == 'yes':
                new_alarm = (datetime.now() + timedelta(seconds=300)).strftime('%H:%M:%S')
                alarms.append(new_alarm)
                print(f"Snoozed for 5 minutes! New alarm set for {new_alarm}.")
                pygame.mixer.music.stop()
            alarms.remove(alarm)
    
    time.sleep(1)
