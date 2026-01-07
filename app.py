import flask
app = flask.Flask("strem-mdeck")

Colmns = 12
Rows = 5 
TotalSlots = Colmns * Rows

buttons = [
    {
        "pos":(0,0),
        "id":"Mute",
        "label":"Mute Discord",
        "img":"https://images-eds-ssl.xboxlive.com/image?url=4rt9.lXDC4H_93laV1_eHHFT949fUipzkiFOBH3fAiZZUCdYojwUyX2aTonS1aIwMrx6NUIsHfUHSLzjGJFxxsG72wAo9EWJR4yQWyJJaDaK1XdUso6cUMpI9hAdPUU_FNs11cY1X284vsHrnWtRw7oqRpN1m9YAg21d_aNKnIo-&format=source"
    },
    {
        "pos": (2, 5),
        "id": "Play",
        "label": "Müzik",
        "img": "https://cdn-icons-png.flaticon.com/512/27/27223.png"
    }
]
def generate_grid():
    grid = [[{"id":None,"label":"","img":""} for _ in range(Colmns)] for _ in range(Rows)]
    for btn in buttons:
        r,c = btn["pos"]
        if 0 <= r < Rows and 0 <= c < Colmns:
            grid[r][c] = btn
    flat_list = []
    for row in grid:
        for item in row:
            flat_list.append(item)
    return flat_list
        
@app.route('/')
def index():
    btns = generate_grid()
    return flask.render_template("index.html",buttons=btns)
@app.route('/action/<action_id>')
def trigger(action_id):
    print(f'Tetiklenen {action_id}')
    return "OK" ,200



app.run('0.0.0.0',33333)