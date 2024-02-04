import requests
import pandas as pd
import time

def fetch_data_with_retry(url: str, params: dict, max_retries=5) -> requests.Response:
    for attempt in range(max_retries):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response  # Successfully got a response
        elif response.status_code == 502:
            print(f"Retry {attempt + 1} of {max_retries} due to 502 error. Waiting {2 ** attempt} seconds.")
            time.sleep(2 ** attempt)  # Exponential backoff
        else:
            print(f"Failed with status code {response.status_code}. Stopping retries.")
            break  # Break on other errors
    return None  # Return None if all retries fail or if non-retryable error occurs

def fetch_games_by_year(api_key: str, start_year: int, end_year: int) -> None:
    for year in range(start_year, end_year + 1):
        print(f"Fetching data for {year}...")
        games_list = []
        page = 1
        while True:
            url = "https://api.rawg.io/api/games"
            params = {
                "key": api_key,
                "dates": f"{year}-01-01,{year}-12-31",
                "page": page,
                "page_size": 40,  # Adjust based on your API's allowed maximum to minimize requests
                "ordering": "-metacritic"  # Order by Metacritic score, descending
            }
            response = fetch_data_with_retry(url, params)
            if response and response.status_code == 200:
                data = response.json()
                games_data = data['results']
                if not games_data:
                    print(f"All data fetched for {year}.")
                    break  # Stop if there are no games returned for the current page

                for game in games_data:
                    games_list.append({
                        "name": game['name'],
                        "release_date": game['released'],
                        "rating": game.get('rating', None),  # Already extracting 'rating'
                        "rating_top": game.get('rating_top', None),
                        "metacritic": game.get('metacritic', None),
                        "playtime": game.get('playtime', None),
                        "genres": ", ".join([genre['name'] for genre in game.get('genres', [])] if game.get('genres') else []),
                    })
                
                page += 1  # Increment to fetch the next page
            elif not response or response.status_code == 404:
                print(f"No more data available for {year} or failed to fetch data. Stopped at page {page}.")
                break  # Stop the loop if no response or a 404 error is encountered

        # Convert the list to a DataFrame and save to a CSV file
        games_df = pd.DataFrame(games_list)
        filename = f"RAWG_gameinfo_{year}.csv"
        games_df.to_csv(filename, index=False)
        print(f"Data for {year} saved to {filename}")

# Example usage
if __name__ == "__main__":
    api_key = "e1da0c7cc6d94de2b4a97e1ce1e34775"
    fetch_games_by_year(api_key, int(input("Staring Year: ")), int(input("Ending Year: ")))
