import pyautogui
import time

def type_string_with_delay(input_string, delay):
    # Wait for the specified delay
    print('Start delay')
    time.sleep(delay)
    print('end delay')
    # Type the input string using keyboard
    pyautogui.typewrite(input_string)

if __name__ == "__main__":
    input_string = "I believe I am an excellent fit for this role due to my comprehensive knowledge and practical experience in both fundamental and advanced aspects of machine learning. My proficiency in Python, combined with hands-on experience in web technologies such as Android, Web3, Flutter, React, and Node.js, allows me to develop versatile and efficient solutions. My eagerness to apply my skills in a real-world setting and my commitment to continuous learning will enable me to contribute effectively to your projects and objectives."
    delay = 5  # Adjust the delay as needed
    type_string_with_delay(input_string, delay)
