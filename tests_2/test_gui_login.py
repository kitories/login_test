import subprocess
import time
import pyautogui
import pytest

@pytest.mark.gui
def test_login_success():
    # Άνοιγμα του GUI (προσαρμόζεις το path)
    proc = subprocess.Popen(["python", "login_gui.py"])
    
    time.sleep(1)  # περιμένουμε να ανοίξει το παράθυρο

    # Πληκτρολόγηση username και password
    pyautogui.write("admin")
    pyautogui.press("tab")  # πάμε στο πεδίο password
    pyautogui.write("1234")
    pyautogui.press("enter")  # πατάμε Enter για login

    time.sleep(1)  # περιμένουμε το messagebox

    # Κλείσιμο του messagebox με Enter
    pyautogui.press("enter")

    # Κλείσιμο του GUI
    proc.terminate()