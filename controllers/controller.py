from flask import render_template
from app import app
from models.game import*
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/rock/scissors')
def player1_wins_by_rock():
    return render_template('player1_wins.html', title= 'player1 wins', choice="rock")

@app.route('/scissors/paper')
def player1_wins_by_scissor():
    return render_template('player1_wins.html', title= 'player1 wins', choice="scissors")

@app.route('/paper/rock')
def player1_wins_by_paper():
    return render_template('player1_wins.html', title= 'player1 wins', choice="paper")

@app.route('/rock/paper')
def player1_loses_by_rock():
    return render_template('player1_loses.html', title= 'player1 loses', choice="rock")

@app.route('/scissors/rock')
def player1_loses_by_scissor():
    return render_template('player1_loses.html', title= 'player1 loses', choice="scissors")

@app.route('/paper/scissors')
def player1_loses_by_paper():
    return render_template('player1_loses.html', title= 'player1 loses', choice="paper")

@app.route('/paper/paper')
@app.route('/rock/rock')
@app.route('/scissors/scissors')
def tie():
    return render_template('tie.html', title= 'tie')
