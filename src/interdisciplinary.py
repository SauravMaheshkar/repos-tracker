"""Serialize a list of interdisciplinary projects to JSON"""
import os
import timeit

from github import Github

from src.topics import ALL_TOPICS
from src.utils import write_to_json

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))


def get_interdisciplinary_projects() -> None:
    """
    Create a JSON file with a list of all interdisciplinary projects.

    :return: None
    """
    interdisciplinary_projects = []
    for repo in g.get_user().get_repos(affiliation="owner"):
        tracker_topics = [topic for topic in repo.get_topics() if topic in ALL_TOPICS]
        if len(tracker_topics) > 1:
            interdisciplinary_projects.append(repo.name)

    write_to_json(
        file_name="bin/interdisciplinary.json", data=interdisciplinary_projects
    )

    del interdisciplinary_projects


if __name__ == "__main__":
    print(
        timeit.timeit(
            "get_interdisciplinary_projects()",
            setup="from __main__ import get_interdisciplinary_projects",
            number=1,
        )
    )
