# Week 0 — Billing and Architecture

## Subheading

This is a description. Here are some bullet points:

- Point 1
- Point 2
- Point 3

And here is an AWS IAM permission `ec2:DescribeInstances`

### Table

This is a table.

| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| value 1a | value 2a | value 3a |
| value 1b | value 2b | value 3b |

## playground-data-scrub

We are going to learn how to scrub passwords from our repo, and to detect AWS Credentials

### Steps

#### Use trufflesecurity

Identifies files that may have secrets - https://github.com/trufflesecurity/trufflehog

#### Use BFG

Use to remove secrets in repository - https://rtyley.github.io/bfg-repo-cleaner/

- Run `brew install bfg`
- Use text file e.g., 'replacements.txt'
- Run bfg tool - `bfg --replace-text replacements.txt`
- `git reflog expire --expire=now --all && git gc --prune=now --aggressive`
- Do `git push --force` (dangerous)
- Drops commits containing secrets
