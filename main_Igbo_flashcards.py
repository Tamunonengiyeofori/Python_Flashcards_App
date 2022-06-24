from tkinter import*
import pandas
from random import*
BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
current_card = {}

try: 
    word_data = pandas.read_csv("data/words_to_learn_igbo.csv")
except FileNotFoundError:
    main_data = pandas.read_csv("data/igbo_words.csv")
    words_to_learn = main_data.to_dict(orient="records")
else:
    words_to_learn = word_data.to_dict(orient="records")

    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn)
    canvas.itemconfig(card_title , text="Igbo" , fill="black")
    canvas.itemconfig(card_text , text=current_card["Igbo"] , fill="black")
    canvas.itemconfig(card_image , image=card_front_img)
    flip_timer = window.after(3000 , func=flip_card)
    
def is_known():
    print("I know IT !!!!")
    words_to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn_igbo.csv")
    
def flip_card():
    canvas.itemconfig(card_image , image=card_back_img)
    canvas.itemconfig(card_title , text="English" , fill="white")
    canvas.itemconfig(card_text , text=current_card["English"] , fill="white")
    
    
        
# ------------------------------------ UI SETUP ---------------------------------- 
window = Tk()
window.title("Flashy")
window.config(padx=50 , pady=50 , bg=BACKGROUND_COLOR)

flip_timer = window.after(3000 , func=flip_card)

canvas = Canvas(width=800 , height=526 , bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0 , column=0 , columnspan=2)
card_front_img = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400 , 263 , image=card_front_img)
card_back_img = PhotoImage(file="images/card_back.png")
correct_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

card_title = canvas.create_text(400 , 100 , text="" , font=("Ariel" , 40 , "italic"))
card_text = canvas.create_text(400, 263 , text="" , font=("Ariel" , 60 , "bold"))

# Create buttons
right_button = Button(image=correct_img , command=is_known)
right_button.grid(row=1 , column=1)
wrong_button = Button(image=wrong_img , command=next_card)
wrong_button.grid(row=1 , column=0)
next_card()
window.mainloop()


