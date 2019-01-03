from datetime import datetime

from src.modules.time import Time, ERROR_NOT_FOUND, OUTPUT_FORMAT

inputs = ['London', 'Perth', 'Sydney', 'perth']


def test_time():
    t = Time()
    result = t.run('Perth')
    assert result.success == 'perth'


def test_location_case_insensitive():
    t = Time()
    result = t.run('Perth')
    assert result.success == 'perth'


def test_location_handles_whitespace():
    t = Time()
    result = t.run('    perth   ')
    assert result.success == 'perth'


def test_format_time():
    city = 'Perth'
    date = datetime(year=2019, month=1, day=4, hour=6, minute=52)
    expected = OUTPUT_FORMAT.format(city, ' 6:52AM  () Jan 04, 2019')
    t = Time()
    assert t._format_time(city, date) == expected


def test_sad_path():
    bad_tz = 'not-timezone'
    t = Time()
    t.run(bad_tz)
    assert t.errors == [ERROR_NOT_FOUND.format(bad_tz)]
