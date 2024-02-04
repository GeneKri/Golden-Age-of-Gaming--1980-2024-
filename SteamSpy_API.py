import requests
import time
import pandas as pd

def fetch_all_games(base_url: str, start_page: int, end_page: int) -> list:
    """Fetch a list of all games across specified pages."""
    all_games = []
    for page in range(start_page, end_page + 1):
        print(f"Fetching data for page {page}...")
        params = {
            'request': 'all',
            'page': page
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            games = response.json()
            if games:
                all_games.extend(games.values())  # Assuming the API returns a dict with appid as keys
            else:
                print(f"No more data available at page {page}.")
                break
        else:
            print(f"Failed to fetch page {page} with status code {response.status_code}")
        
        time.sleep(60)  # Respect the allowed poll rate for 'all' requests

    return all_games

def save_games_to_csv(games: list, filename: str) -> None:
    """Convert the list of games to a DataFrame and save to a CSV file."""
    games_df = pd.DataFrame(games)
    games_df.to_csv(filename, index=False)
    print(f"Data saved to {filename}.")

def main():
    base_url = "https://steamspy.com/api.php"
    start_page = int(input("Enter the starting page number: "))
    end_page = int(input("Enter the ending page number: "))

    all_games = fetch_all_games(base_url, start_page, end_page)

    # Example filename: steam_spy_all_games_page_0_to_10.csv
    filename = f"steam_spy_page_{start_page}_to_{end_page}.csv"
    save_games_to_csv(all_games, filename)

if __name__ == "__main__":
    main()
