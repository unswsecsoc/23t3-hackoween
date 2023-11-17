from flask import Flask, request, make_response, redirect
import json

app = Flask(__name__)


def encrypt(data):
    x = 21
    res = b""
    for b in data:
        res += bytes([b ^ x])
        x = (x + 53) % 256
    return res.hex()


def decrypt(data):
    return bytes.fromhex(encrypt(bytes.fromhex(data)))


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

    cook = {"name": uname, "flag": "SPOOKTF{f1nding_an_OraCLE_w1th0ut_th3_souRc3?}"}

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
