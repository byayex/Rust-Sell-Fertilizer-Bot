import win32api, win32con, pyautogui, time, random
import datetime

x_min, x_max = 1455, 1512
y_min, y_max = 905, 930

input_x_min, input_x_max = 1461, 1510
input_y_min, input_y_max = 950, 960

# Wait so we can open the menu
time.sleep(5)

while True:
    time.sleep(random.randint(1,4))
    # Still in the shop check
    check_shop = pyautogui.pixel(1466,920)
    if check_shop == (115, 141, 69) or check_shop == (110, 135, 66):
        current_time = datetime.datetime.now()
        print('------------------')
        print('Current Time: %s:%s:%s' % (current_time.hour, current_time.minute, current_time.second))
        print('Detected new Stock -> Start Selling now!')
        time.sleep(random.randint(1,3))
        # Select the random of the input, to put mouse to
        input_x, input_y = random.randint(input_x_min, input_x_max), random.randint(input_y_min, input_y_max)
        # Move to the Input Field
        pyautogui.moveTo(input_x, input_y, random.random(), pyautogui.easeOutQuad)
        # Click it
        pyautogui.leftClick()
        # Input high amount to sell, so it sells the max amount, wait 0.1-0.3 seconds per input
        pyautogui.press(str(random.randint(1,9)))
        time.sleep(random.randint(1,2)/10)
        pyautogui.press(str(random.randint(1,9)))
        time.sleep(random.randint(1,2)/10)
        pyautogui.press(str(random.randint(1,9)))
        time.sleep(random.randint(1,2)/10)
        # Select the random of the click, to put mouse to.
        click_x, click_y = random.randint(x_min, x_max), random.randint(y_min, y_max)
        # Move Button to the sell button
        pyautogui.moveTo(click_x, click_y, random.random(), pyautogui.easeOutQuad)
        pyautogui.leftClick()
        print("Sold successfully!")
        pyautogui.moveTo(random.randint(250, 1150), random.randint(133,920), random.random(), pyautogui.easeOutQuad)
        print("Moving back to idle position")
        print('------------------')

    # Move mouse sometimes
    rand = random.randint(0,10)
    if rand == 1:
        print("Moving mouse randomly, to prevent detection!")
        pyautogui.moveTo(random.randint(250, 1150), random.randint(133,920), random.random(), pyautogui.easeOutQuad)