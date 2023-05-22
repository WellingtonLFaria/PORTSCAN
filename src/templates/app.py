from flask import Flask, render_template, request, redirect, jsonify
from waitress import serve
import json

app = Flask(__name__)

from portscan import portscan

@app.route("/")
def index():
    return redirect("/portscan")

@app.route("/portscan", methods=["GET", "POST"])
def portscanroute():
	if request.method == "POST":
		ip = request.form["ip"]
		portasabertas = portscan(ip)
		return jsonify(portasabertas)
	else:
		return render_template("portscan.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
