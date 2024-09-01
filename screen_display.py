import cv2
import numpy as np
import pyautogui
import logging

logging.basicConfig(level=logging.INFO)

def capture_screen():
    # Capture the screen using pyautogui
    try:
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    except Exception as e:
        logging.error(f"Error capturing screen: {e}")
        return None

def main():
    window_name = "Screen Capture"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window_name, 100, 100)  # Adjust the position of the window

    while True:
        frame = capture_screen()
        if frame is not None:
            cv2.imshow(window_name, frame)
        else:
            logging.error("Failed to capture the screen.")
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
