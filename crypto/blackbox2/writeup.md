# Blackbox 2

## Authors

- Daniel Cooper

## Category

- crypto

## Description

This time my friend has upped his game.

Can you exploit it AGAIN without seeing the source code?

[https://blackbox2.ctf.secso.cc/](https://blackbox2.ctf.secso.cc/)

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Discover the cipher is an ECB block cipher, and use this fact to extract the flag.

### Walkthrough

1. We can notice that the length is a multiple of a fixed number to determine it is a block cipher.
2. Encrypting AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA... tells us that it is an ECB cipher, as we can see repeating blocks in the output.
3. We can now encrypt some data so that the `", "` is in a known block, and then remove this block. When the application decrypts it, it will read the flag as part of the username. Refer to [solve.py](./solve.py) for more info.

### Flag

`SPOOKTF{th15_on3_15_reALLY_an_orAcl3}`

</details>
