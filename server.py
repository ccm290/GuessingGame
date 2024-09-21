import flask
import random as r
import copy

app = flask.Flask(__name__)

start_data = {
        'guesses_left': 10,
        'state': 0,
        # 0 - Game In Session
        # 1 - Game Over Win
        # 2 - Game Over Lose

        'hint_arrow': '---',
        'hint_text': '',
        'number': r.randint(1, 100) 
    }
data = copy.deepcopy(start_data)

up_arrow = '↑'
down_arrow = '↓'

@app.route("/")
def startup():
    if(data['state'] == 0):
        return flask.render_template("game_run.html", data=data)
    
    elif(data['state'] == 1):
        return flask.render_template("game_result.html", data=data)    
    

@app.route('/submit_guess', methods=["GET", "POST"])
def submit_guess():
    try:
        guess = flask.request.form.get('txtGuess')
        refresh_game(int(guess))
        return flask.redirect('/')
    except ValueError:
        data['hint_text'] = "Error: Not a valid number!"
        data['hint_arrow'] = '---'
        return flask.redirect('/')

 
@app.route('/new_game', methods=["GET", "POST"])
def reset_board():
    global data, start_data
    start_data['number'] = r.randint(1, 100)
    data = copy.deepcopy(start_data)

    return flask.render_template("game_run.html", data=data)


def refresh_game(guess):
    if(guess == data['number']):
        # win
        data['state'] = 1
        
    else:
        data['guesses_left'] -= 1

        if(data['guesses_left'] == 0):
            data['state'] = 2
        else:
            if(guess < data['number']):
                data['hint_text'] = "Guess again...Aim Higher"
                data['hint_arrow'] = up_arrow
            else:
                data['hint_text'] = "Guess again...Aim Lower"
                data['hint_arrow'] = down_arrow
            
            




'''
    if(data['state'] == 0):
        data['guesses_left'] -= 1
        
        if(data['guesses_left'] == 0):
            data['state'] = 2
            html = display_outcome()
        else:
            html = display_guesses('---', '', data['guesses_left'])
        
    return html

'''