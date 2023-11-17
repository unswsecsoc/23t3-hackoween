from flask import Flask, request, make_response, redirect
import json
from Crypto.Cipher import AES

KEY = b"rvlibuy4hgkasfyb"

app = Flask(__name__)


def encrypt(data):
    while len(data) % 16 != 0:
        data += b"\x00"

    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(data).hex()


def decrypt(data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.decrypt(bytes.fromhex(data)).rstrip(b"\x00")


@app.route("/", methods=["GET"])
def index():
    if request.cookies.get("session"):
        sess = decrypt(request.cookies.get("session")).decode()
        sess = json.loads(sess)

        return f"""
Hello {sess["name"]}! Welcome!
<a href="/logout">Logout</a>
"""
    else:
        return """
    <p>Login</p>
    <form action="/" method="POST">
        <input name="uname">
        <input type="submit">
    </form>
    """


@app.route("/", methods=["POST"])
def login():
    uname = request.form.get("uname")

    cook = {"name": uname, "flag": "SPOOKTF{th15_on3_15_reALLY_an_orAcl3}"}

    cook = json.dumps(cook)
    cook = encrypt(cook.encode())

    resp = make_response(redirect("/"))

    resp.set_cookie("session", cook)

    return resp


@app.route("/logout", methods=["GET"])
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie("session", "")

    return resp
