#!/bin/bash
# feed-analyzer.sh
# Finds the Top 5 Most Active Users in twitter_dataset.csv
# Uses a short Python one-liner to correctly extract the Username column
# (the CSV contains multi-line quoted fields that break naive cut-based parsing),
# then pipes through sort | uniq -c | sort -rn | head -5.

FILE="${1:-twitter_dataset.csv}"

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

echo "============================================================"
echo "  Top 5 Most Active Users in $FILE"
echo "============================================================"

# Extract the Username column properly, then sort, count, and display top 5
python -c "
import csv, sys
with open('$FILE', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Username'])
" | sort | uniq -c | sort -rn | head -5