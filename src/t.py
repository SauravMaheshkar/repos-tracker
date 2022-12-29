from src.get_repos import create_repo_list

tracker_misc_table = create_repo_list("tracker-misc")
with open('README.md', 'w') as f:
    f.write(tracker_misc_table)