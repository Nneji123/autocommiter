import sys
from rich import print
from rich.prompt import Prompt
from utils import create_local_repository, is_connected_to_internet, upload_to_github

if __name__ == '__main__':
    if is_connected_to_internet() == False:
        print("[red]You are not connected to the internet![/red]")
        sys.exit()
    else:
        create_local_repository()
        upload_repo = Prompt.ask("Do you want to upload the repository to GitHub? (yes/no): ")

        if upload_repo.lower() == 'yes':
            upload_to_github()
        else:
            print("[yellow]Local repository created. You can manually push it to GitHub later.[/yellow]")

