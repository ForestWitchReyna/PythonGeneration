from country_info import get_country_code, get_country_currency, transform

def test_get_country_code():
    countries = [{'name': 'Argentina', 'alpha3Code': 'ARS'}]
    assert get_country_code(countries, "Argentina") == "ARS"
    assert get_country_code(countries, "Argintina") == None


def test_get_country_currency():
    # country['currencies'][0]['code']
    countries = [{'name': 'Argentina', 
                  'currencies': [{'code': 'ARS'}]}]
    assert get_country_currency(countries, "Argentina") == "ARS"
    assert get_country_currency(countries, "Brazil") == None


def test_transform():

    def mock_get_countries():
        countries = [{'name': 'Argentina', 'alpha3Code': 'ARS'}]
        return countries

    def mock_get_country_code(countries, name):
        return "ARS"

    def mock_get_country_currency(countries, name):
        return "ARS"

    assert transform("Argentina", mock_get_countries, mock_get_country_code, 
                     mock_get_country_currency) == {"name": "Argentina", "country_code": "ARS", "currency_code": "ARS"}

