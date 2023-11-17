# XSS 4

## Authors

- Daniel Cooper

## Category

- web

## Description

My final attempt - this time I've used DOMPurify!

[https://xss4.ctf.secso.cc/](https://xss4.ctf.secso.cc/)

Author: @ssparrow

## Difficulty

- Easy
- Medium
- Hard

## Points

50

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Use DOM clobbering to achieve XSS.

### Walkthrough

1. This time we have two injection points. Name has XSS, but description is sanitized.
2. Although description is santized, we can still use [dom clobbering](https://portswigger.net/web-security/dom-based/dom-clobbering) to help with the xss.
3. This can be done by doing a description such as

```
<a href="tel:alert(1)" id="z">
```

and a name such as

```
<svg onload=eval(``+z)>
```

4. The way this works is the `<a id="z"` tag means that if the variable `z` is used, it will return the `a` tag. Adding an empty string to it causes it to be converted to a string, which returns the href (`tel:alert(1)`). Evaling this href calls alert(1). We can then replace alert(1) with our XSS payload, as the description does not have a character limit.

### Flag

`SPOOKTF{alr1ght_1_g1v3_up_now..}`

</details>
