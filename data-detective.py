import csv
import sys
import os


def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)

    return raw_tweets


def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    - Remove tweets whose Text field is missing or empty.
    - Replace empty Likes or Retweets with 0.
    - Return a clean list and print how many rows were fixed/removed.
    """
    cleaned = []
    removed_count = 0
    fixed_count = 0

    for tweet in tweets:
        # Check if Text is missing or empty
        text_value = tweet.get('Text', '').strip()
        if len(text_value) == 0:
            removed_count += 1
            continue  # skip this tweet entirely

        # Check and fix missing Likes
        likes_value = tweet.get('Likes', '').strip()
        if len(likes_value) == 0:
            tweet['Likes'] = '0'
            fixed_count += 1

        # Check and fix missing Retweets
        retweets_value = tweet.get('Retweets', '').strip()
        if len(retweets_value) == 0:
            tweet['Retweets'] = '0'
            fixed_count += 1

        cleaned.append(tweet)

    print("=" * 60)
    print("QUEST 1: Data Auditor Report")
    print("=" * 60)
    print(f"  Rows removed (missing Text):     {removed_count}")
    print(f"  Fields fixed  (empty Likes/RTs):  {fixed_count}")
    print(f"  Clean tweets remaining:           {len(cleaned)}")
    print()

    return cleaned


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest Likes.
    Does NOT use the max() function.
    """
    if len(tweets) == 0:
        print("No tweets to analyze.")
        return None

    # Start by assuming the first tweet is the most-liked
    viral = tweets[0]
    highest_likes = int(viral['Likes'])

    for i in range(1, len(tweets)):
        current_likes = int(tweets[i]['Likes'])
        if current_likes > highest_likes:
            highest_likes = current_likes
            viral = tweets[i]

    print("=" * 60)
    print("QUEST 2: The Viral Post")
    print("=" * 60)
    print(f"  Username:  {viral['Username']}")
    print(f"  Likes:     {highest_likes}")
    print(f"  Text:      {viral['Text'][:120]}...")
    print()

    return viral


def custom_sort_by_likes(tweets):
    """
    QUEST 3: Selection Sort — sorts tweets by Likes in descending order.
    Does NOT use .sort() or sorted().

    How it works:
    We iterate through the list one position at a time. For each position i,
    we scan the remaining unsorted portion (i+1 to end) to find the tweet
    with the highest Likes, then swap it into position i. After one full
    pass the largest value sits at index 0, the second-largest at index 1,
    and so on, producing a descending-order list.
    """
    # Work on a copy so we don't mutate the original
    data = []
    for tweet in tweets:
        data.append(tweet)

    n = len(data)
    for i in range(n - 1):
        # Assume the current position holds the max of the unsorted part
        max_index = i
        max_likes = int(data[i]['Likes'])

        # Scan the rest of the unsorted portion
        for j in range(i + 1, n):
            current_likes = int(data[j]['Likes'])
            if current_likes > max_likes:
                max_likes = current_likes
                max_index = j

        # Swap the found maximum into position i
        if max_index != i:
            data[i], data[max_index] = data[max_index], data[i]

    # Print the Top 10
    top_10 = data[:10]

    print("=" * 60)
    print("QUEST 3: Top 10 Most Liked Tweets")
    print("=" * 60)
    for rank in range(len(top_10)):
        t = top_10[rank]
        print(f"  #{rank + 1}  |  @{t['Username']}  |  {t['Likes']} likes")
        print(f"        \"{t['Text'][:80]}...\"")
    print()

    return data


def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword (case-insensitive) and extract matching
    tweets into a brand-new list.
    """
    matches = []

    for tweet in tweets:
        # Case-insensitive search
        if keyword.lower() in tweet['Text'].lower():
            matches.append(tweet)

    print("=" * 60)
    print(f"QUEST 4: Content Filter — keyword \"{keyword}\"")
    print("=" * 60)
    print(f"  Tweets matching \"{keyword}\": {len(matches)}")
    print()

    if len(matches) == 0:
        print("  No tweets matched your search.")
    else:
        # Show up to 10 results so the console stays readable
        display_count = len(matches) if len(matches) < 10 else 10
        for i in range(display_count):
            m = matches[i]
            print(f"  [{i + 1}] @{m['Username']}  |  {m['Likes']} likes")
            print(f"      \"{m['Text'][:100]}...\"")
        if len(matches) > 10:
            print(f"\n  ... and {len(matches) - 10} more results.")
    print()

    return matches


# ─────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")

    # Quest 1 — Clean the data
    clean_dataset = clean_data(dataset)

    # Quest 2 — Find the viral (most-liked) tweet
    find_viral_tweet(clean_dataset)

    # Quest 3 — Custom sort and display Top 10
    custom_sort_by_likes(clean_dataset)

    # Quest 4 — Keyword search
    keyword = input("Enter a keyword to search tweets: ").strip()
    search_tweets(clean_dataset, keyword)