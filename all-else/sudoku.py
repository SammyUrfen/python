import tkinter as tk
from tkinter import messagebox
import copy

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = {}  # Dictionary to store entry widgets
        self.create_gui()

    def create_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(padx=10, pady=10)

        # Create the grid
        for i in range(9):
            for j in range(9):
                cell_frame = tk.Frame(
                    main_frame,
                    borderwidth=1,
                    relief="solid",
                    width=50,
                    height=50
                )
                cell_frame.grid_propagate(False)
                cell_frame.grid(row=i, column=j, padx=1, pady=1)
                
                # Add thick borders for 3x3 boxes
                if i % 3 == 0 and i != 0:
                    cell_frame.grid(pady=(3, 1))
                if j % 3 == 0 and j != 0:
                    cell_frame.grid(padx=(3, 1))
                
                # Create entry widget
                cell = tk.Entry(
                    cell_frame,
                    justify='center',
                    font=('Arial', 18)
                )
                cell.place(relx=0.5, rely=0.5, anchor='center')
                
                # Configure validation
                vcmd = (self.root.register(self.validate_input), '%P', '%S')
                cell.configure(validate='key', validatecommand=vcmd)
                
                self.cells[(i, j)] = cell

        # Buttons frame
        button_frame = tk.Frame(self.root, bg='white')
        button_frame.pack(pady=10)

        # Solve button
        solve_button = tk.Button(
            button_frame,
            text="Solve",
            command=self.solve_button_clicked,
            font=('Arial', 12),
            bg='#4285f4',
            fg='white',
            padx=20,
            pady=5
        )
        solve_button.pack(side=tk.LEFT, padx=5)

        # Clear button
        clear_button = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_board,
            font=('Arial', 12),
            bg='#db4437',
            fg='white',
            padx=20,
            pady=5
        )
        clear_button.pack(side=tk.LEFT, padx=5)

    def validate_input(self, P, S):
        if P == "":  # Allow deletion
            return True
        if not S.isdigit():  # Only allow digits
            return False
        if not (1 <= int(S) <= 9):  # Only allow 1-9
            return False
        if len(P) > 1:  # Only allow single digits
            return False
        return True

    def get_board(self):
        board = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.cells[(i, j)].get()
                board[i][j] = int(value) if value else 0
        return board

    def set_board(self, board):
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                self.cells[(i, j)].delete(0, tk.END)
                if value != 0:
                    self.cells[(i, j)].insert(0, str(value))

    def clear_board(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)

    def check_conflicts(self, board, i, j):
        conflicts = [False] * 9
        # Check row
        for k in range(9):
            if board[i][k] != 0:
                conflicts[board[i][k]-1] = True
        # Check column
        for k in range(9):
            if board[k][j] != 0:
                conflicts[board[k][j]-1] = True
        # Check 3x3 box
        box_i, box_j = 3 * (i // 3), 3 * (j // 3)
        for k in range(3):
            for l in range(3):
                if board[box_i+k][box_j+l] != 0:
                    conflicts[board[box_i+k][box_j+l]-1] = True
        return conflicts

    def solve_sudoku(self, board, i, j):
        if i == 9:
            return True
        
        conflicts = self.check_conflicts(board, i, j)
        candidate = 0
        next_i = i + 1 if j == 8 else i
        next_j = 0 if j == 8 else j + 1
        
        if board[i][j] != 0:
            return self.solve_sudoku(board, next_i, next_j)
        
        while candidate < 9:
            if conflicts[candidate]:
                candidate += 1
                continue
            board[i][j] = candidate + 1
            if self.solve_sudoku(board, next_i, next_j):
                return True
            candidate += 1
        
        board[i][j] = 0
        return False

    def solve_button_clicked(self):
        board = self.get_board()
        # Make a copy to solve
        board_copy = copy.deepcopy(board)
        
        if self.solve_sudoku(board_copy, 0, 0):
            self.set_board(board_copy)
        else:
            messagebox.showerror("Error", "No solution exists!")

def main():
    root = tk.Tk()
    root.configure(bg='white')
    app = SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()