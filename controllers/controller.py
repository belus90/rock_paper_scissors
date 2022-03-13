from flask import render_template, request
from app import app
from models.game import*
from models.player import Player
import random

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play')
def play():
    return render_template('play.html', title ='Play')

@app.route('/play', methods = ['POST'])
def lets_play():
    name = request.form['name']
    choice = request.form['choice']
    player = Player(name = name, choice = choice)
    computer = Player(name = "computer", choice = random.choice(["rock", "paper", "scissors"]))
    winner =  Game.play_the_game(player,computer)
    if winner == None:
        return render_template('tie.html', title= 'tie')
    else:
        return render_template('result.html', title= 'result', player1 = player, player2 = computer,  winner = winner.name)
    
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
