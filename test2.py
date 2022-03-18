import requests 

repo = 'Chandrasekhar674/test-ghpage'
branch = 'main'
access_token = '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'

r = requests.put(
    'https://api.github.com/repos/{0}/branches/{1}/protection'.format(repo, branch),
    headers = {
        'Accept': 'application/vnd.github.luke-cage-preview+json',
        'Authorization': 'Token {0}'.format(access_token)
    },
    json = {
        "restrictions": {
            "users": [
              "chandrasekhar674"
            ]
        },
        "required_status_checks": None,
        "enforce_admins": None,
        "required_pull_request_reviews": None
    }
)
print(r.status_code)
print(r.json())