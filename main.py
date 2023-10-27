import sys

from rich import print
from rich.prompt import Prompt

from utils import create_local_repository, is_connected_to_internet, upload_to_github, is_git_installed

if __name__ == "__main__":
    if is_connected_to_internet() == False:
        print("[red]You are not connected to the internet![/red]")
        sys.exit()
    if is_git_installed() == False:
        print("[red]Git is not installed on your system.[/red]")
        sys.exit()
    else:

        # Provide a warning and information about obtaining a GitHub access token
        print("[orange]Before running the application, make sure you have a GitHub access token.[/orange]")
        print("[orange]You can obtain a GitHub access token by following these steps:[/orange]")
        print("[orange]1. Visit GitHub Settings: https://github.com/settings/tokens[/orange]")
        print("[orange]2. Click 'Generate token.'[/orange]")
        print("[orange]3. Provide a token description and select the necessary scopes (e.g., repo, workflow).[/orange]")
        print("[orange]4. Click 'Generate token.'[/orange]")
        print("[orange]5. Copy the generated token and store it in a safe place.[/orange]")
        print("[orange]For more information visit this site: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens[/orange]")

        create_local_repository()

        upload_repo = Prompt.ask(
            "Do you want to upload the repository to GitHub? (yes/no): "
        )

        if upload_repo.lower() == "yes":
            upload_to_github()
        else:
            print(
                "[orange]Local repository created. You can manually push it to GitHub later.[/orange]"
            )
