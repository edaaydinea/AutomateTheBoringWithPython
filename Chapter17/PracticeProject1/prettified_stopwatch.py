import time
import pyperclip

def prettified_stopwatch():
    print("Press ENTER to begin. Afterward, press ENTER to 'click' the stopwatch. Press Ctrl-C to quit.")
    input()  # press Enter to begin
    print("Started!")
    
    start_time = time.time()  # get the first lap's start time
    last_time = start_time
    lap_num = 1
    lap_data = []
    
    try:
        while True:
            input()  # press Enter for each lap
            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            lap = f"Lap #{str(lap_num).rjust(2)}: {str(total_time).ljust(6)} ({str(lap_time).rjust(6)})"
            print(lap)
            lap_data.append(lap)
            
            lap_num += 1
            last_time = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        # If the user hits Ctrl-C, stop the stopwatch and exit.
        print("\nStopwatch stopped.")
        
        # Copy the lap data to the clipboard
        pyperclip.copy("\n".join(lap_data))
        print("Lap data copied to clipboard.")

if __name__ == "__main__":
    prettified_stopwatch()
