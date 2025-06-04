import tkinter as tk

# Button click function
def press(value):
    current = input_text.get()
    input_text.set(current + str(value))

def clear():
    input_text.set("")

def equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

# Create root window
root = tk.Tk()
root.title("🧮 Calculator")
root.geometry("360x500")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

input_text = tk.StringVar()

# Input Display
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=20)

input_box = tk.Entry(input_frame, textvariable=input_text, font=("Helvetica", 24), width=22, bd=0,
                     justify="right", relief="flat", bg="#ffffff", fg="#333")
input_box.pack(ipady=15, padx=10)

# Create Button Frame
btns_frame = tk.Frame(root, bg="#f4f4f4")
btns_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('=',)
]

# Button styling function
def create_btn(parent, text, color="#e0e0e0", text_color="#333", font_size=16):
    return tk.Button(
        parent,
        text=text,
        font=("Helvetica", font_size, "bold"),
        bg=color,
        fg=text_color,
        bd=0,
        height=2,
        width=6,
        cursor="hand2",
        activebackground="#d0d0d0",
        relief="flat",
        command=lambda: press(text) if text not in ['C', '='] else (clear() if text == 'C' else equal())
    )

# Build Buttons
for row in buttons:
    row_frame = tk.Frame(btns_frame, bg="#f4f4f4")
    row_frame.pack(pady=5)
    for btn in row:
        if btn == "=":
            create_btn(row_frame, btn, color="#4CAF50", text_color="white", font_size=18).pack(
                side="left", expand=True, fill="both", padx=6, pady=2
            )
        elif btn == "C":
            create_btn(row_frame, btn, color="#f44336", text_color="white").pack(
                side="left", expand=True, fill="both", padx=6, pady=2
            )
        else:
            create_btn(row_frame, btn).pack(side="left", expand=True, fill="both", padx=6, pady=2)

# Footer
footer = tk.Label(root, text="✨ Made with Tkinter", font=("Helvetica", 9), bg="#f4f4f4", fg="#999")
footer.pack(side=tk.BOTTOM, pady=10)

# Start App
root.mainloop()