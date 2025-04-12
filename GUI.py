from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import weather
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")


def ask():
    user_val = speech_to_text.speech_to_text()

    if user_val is None:
        text.insert(END, "You: [No input detected]\n")
        

    bot_val = action.Action(user_val)
    text.insert(END, "You: " + user_val + "\n")

    if bot_val is not None:
        text.insert(END, "AI Assistant: " + str(bot_val) + "\n")

    if bot_val == "ok maam":
        root.destroy()

def delete ():
    text.delete(1.0, END)


def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "You: " + send + "\n") 
    if bot != None:
        text.insert(END, "AI Assistant: " + str(bot) + "\n")
    if bot == "ok maam":
        root.destroy()



# frame

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=0, columnspan=2, padx=55, pady=10)  # Span across two columns

# text label

text_label = Label(frame, text="AI Assistant", font=("Georgia", 20, "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

# image label

image = ImageTk.PhotoImage(Image.open("image/image.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=10)

# text frame

text = Text(root, font=("Georgia", 12), bg="#356696", width=200, height=5) # Adjusted width
text.grid(row=2, column=0, columnspan=2, padx=100, pady=20)


# Configure column weights to center the frame
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

 
 #entry widget

entry =Entry(root,justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#BUTTON 1

Button1 = Button(root, text="ASK", font=("Georgia", 12), bg="#356696", pady=16,padx=40,borderwidth=3,relief=SOLID, command=ask)
Button1.place(x=70, y=575)



#BUTTON 2

Button2 = Button(root, text="DELETE", font=("Georgia", 12), bg="#356696", pady=16,padx=30,borderwidth=3,relief=SOLID, command=delete)
Button2.place(x=400, y=575)



#BUTTON 3

Button3 = Button(root, text="SEND", font=("Georgia", 12), bg="#356696", pady=16,padx=40,borderwidth=3,relief=SOLID, command=send)
Button3.place(x=225, y=575)








root.mainloop()