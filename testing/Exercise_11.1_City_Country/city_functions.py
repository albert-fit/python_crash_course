def format_city_country(city, country, population=''):
    """A function that formats the city and country into a string"""
    city_country = f"{city}, {country}".title()
    if population:
        population = f"population {population}"
        return f"{city_country} - {population}"
    else:
        return city_country