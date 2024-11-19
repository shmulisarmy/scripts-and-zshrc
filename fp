#!/bin/bash

# Function to print messages in color
print_message() {
  echo -e "\e[34m$1\e[0m" # Blue text for general info
}

print_error() {
  echo -e "\e[31mError: $1\e[0m" # Red text for errors
}

# Check if there are changes to commit
  # Prompt for commit message
  print_message "Enter a commit message (or press Enter to use the default '...'):"
  read -r commit_message

  # Use default message if none provided
  commit_message="${commit_message:-...}"

  # Add all changes, commit, and push
  git add *
  git commit -m "$commit_message"
  if git push; then
    print_message "Changes successfully pushed to the repository!"
  else
    print_error "Failed to push changes. Check your Git configuration and network connection."
  fi

