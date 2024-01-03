from city_functions import format_city_country

def test_city_country():
    """A function to test format_city_country"""
    city_country = format_city_country('santiago','chile')
    assert city_country == 'Santiago, Chile'

def test_city_country_population():
    """A function to test format_city_country with population"""
    city_country = format_city_country('santiago','chile', population='500000')
    assert city_country == 'Santiago, Chile - population 500000'