# Version Control

## Lesson Plan 1 - Lesson - Introduction to Version Control

*Lesson Objective* - Learn the importance of version control and the fundamentals of git and GitHub

- Go through the [version control slides](./slide_builds/version_control_1-export.pdf)
- Go through [my_first_repo_example_start](my_first_repo_example_start/README.md)
- Go through or assign the first four exercises of [Learn Git Branching](https://learngitbranching.js.org/)
- Get them to do the first [Exercise](./exercise_version_control/README.md)
  - Work with students to get one of their projects cloned. So that they can start using git.

## Lesson Plan 2 - Lab

- Get them to go over the lab of version control.

## Lesson Plan 3/4 (Optional or taught later on.)

*Lesson Objective* - Learn how to effectively work with others in a team using git and GitHub.

- Go through example [working with git](./working-together-with-git/README.md) Using the template Repository [working together with git](https://github.com/CPSC-1012/working-together-with-git) create a new github classroom assignment for this.
  - Work with them to get their projects pulled down locally.
    - don't enable feedback pull requests on this one.
  - Talk about branching
  - Talk about pull requests
  - Talk about fetch/pull
  - Discuss Merge Conflicts and how it's a thing they'll use in the future.
  - This is a 100% guided example with students so that they can get a feel of the problems that arise.

## Topics to cover
- What is version control?
- Why is it important?
- Who uses git and GitHub?
- What is a repository?
- How does a repository work?
- Talk about the different areas of git and the process of getting there.
  - untracked
  - changed
  - staged
  - committed
- Talk about remote repositories (GitHub)
  - What is a remote repository?
  - Talk about other options (GitLab, Bitbucket)

- Talk about branches and pull requests
  - why they're important

- Talk about the commands that are handy.
  - `git init`
  - `git status`
  - `git diff`
    - `git diff --staged`
  - `git add <file or anything>`
  - `git commmit -m "message"`
  - `git push` (origin)
  - `git pull`
    - `git fetch`
  - `git checkout -b <branch name>`
    - `git checkout <branch name>`
  - `git log`
    - `git log --graph`
  - `git remote add origin <remote repository url>`
  - `git remote -v`
