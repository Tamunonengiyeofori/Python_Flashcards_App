from tkinter import*
import pandas
from random import*
BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
current_card = {}

try:
    words_data= pandas.read_csv("data/words_to_learn_french.csv")
except FileNotFoundError:
    print("File not found !!!")
    main_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = main_data.to_dict(orient="records")
    print(main_data)
else:
    words_to_learn = words_data.to_dict(orient="records")
 
# french_word = True

    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words_to_learn) 
    canvas.itemconfig(card_title , text="French" , fill="black")
    canvas.itemconfig(card_text , text=current_card["French"] , fill="black")
    canvas.itemconfig(card_image , image=card_front_img)
    flip_timer = window.after(3000 , func=flip_card) 
    
def is_known():
    words_to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn_french.csv" , index=False)
    
    
def flip_card():
    # global french_word
    # if french_word:
    canvas.itemconfig(card_image , image=card_back_img)
    canvas.itemconfig(card_title , text="English" , fill="white")
    canvas.itemconfig(card_text , text=current_card["English"] , fill="white")
        # french_word = False
    # else:
    #     if not french_word:
    #         canvas.itemconfig(card_image , image=card_front_img)
    #         canvas.itemconfig(card_title , text="French" , fill="black")
    #         canvas.itemconfig(card_text , text=current_card["French"] , fill="black")
    #         french_word = True
        
# ------------------------------------ UI SETUP ---------------------------------- 
window = Tk()
window.title("Flashy")
window.config(padx=50 , pady=50, bg=BACKGROUND_COLOR)

# Create a timer variable and make it wait 3secs before flipping card
flip_timer = window.after(3000 , func=flip_card)

# Creating canvas for flash card
canvas = Canvas(width=800 , height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100 , text="" , font=("Ariel" , 40 , "italic"))
card_text = canvas.create_text(400, 263 , text="" , font=("Ariel" , 60 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row=0 , column=0, columnspan=2)

card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Buttons
correct_button = Button(image=right_img)
correct_button.config(bg=BACKGROUND_COLOR , highlightthickness=0 , command=is_known)
correct_button.grid(row=1 , column=1)
wrong_button = Button(image=wrong_img)
wrong_button.config(bg=BACKGROUND_COLOR , highlightthickness=0 , command=next_card)
wrong_button.grid(row=1 , column=0)

next_card()

window.mainloop()

