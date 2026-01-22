# Project 02 – Linux Fundamentals

## Navigation Commands

pwd
- Print working directory

ls
- List files in current directory

ls -la
- List all files (including hidden) with detailed view

cd /
- Move to root directory

cd ~
- Move to home directory

cd <folder>
- Change into a directory

cd ..
- Move up one directory


## File & Directory Management

mkdir <folder>
- Create directory

touch file.txt
- Create empty file

rm file.txt
- Remove file

rm -r <folder>
- Remove directory recursively


## Permissions

ls -l
- View permissions

chmod u-w file.txt
- Remove write permission from user

chmod +x file.txt
- Add execute permission

Permission format example:
-rwxr-xr-x
Owner | Group | Others


## Editing Files

nano file.txt
- Open file in nano editor

CTRL + O
- Save

CTRL + X
- Exit


## Git Commands Used

git status
- Check current changes

git add .
- Stage changes

git commit -m "message"
- Commit changes

git push
- Push to remote

git pull --rebase
- Sync local with remote before pushing


## Key Learning

- Always check directory before running git add
- Understand file permissions before modifying files
- Rebase fixes remote ahead errors
- Structure projects clearly inside repo
