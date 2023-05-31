import tkinter as tk
from PIL import Image, ImageTk
import socket

HOST = 'localhost'
PORT = 65500

#------------------------ Global variables
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

#----------------------- Creating a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connecting to the server
    s.connect((HOST, PORT))

    window = tk.Tk()
    window.geometry("300x500")
    window.title("Scissor Paper Rock @Diwas ")

    image = Image.open('aa.jpeg')
    image.thumbnail((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=photo)
    label_image.grid(column=15, row=0)



    def send_choice(choice):
        # Sending the user's choice to the server
        s.sendall(choice.encode('utf-8'))

    def choice_to_number(choice):
        rps = {'scissor': 0, 'paper': 1, 'rock': 2}
        return rps.get(choice, -1)

    def number_to_choice(number):
        rps = {0: 'scissor', 1: 'paper', 2: 'rock'}
        return rps[number]

    def result(human_choice, comp_choice):
        global USER_SCORE
        global COMP_SCORE 
        user = choice_to_number(human_choice)
        comp = choice_to_number(comp_choice)

        if (comp == -1 | user == comp):
            return "Tie"
        elif (user - comp) % 3 == 1:
            USER_SCORE += 1
            return "You win"
        else:
            COMP_SCORE += 1
            return "Comp wins"

    # Text area
    text_area = tk.Text(master=window, height=12, width=30, bg='light gray')
    text_area.grid(column=15, row=4)

    # Event Handling
    def rock():
        USER_CHOICE = 'rock'
        COMP_CHOICE = s.recv(1024).decode('utf-8')
        game_result = result(USER_CHOICE, COMP_CHOICE)

        # Update text area
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"Your Choice: {USER_CHOICE}\nComputer's Choice: {COMP_CHOICE}\nResult: {game_result}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}\n")

    def paper():

        USER_CHOICE = 'paper'
        COMP_CHOICE = s.recv(1024).decode('utf-8')
        game_result = result(USER_CHOICE, COMP_CHOICE)

        # Update text area
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"Your Choice: {USER_CHOICE}\nComputer's Choice: {COMP_CHOICE}\nResult: {game_result}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}\n")

    def scissor():

        USER_CHOICE = 'scissor'
        COMP_CHOICE = s.recv(1024).decode('utf-8')
        game_result = result(USER_CHOICE, COMP_CHOICE)

        # Update text area
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, f"Your Choice: {USER_CHOICE}\nComputer's Choice: {COMP_CHOICE}\nResult: {game_result}\nYour Score: {USER_SCORE}\nComputer Score: {COMP_SCORE}\n")

    # Buttons
    button1 = tk.Button(text="       Scissor         ", bg="yellow", command=lambda: [send_choice('scissor'), scissor()], height=1, width=8, font=('arial', 15, 'bold'))
    button1.grid(column=15, row=1)
    button2 = tk.Button(text="        Paper          ", bg="blue", command=lambda: [send_choice('paper'), paper()], height=1, width=8, font=('arial', 15, 'bold'))
    button2.grid(column=15, row=2)
    button3 = tk.Button(text="         Rock          ", bg="purple", command=lambda: [send_choice('rock'), rock()], height=1, width=8, font=('arial', 15, 'bold'))
    button3.grid(column=15, row=3)

    window.mainloop()