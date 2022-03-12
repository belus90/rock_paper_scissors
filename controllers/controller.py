from flask import render_template
from app import app
from models.player_pick import players
from models.player import Player

@app.route('/players')
def index():
    return render_template('index.html', title='Home', players=players)