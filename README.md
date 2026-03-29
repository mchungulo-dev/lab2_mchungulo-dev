# Lab 2: The Social Media Data Detective

## Usage Instructions

**Python script** — run from the project directory (the CSV must be in the same folder):

```bash
python3 data-detective.py
```

The script will clean the data, display the most-liked tweet, print the Top 10 tweets by Likes, and then prompt you to enter a keyword to search.

**Bash script** — make it executable, then run it with the CSV as an argument:

```bash
chmod +x feed-analyzer.sh
./feed-analyzer.sh twitter_dataset.csv
```

## How the Custom Sorting Algorithm Works

The program uses **Selection Sort** to order tweets by Likes in descending order. It iterates through the list one position at a time; for each position it scans every remaining unsorted element to find the one with the highest Likes count, then swaps that element into the current position. After completing all passes the entire list is sorted from most to fewest likes, and the first ten entries are sliced off as the Top 10.
