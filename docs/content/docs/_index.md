---
title: "fast-flights"
---

A fast, robust Google Flights scraper (API) for Python. (Probably)

`fast-flights` uses Base64-encoded [Protobuf](https://developers.google.com/protocol-buffers) strings to generate the **`tfs` query parameter**, which stores all the information for a lookup request. We then parse the HTML content and extract the info we need using `selectolax`.

Everything is typed and documented (mostly, unless things are self-explanatory).

```sh
pip install fast-flights
```

## Getting started
It's pretty simple and beginner-friendly.

```python
from fast_flights import FlightQuery, Passengers, ResultList, create_query, get_flights

result: ResultList = create_query(
    flights=[
        FlightQuery(date="2025-01-01", from_airport="TPE", to_airport="MYJ")  # (1)
    ],
    trip="one-way",  # (2)
    seat="economy",  # (3)
    passengers=Passengers(adults=2, children=1, infants_in_seat=0, infants_on_lap=0),  # (4)
)

print(result)
```

1. 🛂 This specifies the (desired) date of departure for the outbound flight. Make sure to change the date!
2. 🧳 This specifies the trip type (`round-trip` or `one-way`). Note that `multi-city` is **not yet** supported. Note that if you're having a `round-trip`, you need to add more than one item of flight data (in other words, 2+).
3. 💺 Money-spending time! This specifies the seat type, which is `economy`, `premium-economy`, `business`, or `first`.
4. 👯 Nice interface, eh? This specifies the number of a specific passenger type.

## How it's made
Curious? Check it out [here](https://github.com/AWeirdDev/flights#how-its-made).

## Contributing

Feel free to contribute! Though I won't be online that often, I'll try my best to answer all the whats, hows & WTFs.

❤ Acknowledgements:

- @d2x made their first contribution in #7
- @PTruscott made their first contribution in #19
- @artiom-matvei made their first contribution in #20
- @esalonico fixed v2.0 currency issues in #25
- @NickJLange helped add a LICENSE file in #38
- @Lim0H (#39) and @andreaiorio (#41) fixed `primp` client issues.
- @kiinami (#43) added local Playwright support

...and more people!

I really have to apologize to the community. I don't really like reading pull requests and cherry-picking. Most of the time I *remember* there's a pull request and then 3 minutes I later I completely forget about it. Not in an *intentional* way, it's just somehow my brain really hates doing these tasks...

If you'd like to help me make this community better, [here](https://github.com/AWeirdDev/flights/issues/92).
