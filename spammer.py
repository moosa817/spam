import pyautogui, time
f = open("spam.txt","r")
input_text =  input("Type Go to run the program('go'): ")
if(input_text == "go"):
    time.sleep(5)
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")




        

