# tic_tac_toe.py
import random
import tkinter as tk
import tkinter.messagebox

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tic Tac Toe')
        self.geometry('500x400')

        self.char_x = tk.PhotoImage(file='./char_x.png')
        self.char_o = tk.PhotoImage(file='./char_o.png')
        self.empty = tk.PhotoImage()

        self.active = 'GAME ACTIVE'
        self.total_cells = 9
        self.line_size = 3
        self.computer = {'value': 1, 'bg': 'orange',
                         'win': 'COMPUTER WINS', 'image': self.char_x}
        self.user = {'value': self.line_size+1, 'bg': 'grey',
                     'win': 'USER WINS', 'image': self.char_o}
        self.board_bg = 'white'
        self.all_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6))

        self.create_radio_frame()
        self.create_control_frame()

    def create_radio_frame(self):
        self.radio_frame = tk.Frame()
        self.radio_frame.pack(side=tk.TOP, pady=5)

        tk.Label(self.radio_frame, text='First Move').pack(side=tk.LEFT)
        self.radio_choice = tk.IntVar()
        self.radio_choice.set(self.user['value'])
        tk.Radiobutton(self.radio_frame, text='Computer',
                       variable=self.radio_choice, value=self.computer['value']
                      ).pack(side=tk.LEFT)
        tk.Radiobutton(self.radio_frame, text='User',
                       variable=self.radio_choice, value=self.user['value']
                      ).pack(side=tk.RIGHT)

    def create_control_frame(self):
        self.control_frame = tk.Frame()
        self.control_frame.pack(side=tk.TOP, pady=5)

        self.b_quit = tk.Button(self.control_frame, text='Quit',
                                command=self.quit)
        self.b_quit.pack(side=tk.LEFT)

        self.b_play = tk.Button(self.control_frame, text='Play',
                                command=self.play)
        self.b_play.pack(side=tk.RIGHT)

    def create_status_frame(self):
        self.status_frame = tk.Frame()
        self.status_frame.pack(expand=True)

        tk.Label(self.status_frame, text='Status: ').pack(side=tk.LEFT)
        self.l_status = tk.Label(self.status_frame)
        self.l_status.pack(side=tk.RIGHT)

    def create_board_frame(self):
        self.board_frame = tk.Frame()
        self.board_frame.pack(expand=True)

        self.cell = [None] * self.total_cells
        self.board = [0] * self.total_cells
        self.remaining_moves = list(range(self.total_cells))
        for i in range(self.total_cells):
            self.cell[i] = tk.Label(self.board_frame, highlightthickness=1,
                                    width=75, height=75, bg=self.board_bg,
                                    image=self.empty)
            self.cell[i].bind('<Button-1>',
                              lambda e, move=i: self.user_click(e, move))
            r, c = divmod(i, self.line_size)
            self.cell[i].grid(row=r, column=c)

    def play(self):
        self.b_play['state'] = 'disabled'
        if self.b_play['text'] == 'Play':
            self.create_status_frame()
            self.b_play['text'] = 'Play Again'
        else:
            self.board_frame.destroy()
        self.l_status['text'] = self.active
        self.state = self.active
        self.last_click = 0
        self.create_board_frame()
        if self.radio_choice.get() == self.computer['value']:
            self.computer_click()

    def quit(self):
        self.destroy()

    def user_click(self, e, user_move):
        if self.board[user_move] != 0 or self.state != self.active:
            # Check if the cell is already marked or the game is not active
            tk.messagebox.showwarning('Warning', 'Already been chosen!')
            return
        self.update_board(self.user, user_move)
        if self.state == self.active:
            self.computer_click()

    # def computer_click(self):
    #     computer_move = random.choice(self.remaining_moves)
    #     self.update_board(self.computer, computer_move)

    def computer_click(self):
        if self.radio_choice.get() == self.computer['value']:
            # Computer's turn (Minimax logic)
            move = self.minimax_move()
            self.update_board(self.computer, move)

    def minimax_move(self):
        best_score = -float('inf')
        best_move = None

        for move in self.remaining_moves:
            if self.board[move] == 0:
                self.board[move] = self.computer['value']
                score = self.minimax(self.board, 0, False)
                self.board[move] = 0
                if score > best_score:
                    best_score = score
                    best_move = move
        return best_move

    def minimax(self, board, depth, is_maximizing):
        scores = {
            'COMPUTER WINS': 1,
            'USER WINS': -1,
            'TIE': 0,
            'GAME ACTIVE': 0
        }
        result = self.check_game_state(board)
        if result in scores:
            return scores[result]

        if is_maximizing:
            best_score = -float('inf')
            for move in range(self.total_cells):
                if board[move] == 0:
                    board[move] = self.computer['value']
                    score = self.minimax(board, depth + 1, False)
                    board[move] = 0
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in range(self.total_cells):
                if board[move] == 0:
                    board[move] = self.user['value']
                    score = self.minimax(board, depth + 1, True)
                    board[move] = 0
                    best_score = min(score, best_score)
            return best_score

    def check_game_state(self, board):
        for line in self.all_lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != 0:
                return self.computer['win'] if board[line[0]] == self.computer['value'] else self.user['win']
        return 'TIE' if 0 not in board else 'GAME ACTIVE'

    def update_board(self, player, move):
        self.board[move] = player['value']
        self.remaining_moves.remove(move)
        self.cell[self.last_click]['bg'] = self.board_bg
        self.last_click = move
        self.cell[move]['image'] = player['image']
        self.cell[move]['bg'] = player['bg']
        self.update_status(player)
        self.l_status['text'] = self.state
        if self.state != self.active:
            self.b_play['state'] = 'normal'

    def update_status(self, player):
        winner_sum = self.line_size * player['value']
        for line in self.all_lines:
            if sum(self.board[i] for i in line) == winner_sum:
                self.state = player['win']
                self.highlight_winning_line(player, line)
        if self.state == self.active and not self.remaining_moves:
            self.state = 'TIE'

    def highlight_winning_line(self, player, line):
        for i in line:
            self.cell[i]['bg'] = player['bg']

if __name__ == '__main__':
    root = Root()
    root.mainloop()
