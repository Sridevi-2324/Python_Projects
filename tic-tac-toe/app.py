from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Game state
board = ['', '', '', '', '', '', '', '', '']
current_player = 'X'
game_active = True

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player)

@app.route('/move/<int:index>')
def move(index):
    global current_player, game_active
    if board[index] == '' and game_active:
        board[index] = current_player
        if check_win():
            game_active = False
            return f'{current_player} wins!'
        current_player = 'O' if current_player == 'X' else 'X'
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global board, current_player, game_active
    board = ['', '', '', '', '', '', '', '', '']
    current_player = 'X'
    game_active = True
    return redirect(url_for('index'))

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] and board[a] == board[b] == board[c]:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
