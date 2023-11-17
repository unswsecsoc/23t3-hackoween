import asyncio
import quart
import sys

app = quart.Quart("/funni/directory/that/you/will/never/find/flag.txt")

@app.route("/")
async def present():
    return await quart.send_file("index.html")

@app.route("/compile", methods=["POST"])
async def compile():
    code = await quart.request.get_data(cache=False, as_text=False, parse_form_data=False)

    mktemp = await asyncio.create_subprocess_exec("mktemp", stdout=asyncio.subprocess.PIPE)
    file, _ = await mktemp.communicate()
    file = file.strip()

    if mktemp.returncode != 0:
        return quart.Response(
            "`mktemp` returned with a non-zero return code - "
            "this should not happen, please contact the challenge author.",
            status=500
        )

    compiler = await asyncio.create_subprocess_exec(
        "gcc", "-O3", "-x", "c", "-o", file, "-",
        stdin=asyncio.subprocess.PIPE
    )

    await compiler.communicate(code)

    disassembler = await asyncio.create_subprocess_exec(
        "objdump", "--disassemble", "--section=.text", "--disassembler-options=intel", file,
        stdout=asyncio.subprocess.PIPE
    )

    instructions, _ = await disassembler.communicate()

    if compiler.returncode != 0 or disassembler.returncode != 0:
        return quart.Response(
            "An error occurred during compilation and/or disassembly - "
            "the message has been omitted for security reasons.",
            status=400
        )

    return quart.Response(instructions.decode(), status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(sys.argv[1]))
