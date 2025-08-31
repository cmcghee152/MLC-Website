from flask import Flask, render_template


# Configure application
app = Flask(__name__)
app.secret_key = 'test'



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template('index.html', current_page="index")

@app.route("/join", methods=["GET", "POST"])
def join():
    return render_template('join.html', current_page="join")

@app.route("/officers", methods=["GET", "POST"])
def officers():
    return render_template('officers.html', current_page="officers")

@app.route("/playlists", methods=["GET", "POST"])
def playlists():
    return render_template('playlists.html', current_page="playlists")

@app.route("/playlists-2024", methods=["GET", "POST"])
def playlists_2024():
    return render_template('playlists-2024.html', current_page="playlists")

if __name__ == '__main__':
    app.run(debug=True)