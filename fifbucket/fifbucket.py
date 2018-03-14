#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals
from urllib.parse import urlencode
import logging
import requests

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class Bitbucket():
    def __init__(self, bitbucket_url='https://api.bitbucket.org/2.0/repositories',
                 owner=None, username=None, password=None, verify=True):
        self.bitbucket_url = bitbucket_url
        self.owner = owner
        self.verify = verify
        self.API_URL = '{}/{}'.format(bitbucket_url, owner)
        self.username = username
        self.password = password

    def __request(self, method, url, params=None):
        logger.info('{} {} Params: {}'.format(method, url, params))
        r = requests.request(
            method, url, json=params, verify=self.verify, auth=(
                self.username, self.password)
        )
        logger.debug(r.content)
        r.raise_for_status()
        try:
            return r.json()
        except ValueError as e:
            logger.error(e.message)
            return r.content

    def __get(self, url, params=None):
        return self.__request('GET', url, params)

    def __post(self, url, params=None):
        return self.__request('POST', url, params)

    def __delete(self, url, params=None):
        return self.__request('DELETE', url, params)

    def get_repos(self, page=None, query=None):
        url = self.API_URL
        qstr = {}
        if page:
            qstr['page'] = page
        if query:
            qstr['q'] = query
        qstr = urlencode(qstr)
        if qstr:
            url = '{}?{}'.format(url, qstr)
        print(url)
        return self.__get(url)

    def get_pr(self, repo_slug=None, query=None):
        url = '{}/{}/pullrequests'.format(self.API_URL, repo_slug)
        qstr = {}
        if query:
            qstr['q'] = query
        qstr = urlencode(qstr)
        if qstr:
            url = '{}?{}'.format(url, qstr)
        return self.__get(url)
