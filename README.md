# mobi-viz
This repository is designed to share visualization code for mobility data.
Intended use: this code is intended to visualize household equipment, travel time and mode share .
## set-up
You can use package manager uv to download all required libraries in no time!\
First install uv: https://docs.astral.sh/uv/getting-started/installation/#standalone-installer \
Then install python by typing the following command in terminal: uv python install\
Finally, install the required packages: uv add numpy; uv add pandas; uv add matplotlib\
You're good to go! You can execute the code by calling: uv run main.py
## use case
The code first loads mobility survey data, and produces three graphs: a mobility equipment bar chart, a travel time histogram and a mode share donut chart