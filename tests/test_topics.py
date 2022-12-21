"""Basic test to always pass"""
from __future__ import annotations

import os

from github import Github

from src.topics import ALL_TOPICS

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def test_contains_topics() -> None:
    """Simple Test to check if all repos have at least one tracker topic"""
    for repo in g.get_user().get_repos(affiliation="owner"):
        tracker_topics = [topic for topic in repo.get_topics() if topic in ALL_TOPICS]
        assert (
            len(tracker_topics) > 0
        ), f"Repo {repo.name} does not have any tracker topics"
