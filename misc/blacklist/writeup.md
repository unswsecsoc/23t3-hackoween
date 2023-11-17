# Blacklist

## Authors

- Daniel Cooper

## Category

- misc

## Description

I have thought about security, trust me! I've written a great blacklist! It's not possible to bypass it...

`nc pwn.ctf.secso.cc 6001`

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Bypass a python blacklist.

### Walkthrough

`["import", "open", "system", "eval", "exec"]` are the banned keywords here.
The trick is that we can use python's `__builtins__` variable to access built in variables using a string rather than typing it out. Once we can access using a string we can use string concatanation to bypass the blasklist.

For example:

```
__builtins__.__dict__["__impo" + "rt__"]("subprocess").call("/bin/sh")
```

### Flag

`SPOOKTF{pyth0n_succ3ssfully_3xpLOit3d!}`

</details>
