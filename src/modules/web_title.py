# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# gedit: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

""" Define the title of web pages in irc. """

from requests import get

from logger import LOGGER
from utils import parse_int

try:
    from lxml import etree
except ImportError:
    LOGGER.error(
        "DAMMMMNNN!!!! You don't have lxml etree support! Enable it! GO GO GO!"
    )
    raise


def get_title(url):
    """ Find the title of a url address. """
    title = ""
    content_type = "text/html"

    response = get(url, headers={"Accept": content_type}, stream=True)

    if 200 < response.status_code >= 300:
        # pylint: disable=bad-continuation
        LOGGER.warning(
            "get_title: Error %s occurred when fetching URL %s",
            response.status_code,
            url,
        )
    elif "Content-Type" in response.headers and not response.headers[
        "Content-Type"
    ].startswith(content_type):
        # pylint: disable=bad-continuation
        LOGGER.warning(
            "get_title: Content type of %s is not %s when accessing URL %s",
            response.headers["Content-Type"],
            content_type,
            url,
        )
    elif (
        "Content-Length" in response.headers
        and parse_int(response.headers["Content-Length"], 0) > 1024 ** 2
    ):
        # pylint: disable=bad-continuation
        LOGGER.warning(
            "get_title: Content length is greater than 1MB when accessing URL %s", url
        )
    else:
        LOGGER.info("get_title for %s: status = %s", url, response.status_code)

        response.raw.decode_content = True

        # pylint: disable=c-extension-no-member,unused-variable
        for event, element in etree.iterparse(
            response.raw, tag="title", html=True, events=["end"]
        ):
            title = element.text
            break

        response.close()

    return title
