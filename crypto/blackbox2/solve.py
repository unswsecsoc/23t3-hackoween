#!/usr/bin/python3

from requests import Session

s = Session()

TARGET = "https://blackbox2.ctf.secso.cc/"


def encrypt(uname):
    if '"' in uname or "\\" in uname:
        raise RuntimeError("Bad char")
    s.cookies.clear()
    s.post(TARGET, data={"uname": uname})
    return bytes.fromhex(s.cookies.get("session"))


def get(cookie):
    s.cookies.set("session", cookie.hex())
    return s.get(TARGET).text


def encrypt_single_block(block_data):
    assert len(block_data) == 16

    return encrypt("A" * 6 + block_data)


{"name": "AAAAAA", "flag": "The flag is SPOOKTF{th15_on3_15_reALLY_an_orAcl3}"}

cook = encrypt("A" * 6)
cook = cook[:16] + cook[32:]

print(get(cook))
