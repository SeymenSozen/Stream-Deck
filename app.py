import flask
app = flask.Flask("strem-mdeck")

Colmns = 12
Rows = 5 
TotalSlots = Colmns * Rows

buttons = [
    {
        "pos":(0,0),
        "type":"switch",
        "value":1,
        "id":"Mic",
        "label":"Mikrofon",
        "active_image":"https://media.istockphoto.com/id/1298266863/vector/retro-microphone-vector-sign.jpg?s=612x612&w=0&k=20&c=gWqaiRyIC7csOCQ7SF-dO8-dtgUYdCUSBXBwmA2OUNA=",
        "passive_image":'https://c8.alamy.com/comp/2PTX4A8/microphone-mic-mute-color-vector-grayscale-icon-music-sign-graph-symbol-for-music-and-sound-web-site-and-apps-design-logo-app-ui-2PTX4A8.jpg'
    },
        {
        "pos":(0,1),
        "type":"switch",
        "value":1,
        "id":"Mic",
        "label":"Discord Mikrofon",
        "active_image":"https://images.ctfassets.net/h50kqpe25yx1/7EZbsGciGNJpOd6nxEwdfA/3da50880bb5b9e364d8b275c99d4b132/elgato-x-discord-grid-card-2.jpg",
        "passive_image":'https://cdn.discordapp.com/attachments/1088850571492445481/1126034867081864060/discord-mic-off-icon-10.jpg'
    },

    {
        "pos":(0,2),
        "type":"action",
        "id":"Scane1",
        "label":"Sahne 1",
        "img":"data:image/jpeg;base64,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"
    }   
]
def generate_grid():
    grid = [[{"id":None,"label":"","img":""} for _ in range(Colmns)] for _ in range(Rows)]
    for btn in buttons:
        if btn["type"] == "switch":
            if btn["value"] == 1:
                btn["img"] = btn["active_image"]
            else:
                btn["img"] = btn["passive_image"]
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