from fifbucket.client import Bitbucket
import json

bitbucket = Bitbucket(owner='owner', username='username', password='password')


data_first = {
    'size': 1,
    'values': ['data_first'],
    'pagelen': 100,
    'next': 'https://api.bitbucket.org/2.0/next'
}

data_second = {
    'size': 1,
    'values': ['data_second'],
    'pagelen': 100,
    'previous': 'https://api.bitbucket.org/2.0/previous'
}


def test_get_repos(requests_mock):
    requests_mock.get('https://api.bitbucket.org/2.0/repositories/owner', text=json.dumps(data_first))
    requests_mock.get('https://api.bitbucket.org/2.0/next', text=json.dumps(data_second))
    query = 'project.key="PROJ"'
    assert ['data_first', 'data_second'] == bitbucket.get_repos(query)


def test_get_repo_pr(requests_mock):
    repository_slug = 'repository_slug'
    requests_mock.get(
        'https://api.bitbucket.org/2.0/repositories/owner/repository_slug/pullrequests',
        text=json.dumps(data_first)
    )
    requests_mock.get('https://api.bitbucket.org/2.0/next', text=json.dumps(data_second))
    assert ['data_first', 'data_second'] == bitbucket.get_repo_pr(repository_slug)


def test_get_permissions(requests_mock):
    requests_mock.get('https://api.bitbucket.org/2.0/teams/owner/permissions/repositories', text=json.dumps(data_first))
    requests_mock.get('https://api.bitbucket.org/2.0/next', text=json.dumps(data_second))
    query = 'repository.name="repository_slug" AND permission="admin"'
    assert ['data_first', 'data_second'] == bitbucket.get_permissions(query)


def test_get_permissions_repo(requests_mock):
    repository_slug = 'repository_slug'
    requests_mock.get('https://api.bitbucket.org/2.0/teams/owner/permissions/repositories/repository_slug',
                      text=json.dumps(data_first))
    requests_mock.get('https://api.bitbucket.org/2.0/next', text=json.dumps(data_second))
    query = 'permission="admin"'
    assert ['data_first', 'data_second'] == bitbucket.get_permissions_repo(repository_slug, query)
