import tkinter as tk;
from tkinter  import font;
from tkinter import messagebox 

class Board(tk.Tk):
    
    
    def __init__(self):
        super().__init__()
        self.title("Six-shipes")
        self._cells={}
        self._create_board_display()
        self._create_board_grid()
        self.first = False
        self.start_game()
        self.refresh_game()
        
    def start_game(self):
        for button in self._cells:
            button.config(text = "",background="gray")
        self.get_button(0,1).config(text = "^",background="blue")
        self.get_button(0,2).config(text = "^",background="blue")
        self.get_button(0,3).config(text = "^",background="blue")
        self.get_button(1,0).config(text = ">",background="green")
        self.get_button(2,0).config(text = ">",background="green")
        self.get_button(3,0).config(text = ">",background="green")
        
    def refresh_game(self):
        change =False
        for button in self._cells:
            if button.cget("text") == "":
                button.config(state ="disabled",background = "gray")
            else:
                button.config(state = "normal")               
            if self.first:
                if button.cget("text") == "^":
                    button.config(state = "normal")
                if button.cget("text") == ">":
                    button.config(state = "disabled")
            else:
                if button.cget("text") == ">":
                    button.config(state = "normal")
                if button.cget("text") == "^":
                    button.config(state = "disabled")
        self.get_button(4,1).config(state="disabled")
        self.get_button(4,2).config(state="disabled")
        self.get_button(4,3).config(state="disabled")
        self.get_button(1,4).config(state="disabled")
        self.get_button(2,4).config(state="disabled")
        self.get_button(3,4).config(state="disabled")
        finishG = 0
        finishB = 0
        isLockGreen = True
        for button in self._cells:
            if self._cells[button] == (1,4) and button.cget("text") != "":
                finishG += 1
            if self._cells[button] == (2,4) and button.cget("text") != "":
                finishG += 1
            if self._cells[button] == (3,4) and button.cget("text") != "":
                finishG += 1
            if self._cells[button] == (4,1) and button.cget("text") != "":
                finishB += 1
            if self._cells[button] == (4,2) and button.cget("text") != "":
                finishB += 1
            if self._cells[button] == (4,3) and button.cget("text") != "":
                finishB += 1
        if finishB >= 2 or finishG >= 2:
            for button in self._cells:
                if self._cells[button] != (1,4) and self._cells[button] != (2,4) and self._cells[button] != (3,4):
                    if button.cget("text") == ">":
                        row,col = self._cells[button]
                        if(self.get_button(row,col+1).cget("text") == "^"):
                            button2 = self.get_button(row,col+2)
                            if(button2 is not None):
                                if(button2.cget("text") == "^"):
                                  change = True
                                  isLockGreen = True
                if self._cells[button] != (4,1) and self._cells[button] != (4,2) and self._cells[button] != (4,3):
                    if button.cget("text") == "^":
                        row,col = self._cells[button]
                        if(self.get_button(row+1,col).cget("text") == ">"):
                            button2 = self.get_button(row+2,col)
                            if(button2 is not None):
                                if(button2.cget("text") == ">"):
                                  change = True 
                                  isLockGreen = False
        if change:
            if isLockGreen:
                self.first = True
            else:
                self.first = False
            for button in self._cells:
                if button.cget("text") == "":
                    button.config(state ="disabled",background = "gray")
                else:
                    button.config(state = "normal")               
                if self.first:
                    if button.cget("text") == "^":
                        button.config(state = "normal")
                    if button.cget("text") == ">":
                        button.config(state = "disabled")
                else:
                    if button.cget("text") == ">":
                        button.config(state = "normal")
                    if button.cget("text") == "^":
                        button.config(state = "disabled")
            self.get_button(4,1).config(state="disabled")
            self.get_button(4,2).config(state="disabled")
            self.get_button(4,3).config(state="disabled")
            self.get_button(1,4).config(state="disabled")
            self.get_button(2,4).config(state="disabled")
            self.get_button(3,4).config(state="disabled")
            
        if self.first ==False:
            self.display.config(text="Green",foreground="green")
        else:
            self.display.config(text="Blue",foreground="blue")
        if self.get_button(4,1).cget("text") == "^" and self.get_button(4,2).cget("text") == "^" and self.get_button(4,3).cget("text") == "^" :
            messagebox.showinfo("end game","blue win")
            self.first = False
            self.start_game()
            self.refresh_game()
        if self.get_button(1,4).cget("text") == ">" and self.get_button(2,4).cget("text") == ">" and self.get_button(3,4).cget("text") == ">" :
            messagebox.showinfo("end game","green win")
            self.first = False
            self.start_game()
            self.refresh_game()
        
    
    def jump(self,row,col,row2,col2,key):
        color = ""
        if key == ">":
            color = "green"
        else:
            color = "blue"
        self.get_button(row,col).config(text="")
        self.get_button(row2,col2).config(text=key,background = color)
        if self.first:
            self.first = False
        else:
            self.first = True
        self.refresh_game()  
    
    def onclick_button(self,row,col):
        button = self.get_button(row,col)
        if button.cget("text") == "^":
            button2 = self.get_button(row+1,col)
            if(button2 != None):
                if(button2.cget("text")==""):
                    self.jump(row,col,row+1,col,"^")
                else:
                    button3 = self.get_button(row+2,col)
                    if(button3.cget("text")==""):
                        self.jump(row,col,row+2,col,"^")
                    else:
                        self.refresh_game()
        else:
            button2 = self.get_button(row,col+1)
            if(button2 != None):
                if(button2.cget("text")==""):
                    self.jump(row,col,row,col+1,">")
                else:
                    button3 = self.get_button(row,col+2)
                    if(button3.cget("text")==""):
                        self.jump(row,col,row,col+2,">")
                    else:
                        self.refresh_game()
        
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(master=display_frame,
                                text = "Green",foreground="green",font=font.Font(size=24,weight="bold"))
        self.display.pack()
    
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self,)
        grid_frame.pack(fill=tk.BOTH)
        for row in range(5):
            self.rowconfigure(row,weight=5,minsize=50)
            self.columnconfigure(row,weight=5,minsize=150,)
            for col in range(5):
                if col in range(4) and row in range(0,4):
                    if(col == 0 and row == 0):
                        button = tk.Button(
                           master=grid_frame,
                        text="",
                        width=3,height=2,
                        highlightbackground="lightblue",state="disabled",command= lambda row = row,col=col:self.onclick_button(row,col)
                    )
                    else:
                        button = tk.Button(
                            master=grid_frame,
                            text="",
                            width=3,height=2,
                            highlightbackground="lightblue",command= lambda row = row,col=col:self.onclick_button(row,col)
                        )
                else:
                    button = tk.Button(
                           master=grid_frame,
                        text="",
                        width=3,height=2,
                        highlightbackground="lightblue",state="disabled",command= lambda row = row,col=col:self.onclick_button(row,col)
                    )
                self._cells[button] = (row,col)
                button.grid(
                    row=row,
                    column=col,
                    padx=0.5,pady=0.5,sticky="nsew"
                )

        
    def get_button(self, row, col):
        for button, (button_row, button_col) in self._cells.items():
            if button_row == row and button_col == col:
                return button
        return None
                        
def main():
    board = Board()
    board.mainloop()
    
if __name__ == "__main__":
    main()