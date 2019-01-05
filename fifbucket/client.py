#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from __future__ import unicode_literals
from urllib.parse import urlencode
import logging
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def url_plus_query(url, query=None, page=None):
    qstr = {}
    qstr['pagelen'] = 100
    if query:
        qstr['q'] = query
    if page:
        qstr['page'] = page
    qstr = urlencode(qstr)
    if qstr:
        url = '{}?{}'.format(url, qstr)
    return url


class Bitbucket():
    def __init__(self, api_url='https://api.bitbucket.org/2.0',
                 owner=None, username=None, password=None, verify=True):
        self.API_URL = api_url
        self.OWNER = owner
        self.password = password
        self.username = username
        self.verify = verify

    def __request(self, method, url, params=None):
        logger.info('{} {} Params: {}'.format(method, url, params))
        session = requests.Session()
        retry = Retry(total=5, backoff_factor=1, status_forcelist=[500])
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        request = session.request(
            method, url, json=params, verify=self.verify, auth=(
                self.username, self.password)
        )
        logger.debug(request.content)
        request.raise_for_status()
        try:
            return request.json()
        except ValueError as e:
            logger.error(e.message)
            return request.content

    def __get(self, url, params=None):
        return self.__request('GET', url, params)

    def __post(self, url, params=None):
        return self.__request('POST', url, params)

    def __delete(self, url, params=None):
        return self.__request('DELETE', url, params)

    def __get_value(self, url):
        response_json = self.__get(url)
        values = response_json['values']
        while 'next' in response_json:
            response_json = self.__get(response_json['next'])
            values += response_json['values']
        return values

    def get_repos(self, query=None):
        url = '{}/repositories/{}'.format(self.API_URL, self.OWNER)
        url = url_plus_query(url, query)
        return self.__get_value(url)

    def get_pr(self, repo_slug=None, query=None):
        url = '{}/repositories/{}/{}/pullrequests'.format(self.API_URL, self.OWNER, repo_slug)
        url = url_plus_query(url, query)
        return self.__get(url)

    def get_permissions(self, query=None):
        url = '{}/teams/{}/permissions/repositories'.format(self.API_URL, self.OWNER)
        url = url_plus_query(url, query)
        return self.__get_value(url)
