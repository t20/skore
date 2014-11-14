import os
import json

from flask import Flask, render_template, request, redirect, url_for, \
flash, jsonify

from models import Board, Item
from models import get_boards, get_board, get_items


app = Flask(__name__)
app.config.from_object('settings.Config')
app.secret_key = app.config['APP_SECRET_KEY']


@app.route('/')
def index():
    boards = get_boards()
    return render_template('index.html', boards=boards)


@app.route('/board/new', methods=['GET', 'POST'])
def new_board():
    if request.method == 'GET':
        return render_template('board_form.html')
    # else POST
    name = request.form.get('name')
    desc = request.form.get('desc', '')
    items = request.form.getlist('item')

    b = Board(name=name, desc=desc)
    saved = b.save()
    
    board_id = int(b.id)
    for item in items:
        if not item:
            continue
        i = Item(name=item, board_id=board_id)
        saved = i.save()
        # print 'saved?', saved
        # print 'Item: {} - saved? {}'.format(item, saved)

    flash('New board created.')
    return redirect(url_for('board', board_id=int(b.id)))


@app.route('/board/<board_id>')
def board(board_id):
    board = get_board(board_id)
    items = get_items(board_id)
    return render_template('board.html', board=board, items=items)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 0))
    if port:
        app.debug = False
        app.run(host='0.0.0.0', port=port)
    else:
        app.debug = True
        app.run()

