import pyautogui, time
f = open("spam.txt","r")
input_text =  input("Type Go to run the program('go'): ")
if(input_text == "go"):
    print("Switch to text area you have 10 seconds")
    time.sleep(12)
    for word in f:
        time.sleep(1)
        pyautogui.typewrite(word)
        pyautogui.press("enter")




        

