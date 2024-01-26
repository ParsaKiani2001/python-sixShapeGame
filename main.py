import tkinter as tk;
from tkinter  import font;

class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Six-shipes")
        self._cells={}
        self._create_board_display()
        self._create_board_grid()
        
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(master=display_frame,
                                text = "Ready?",font=font.Font(size=24,weight="bold"))
        self.display.pack()
    
    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self,)
        grid_frame.pack(fill=tk.BOTH)
        for row in range(5):
            self.rowconfigure(row,weight=5,minsize=50)
            self.columnconfigure(row,weight=5,minsize=150,)
            for col in range(5):
                if col in range(4) and row in range(1,4):
                    button = tk.Button(
                        master=grid_frame,
                        text="",
                        width=3,height=2,
                        highlightbackground="lightblue"
                    )
                else:
                    button = tk.Button(
                           master=grid_frame,
                        text="",
                        width=3,height=2,
                        highlightbackground="lightblue",state="disabled"
                    )
                self._cells[button] = (row,col)
                button.grid(
                    row=row,
                    column=col,
                    padx=0.5,pady=0.5,sticky="nsew"
                )
                
def main():
    board = Board()
    board.mainloop()
    
if __name__ == "__main__":
    main()