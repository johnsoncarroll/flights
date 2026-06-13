"""SearchApi integration test."""

from pprint import pprint

from fast_flights import FlightQuery, Passengers, create_query, get_flights
from fast_flights.integrations import SearchApi

query = create_query(
    flights=[
        FlightQuery(
            date="2026-07-01",
            from_airport="MYJ",
            to_airport="TPE",
        ),
    ],
    seat="economy",
    trip="one-way",
    passengers=Passengers(adults=1),
    language="zh-TW",
    currency="TWD",
)
res = get_flights(query, integration=SearchApi())
pprint(res)
