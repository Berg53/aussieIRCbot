from datetime import datetime

from mock import patch

from src.modules.time import Time, ERROR_NOT_FOUND, OUTPUT_FORMAT

inputs = ['London', 'Perth', 'Sydney', 'perth', 'NZ', 'New York']

EXPECTED_OUTPUT = 'Australia/Perth:  7:52AM AWST (+0800) Jan 04, 2019'

class DTMock(datetime):
    """
    Python's bullshit mocking can't patch C stuff at runtime
    """
    def now(tz):
        return datetime(year=2019, month=1, day=4, hour=7, minute=52, tzinfo=tz)


@patch('src.modules.time.datetime', DTMock)
def test_time():
    t = Time()
    result = t.run('perth')
    assert result.success == EXPECTED_OUTPUT


# def test_location_case_insensitive():
#     t = Time()
#     result = t.run('perth')
#     assert result.success == 'perth'
#
#
# def test_location_handles_whitespace():
#     t = Time()
#     result = t.run('    perth   ')
#     assert result.success == 'perth'


def test_format_time():
    city = 'NZ'
    date = datetime(year=2019, month=1, day=4, hour=6, minute=52)
    expected = OUTPUT_FORMAT.format(city, ' 6:52AM  () Jan 04, 2019')
    t = Time()
    assert t._format_time(city, date) == expected


def test_sad_path():
    bad_tz = 'not-timezone'
    t = Time()
    t.run(bad_tz)
    assert t.errors == [ERROR_NOT_FOUND.format(bad_tz)]


def test_empty_string():
    t = Time()
    t.run('')
    assert t.errors == [ERROR_NOT_FOUND.format('')]

