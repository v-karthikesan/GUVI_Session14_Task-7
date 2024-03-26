import requests


class BreweryInfoFetcher:
    def __init__(self, states):
        self.states = states
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def fetch_breweries(self, state):
        try:
            response = requests.get(f"{self.base_url}?by_state={state}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {state}: {e}")
            return []

    def list_breweries_by_state(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            if breweries:
                print(f"\nBreweries in {state}:")
                for brewery in breweries:
                    print(brewery['name'])

    def count_breweries_by_state(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            print(f"\nNumber of breweries in {state}: {len(breweries)}")

    def count_brewery_types_by_city(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            print(f"\nTypes of breweries in cities of {state}:")
            city_brewery_count = {}
            for brewery in breweries:
                city = brewery.get('city', 'Unknown')
                brewery_type = brewery.get('brewery_type', 'Unknown')
                city_brewery_count[city] = city_brewery_count.get(city, {})
                city_brewery_count[city][brewery_type] = city_brewery_count[city].get(brewery_type, 0) + 1
            for city, types_count in city_brewery_count.items():
                print(f"{city}: {types_count}")

    def count_and_list_breweries_with_websites(self):
        for state in self.states:
            breweries = self.fetch_breweries(state)
            websites_count = sum(1 for brewery in breweries if brewery.get('website_url'))
            print(f"\nNumber of breweries with websites in {state}: {websites_count}")
            print(f"Websites of breweries in {state}:")
            for brewery in breweries:
                if brewery.get('website_url'):
                    print(brewery['name'], "-", brewery['website_url'])


# Main program
states = ["Alaska", "Maine", "New York"]
brewery_info_fetcher = BreweryInfoFetcher(states)

# List breweries by state
brewery_info_fetcher.list_breweries_by_state()

# Count breweries by state
brewery_info_fetcher.count_breweries_by_state()

# Count brewery types by city
brewery_info_fetcher.count_brewery_types_by_city()

# Count and list breweries with websites by state
brewery_info_fetcher.count_and_list_breweries_with_websites()
