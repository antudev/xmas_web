from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://christmascountdown.live/api/timeleft"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        countdown = {
            "days": int(data.get("days", 0)),
            "hours": int(data.get("hours", 0)),
            "minutes": int(data.get("minutes", 0)),
            "seconds": int(data.get("seconds", 0)),
        }

    except:
        countdown = {
            "days": 0,
            "hours": 0,
            "minutes": 0,
            "seconds": 0,
        }

    return render_template("index.html", countdown=countdown)

if __name__ == "__main__":
    app.run(debug=True)
