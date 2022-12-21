"""Serialize a list of all repositories that have a specific topic."""
import os
import timeit

from github import Github

from src.topics import ALL_TOPICS
from src.utils import write_to_json

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def create_repo_list(tracker_topic: str) -> None:
    """
    Create a JSON file with a list of all repos that have a specific topic.

    :param topic: The topic to search for.
    :type topic: str
    :return: None
    """
    repos = []
    for repo in g.get_user().get_repos(affiliation="owner"):
        if tracker_topic in repo.get_topics():
            repos.append(repo.name)

    write_to_json(file_name=f"bin/{tracker_topic}.json", data=repos)

    del repos


if __name__ == "__main__":
    for topic in ALL_TOPICS:
        print(
            timeit.timeit(
                "create_repo_list(topic)",
                setup="from __main__ import create_repo_list, topic",
                number=1,
            )
        )
