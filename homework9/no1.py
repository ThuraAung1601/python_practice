import tkinter as tk

class KMITL_Phone:
    def __init__(self, root):
        self.root = root
        self.root.title("KMITL Phone")
        self.root.geometry("200x300")
        self.root.option_add("*Font", "Tahoma 12")

        # Create a Text widget for displaying the dialed number
        self.display = tk.Text(root, height=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="nsew")

        # Define the button labels
        self.button_labels = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#',
            'Talk', '<'
        ]

        # Global variable to track if "Talk" button was pressed
        self.talk_pressed = False

        # Create the buttons
        self.create_buttons()

        # Configure grid weights for resizing
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        row, col = 1, 0
        for label in self.button_labels:
            button = tk.Button(self.root, text=label, width=5, height=2)
            button.grid(row=row, column=col, padx=1, pady=1)
            button.bind("<Button-1>", self.button_click)  # Bind the click event to the function
            col += 1
            if col > 2:
                col = 0
                row += 1

    def button_click(self, event):
        if event.widget.cget("text") == "<":
            if self.talk_pressed:
                # Clear the display after "Talk" was pressed
                self.display.delete("1.0", tk.END)
                self.talk_pressed = False  # Reset the flag

            current_text = self.display.get("1.0", "end-2c")  # Remove the last character + \n
            self.display.delete("1.0", tk.END)
            self.display.insert("1.0", current_text)
        elif event.widget.cget("text") == "Talk":
            if not self.talk_pressed:
                to_display = self.display.get("1.0", "end-1c")  # Remove \n
                self.display.delete("1.0", tk.END)
                self.display.insert(tk.END, f"Dialing<<{to_display}>>")
                self.talk_pressed = True  # Set the flag to indicate "Talk" was pressed
        else:
            if self.talk_pressed:
                # Clear the display after "Talk" was pressed
                self.display.delete("1.0", tk.END)
                self.talk_pressed = False  # Reset the flag

            self.display.insert(tk.END, event.widget.cget("text"))

if __name__ == "__main__":
    root = tk.Tk()
    app = KMITL_Phone(root)
    root.mainloop()
