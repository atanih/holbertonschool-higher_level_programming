#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and process them."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch all the posts and print the title of each one."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all the posts and save id, title and body into posts.csv."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        rows = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]
        fields = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
