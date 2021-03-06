import os

from page_loader.url_formatter import to_dirname, to_filename, truncate_name

URL = 'https://ru.hexlet.io/courses'
LINK = '/assets/professions/nodejs.png'
DIR_PATH = '/var/tmp'


def test_generate_dirname():
    CONVERTED_ASSETS_DIRNAME = """/var/tmp/ru-hexlet-io-courses_files/\
ru-hexlet-io-assets-professions-nodejs.png"""
    CONVERTED_DIRNAME = '/var/tmp/ru-hexlet-io-courses.html'
    assert to_dirname(DIR_PATH, URL, '.html') == CONVERTED_DIRNAME
    assets_dirname = to_dirname(DIR_PATH, URL, '_files')
    assert to_dirname(assets_dirname, URL, LINK,
                      is_link=True) == CONVERTED_ASSETS_DIRNAME


def test_to_filename():
    CONVERTED_URL = 'ru-hexlet-io-courses'
    CONVERTED_LINK = 'ru-hexlet-io-assets-professions-nodejs.png'
    assert to_filename(URL, URL) == CONVERTED_URL
    assert to_filename(LINK, URL) == CONVERTED_LINK


def test_truncate_name():
    long_filename = os.path.join(DIR_PATH, 'a' * 256 + '.jpg')
    name_max = os.pathconf('/', 'PC_NAME_MAX')
    test_filename = truncate_name(long_filename)
    assert len(test_filename) == name_max + len(DIR_PATH)
