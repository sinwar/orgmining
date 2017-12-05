AUTH = ('sinwar', '######')

DATABASE_NAME = 'mining'

REPO_NAMES = ['<GITHUB_REPOSITORY_NAMES>']

EXCLUDED_USERS = ['0x48piraj']

SLACK_USERS = {
    '<GITHUB_USERNAME>': '<SLACK_USERNAME>',
}

REPOS_URL = 'https://api.github.com/orgs/coala/repos'

ISSUES_URL = ('https://api.github.com/repos/coala/'
              '{repo}/issues?state=all&filter=all')

EVENTS_URL = ('https://api.github.com/repos/coala/'
              '{repo}/issues/{number}/events')

COMMITS_URL = ('https://api.github.com/repos/coala/'
               '{repo}/commits')

BACK_END_QUERIES = ['<BACK_END_FOLDERS_OR_FILES>']

FRONT_END_QUERIES = ['<FRONT_END_FOLDERS_OR_FILES>']

SETUPER_QUERIES = ['SETUPER_FOLDER_OR_FILES']
