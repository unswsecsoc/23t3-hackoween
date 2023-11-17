# Car Shop

## Authors

- Daniel Cooper

## Category

- web

## Description

I wonder if my car's "engine" is secure... Why don't you find out? Good luck - you'll need it.

[https://carshop.ctf.secso.cc/](https://carshop.ctf.secso.cc/)

NOTE: this challenge comes with reset functionality in case it gets borked. To reset the challenge, run the following command:
`nc pwn.ctf.secso.cc 1337`

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

This was a difficult one! The app has an LFI which can be used to read the source and find the templating engine used. Then, by polluting the nginx logs, RCE can be achieved.

### Walkthrough

1. The url parameter allows for LFI. Accessing invalid paths leaks the app as /app/app.js, and we can access this to read the source. We see that the app uses handlbars as a templating engine.
2. RCE can be done through handlebars using techniques found here:
   [https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#handlebars-nodejs](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#handlebars-nodejs)
   More information can be seen in the [solve script](./solve.py)
3. We can pollute /var/log/nginx/access.log using our user agent. Then we can load this using the LFI and execute our RCE payload.

### Flag

`SPOOKTF{i_sur3_hOpe_you_d1dnt_guess_th3_NAME_of_th15_fil3!}`

</details>
