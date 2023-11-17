# Blackbox

## Authors

- Daniel Cooper

## Category

- crypto

## Description

My friend made a crypto application, but he knows nothing about crypto so it's probably vulnerable to something. The issue is, he won't let me read the source
cause he says "real attackers won't be able to see the source"

Can you exploit it without seeing the source code?

[https://blackbox.ctf.secso.cc/](https://blackbox.ctf.secso.cc/)

Author: @ssparrow

## Hints

## Files

## Solution

<details>
<summary>Spoiler</summary>

### Idea

Discover that the cipher is a [stream cipher](https://en.wikipedia.org/wiki/Stream_cipher) and use this fact to decrypt the rest of the flag.

### Walkthrough

1. There are many ways to discover that the cipher is a stream cipher. Firstly, each byte encrypted is not dependent on any of the others, only on it's position. This means that if we enter AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA as input we get this:

```
6e6811d5847b71b29dd0661dd087ba7124db8e45782fe2994c0336eda0570ac1f4ab5e15c8ffb2691cd386bd7027da91447b2e86f52e611ec183706ebb96c97305c5f0bf7d18e8aecc5c03f5bf616411cb85403618edaf5d12f586984966feb4aa5e37a7968d5c1dcfb134030c84a6
```

and if we enter BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB we get this:

```
6e6811d5847b71b29dd0651ed384b97227d88d467b2ce19a4f0035eea35409c2f7a85d16cbfcb16a1fd085be7324d99247782d86f52e611ec183706ebb96c97305c5f0bf7d18e8aecc5c03f5bf616411cb85403618edaf5d12f586984966feb4aa5e37a7968d5c1dcfb134030c84a6
```

2. As the inputs differ at byte 10, this is where our payload is being injected. If we send it a lot of A's, we can XOR with A to retrieve the key.
   For example, submitting:

```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

yields

```
6e6811d5847b71b29dd0661dd087ba7124db8e45782fe2994c0336eda0570ac1f4ab5e15c8ffb2691cd386bd7027da91447b2ee5984f0239eca3560dc0f7aa6114cbfeb5681fd289bc7326dd90477a31e49b4e0538efa2590cc3f6ad6017ca81b46b1ed588bf7229dc93467d30e79a51043beea5580fc2f9ac6316cd80b76a21d48bbe7528df92497c33e69d50073af1a45b0ec59bc2037aebae964b43aceb22663ad09b426a35d3bb232918d8887c0fe4d4b06b2bef80b4683de0fd755e5bd5a1554b1c9a81602708e0842f6efb998d
```

We can XOR this with the A to retrieve the key stream:

```
2f295094c53a30f3dc91275c91c6fb30659acf04396ea3d80d4277ace1164b80b5ea1f5489bef3285d92c7fc31669bd0053a6fa4d90e4378ade2174c81b6eb20558abff4295e93c8fd32679cd1063b70a5da0f4479aee3184d82b7ec21568bc0f52a5f94c9fe33689dd2073c71a6db10457aafe4194e83b8ed22578cc1f62b6095caff34699ed3083d72a7dc11467bb0e51a4f84da83423baaefd70a02edaa63277b91da032b7492fa62685999c93d4ea595f12a6aaec1f5297ca1bc341f1a94e0140a5ddbc0216649a1c56e2fbad8cc
```

Now we can XOR the key stream with a shorter encrypted payload to retrieve the following data:

```
AAAAAAAAAAa", "flag": "SPOOKTF{f1nding_an_OraCLE_w1th0ut_th3_souRc3?}"}
```

### Flag

`SPOOKTF{f1nding_an_OraCLE_w1th0ut_th3_souRc3?}`

</details>
