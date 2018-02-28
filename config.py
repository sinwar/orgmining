AUTH = ('sinwar', '4premsinwar')

DATABASE_NAME = 'mining'

REPO_NAMES = ['sp2admn']

EXCLUDED_USERS = ['0x48piraj']

SLACK_USERS = {
    'sinwar': 'sinwar',
}

REPOS_URL = 'https://api.github.com/orgs/sppadmn/repos'

ISSUES_URL = ('https://api.github.com/repos/sppadmn/'
              '{repo}/issues?state=all&filter=all')

EVENTS_URL = ('https://api.github.com/repos/sppadmn/'
              '{repo}/issues/{number}/events')

COMMITS_URL = ('https://api.github.com/repos/sppadmn/'
               '{repo}/commits')

BACK_END_QUERIES = ["adduser.php", "ind.php", "admin.php", "login.php", "json.php"]

FRONT_END_QUERIES = ["css/, mini"]

SETUPER_QUERIES = ["images"]
