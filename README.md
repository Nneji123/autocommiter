# Autocommiter

This repository contains utility functions for the Autocommiter tool.

## Introduction

Autocommiter is a Python utility that automates the process of creating a local Git repository, setting up GitHub Actions for scheduled commits, and uploading the repository to GitHub.

## Features

- Create a local Git repository
- Set up GitHub Actions for scheduled commits
- Generate a comprehensive README
- Add a license to your project

## Usage

### Prerequisites
Before using Autocommiter, make sure you have:

Python installed on your system
A GitHub account with a personal access token

A Desktop application is also available for Windows users in case you don't have Python installed on your system.
### Create a Local Repository

1. Run the `create_local_repository` function.
2. Follow the prompts to provide a folder name and a TXT file name.
3. Schedule the automatic commits by entering a time in UTC.

### GitHub Actions Configuration

The `create_local_repository` function automatically creates a GitHub Actions workflow file (`.github/workflows/auto_commit.yml`). This workflow is scheduled to run at the specified time every day.

```yaml
name: Auto Commit

on:
  schedule:
    - cron: '[cron_expression]'

permissions:
  contents: write

jobs:
  update-text-file:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Repository
      uses: actions/checkout@v3

    - name: Update TXT File
      run: echo $(date) >> [file_name].txt

    - name: Commit Changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        git commit -am "Auto commit at $(date)"
        git push
```

### Author
[Ifeanyi Nneji](https://github.com/Nneji123)

### Acknowledgments
Special thanks to the Autocommiter community for their support and contributions.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
