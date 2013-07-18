""" Fetch and parse stenograms """

from datetime import date
from path import path
import requests


def fetch_day(day):
    contents_page = requests.get(
        'http://www.cdep.ro/pls/steno/steno.data',
        params={
            'cam': 2,
            'dat': day.strftime('%Y%m%d'),
            'idl': 1,
        })

    print contents_page.text


if __name__ == '__main__':
    import requests_cache
    here = path(__file__).abspath().parent
    requests_cache.install_cache(here / 'http_cache')
    fetch_day(date(2013, 6, 10))
