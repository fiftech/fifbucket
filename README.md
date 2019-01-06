
# fifbucket 
[![Build Status](https://travis-ci.com/fiftech/fifbucket.svg?branch=master)](https://travis-ci.com/fiftech/fifbucket) [![Coverage Status](https://coveralls.io/repos/github/fiftech/fifbucket/badge.svg?branch=master)](https://coveralls.io/github/fiftech/fifbucket?branch=master) [![Pypi Status](https://pypip.in/v/fifbucket/badge.png)](https://pypi.python.org/pypi/fifbucket/) [![Pypi Download](https://pypip.in/d/fifbucket/badge.png)](https://pypi.python.org/pypi/fifbucket/) [![Pypi Wheel](https://pypip.in/wheel/fifbucket/badge.png)](https://pypi.python.org/pypi/fifbucket/)


**fifbucket** is a python library for call Bitbucket api: 
> Bitbucket Api Documentation: https://developer.atlassian.com/bitbucket/api/2/reference/resource/

## Configuration

Obligatory arguments

| Argument       |Description                              |
|----------------|-----------------------------------------|
|owner           |`Bitbucket repository owner`             |
|username        |`Bitbucket username`                     |
|password        |`Bitbucket user password or app password`|


## Basic usage
**How install**
```bash
pip install fifbucket
```

**How load the class:**
```python
# -*- coding: utf-8 -*-

OWNER="owner"
BITBUCKET_USER="username"
BUTBUCKET_PASSWORD="password"

from fifbucket.client import Bitbucket
bitbucket = Bitbucket(owner=OWNER, username=BITBUCKET_USER, password=BUTBUCKET_PASSWORD)
```
**get_repos(query) example:** list all repository from a project
* API info: [`https://api.bitbucket.org/2.0/repositories/{username}`](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D)
```python
PROJECT = 'PROJ'
QUERY = 'query='project.key="{}"'.format(PROJECT)'
bitbucket.get_repos(query=QUERY)
```
**get_pr example(repo_slug, query) example:** list pull request info from a repo
* API info: [`https://api.bitbucket.org/2.0/repositories/{username}/{repository}/pullrequests`](https://developer.atlassian.com/bitbucket/api/2/reference/resource/repositories/%7Busername%7D/%7Brepo_slug%7D/pullrequests)

```python
REPOSITORY = 'repository_slug'
bitbucket.get_pr_info(REPOSITORY)
```

**get_permissions(query) example:** list info of all admins in a repository
* API info: [`https://api.bitbucket.org/2.0/teams/{username}/permissions/repositories`](https://developer.atlassian.com/bitbucket/api/2/reference/resource/teams/%7Busername%7D/repositories)

```python
REPOSITORY = 'repository_slug'
QUERY = 'repository.name="{}" AND permission="admin"'.format(REPOSITORY)
bitbucket.get_permissions(query=QUERY)
```