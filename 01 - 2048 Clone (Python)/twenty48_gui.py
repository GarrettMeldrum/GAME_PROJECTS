import tkinter as tk
from tkinter import font
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from twenty48_backend import twenty48

class twenty48_GUI:
    def __init__(self, game):
        self.game = game
        self.window = tk.Tk()
        self.window.title("2048")

        self.grid_frame = tk.Frame(self.window, bg="azure3")
        self.grid_frame.pack(padx=10, pady=10)

        self.cell_labels = [[None for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                label = tk.Label(self.grid_frame, text="", width=4, height=2, font=("Helvetica", 24, "bold"), bg="lightgrey", relief="solid")
                label.grid(row=i, column=j, padx=5, pady=5)
                self.cell_labels[i][j] = label

        self.window.bind("<Up>", self.move_up)
        self.window.bind("<Down>", self.move_down)
        self.window.bind("<Left>", self.move_left)
        self.window.bind("<Right>", self.move_right)

        self.update_grid()

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                value = self.game.grid[i][j]
                if value == 0:
                    self.cell_labels[i][j].config(text="", bg="lightgrey")
                else:
                    self.cell_labels[i][j].config(text=str(value), bg=self.get_color(value), font=self.get_font(value))

    def get_color(self, value):
        colors = {
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
            4096: "#3c3a32",
            8192: "#3c3a32",
        }
        return colors.get(value, "#cdc1b4")

    def get_font(self, value):
        if value < 100:
            return ("Helvetica", 24, "bold")
        elif value < 1000:
            return ("Helvetica", 20, "bold")
        else:
            return ("Helvetica", 16, "bold")

    def move_left(self, event):
        self.game.move_left()
        self.update_grid()
        if self.game.is_game_over():
            self.game_over()

    def move_right(self, event):
        self.game.move_right()
        self.update_grid()
        if self.game.is_game_over():
            self.game_over()

    def move_up(self, event):
        self.game.move_up()
        self.update_grid()
        if self.game.is_game_over():
            self.game_over()

    def move_down(self, event):
        self.game.move_down()
        self.update_grid()
        if self.game.is_game_over():
            self.game_over()

    def game_over(self):
        game_over_label = tk.Label(self.window, text="Game Over!", font=("Helvetica", 32, "bold"), bg="red", fg="white")
        game_over_label.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = twenty48()
    game_gui = twenty48_GUI(game)
    game_gui.run()
