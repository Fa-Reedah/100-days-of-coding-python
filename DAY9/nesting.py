"""NESTING

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting list in dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12, "days_spent_per_visit": 3}
}

# Nesting dictionary in list
travel_log = [
    {"Country": "France", "cities_visited": ["Paris", "Lillie", "Dijon"]},
    {"Country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12, "days_spent_per_visit": 3}
]
"""

# Exercise

travel_log = [
    {
        "Country": "France",
        "visits": 12,
        "cities_visited": ["Paris", "Lillie", "Dijon"]
    },

    {
        "Country": "Germany",
        "total_visits": 12,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    }
]


def add_new_country(country, times_travelled, place_visited):
    travel_log.append(
        {
            "Country": str(country),
            "Visits": int(times_travelled),
            "cities_visited": place_visited
        }
    )


add_new_country("Russia", 2, ["Moscow", "Saint Pettersburg"])
print(travel_log)
