#!/usr/bin/env python3
"""Fetch and process post data from JSONPlaceholder API."""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save to CSV with id, title, and body."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]

        with open("posts.csv", mode="w", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)

