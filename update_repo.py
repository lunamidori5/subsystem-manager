import os
import git

def update_repo():
    """
    Checks if the current Git repository is up-to-date and pulls changes if not.
    Operates on the repository in the current working directory.
    Asks for user confirmation before pulling changes.
    """
    repo_path = os.getcwd()

    try:
        repo = git.Repo(repo_path)

        if repo.bare:
            print(f"Repository at {repo_path} is bare, skipping update.")
            return False
        
        origin = repo.remotes.origin
        print(f"Fetching latest changes from remote for {repo_path}...")
        origin.fetch()

        local_commit = repo.head.reference.commit

        remote_commit = origin.refs[repo.head.reference.name].commit

        if local_commit == remote_commit:
            print("Repository is already up-to-date.")
            return False
        else:
            print("Repository is not up-to-date.")
            print("Pulling changes...")
            try:
                origin.pull()
                print("Successfully pulled changes.")
                return True
            except Exception as e:
                print(f"Error pulling changes: {e}")
                return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False