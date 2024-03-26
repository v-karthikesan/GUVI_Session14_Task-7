import requests

class CountryInfoFetcher:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    def display_country_info(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        for country in self.data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            currency_info = ", ".join([f"{code} ({details.get('name', 'N/A')})" for code, details in currencies.items()])
            print(f"Country: {name}")
            print(f"Currencies: {currency_info}")
            print("-" * 50)

    def display_dollar_countries(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        dollar_countries = [country.get('name', {}).get('common', 'N/A') for country in self.data 
                            if 'currencies' in country and 'USD' in country['currencies']]
        if dollar_countries:
            print("\nCountries with DOLLAR as currency:")
            print(", ".join(dollar_countries))
        else:
            print("No countries found with DOLLAR as currency.")

    def display_euro_countries(self):
        if self.data is None:
            print("Data not fetched. Call fetch_data() first.")
            return

        euro_countries = [country.get('name', {}).get('common', 'N/A') for country in self.data 
                          if 'currencies' in country and 'EUR' in country['currencies']]
        if euro_countries:
            print("\nCountries with EURO as currency:")
            print(", ".join(euro_countries))
        else:
            print("No countries found with EURO as currency.")

# Main program
url = "https://restcountries.com/v3.1/all"
country_info_fetcher = CountryInfoFetcher(url)

# Fetch data from the URL
country_info_fetcher.fetch_data()

# Display country information
country_info_fetcher.display_country_info()

# Display countries with DOLLAR as currency
country_info_fetcher.display_dollar_countries()

# Display countries with EURO as currency
country_info_fetcher.display_euro_countries()





