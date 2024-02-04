# Golden Age of Gaming Analysis

## Introduction
This project explores the evolution of video games from 1980 to the present, aiming to identify the "Golden Age of Gaming." Through comprehensive data analysis, we investigate trends in game releases, reception, playtime, and sales, leveraging data from the RAWG Video Games Database API and other sources. Our goal is to pinpoint when and why certain periods in gaming history stood out in terms of innovation, quality, and player engagement.

## Technologies and Tools Used
- **Programming Languages**: Python
- **Data Analysis Libraries**: Pandas, NumPy, Matplotlib
- **Other Tools**: VSCode 2023, Jupyter Notebooks

## Installation and Setup Instructions
### Dependencies
- Python 3.12+
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Requests
- Seaborn

### Installation Instructions
1. Clone the repository:
```
git clone https://github.com/yourgithub/gaming_analysis.git
```
2. Navigate to the project directory and install the required packages using pip:
```
pip install -r requirements.txt
```

## Usage
To run the analysis, execute the following command in the terminal:
```
python analysis_script.py
```
For detailed analysis, open the Jupyter Notebooks in the `notebooks` directory:
```
jupyter notebook exploration.ipynb
```

## Data
### Data Sources
- **RAWG Video Games Database API**: Provides extensive data on video games, their ratings, platforms, and release dates.
- **Steam Spy API**: Used for gathering additional data on game sales and player numbers.

### Data Description
The dataset includes over 20,000 video games released from 1980 to 2023, with variables covering game titles, release dates, platforms, ratings, and metacritic scores. Data preprocessing involved cleaning, normalization, and merging data from multiple sources.

## Methodology
Our analysis employs statistical methods and time series analysis to examine trends over time. We focused on correlating game release volumes, ratings, and sales data to identify peak periods of gaming innovation and engagement.

## Results
### Findings
- The late 1990s to early 2000s emerged as a significant period, with a spike in high-quality game releases and innovations in gaming technology.
- Platform analysis revealed the dominance of PC and console gaming in different eras.

### Visualizations
![Game Releases Over Time](images/releases_over_time.png)
*Figure 1: Trends in game releases over the years.*

## Conclusion and Future Work
This project highlights several key periods in gaming history that could be considered the "Golden Age." Future work will delve deeper into genre-specific trends and the impact of online gaming and digital distribution on the industry.

## Contributing
Contributions are welcome! If you're interested in collaborating or have suggestions for further analysis, please open an issue or submit a pull request.

## License
This work is licensed under CC BY-NC-SA 4.0. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/

## Contact Information
For any queries or discussions, feel free to contact me at your.email@example.com.

## Acknowledgments
- RAWG for providing access to their comprehensive video games database.
- Steam Spy for additional sales data.
- My mentor and peers who provided invaluable feedback and support.



