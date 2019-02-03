import logging
import time
from collections import defaultdict, namedtuple


__all__ = ["Occurrence", "Throttle", "DefaultThrottle", "DontThrottle"]

_LOGGER = logging.getLogger(__name__)


Occurrence = namedtuple("Occurrence", ("since", "times"))


class Throttle(object):
    def __init__(self, wait: int, threshold: int):
        """
        :param wait: Time in seconds between occurrences.
        :param threshold: Number of times occurrences can happen within the wait
                          period.
        """
        self._wait = int(wait)
        self._threshold = int(threshold)
        self._occurrences = defaultdict(lambda: Occurrence(int(time.time()), 0))

    @property
    def wait(self) -> int:
        return self._wait

    @property
    def threshold(self) -> int:
        return self._threshold

    def _key(self, *key_parts):
        _LOGGER.debug("_key({})".format(", ".join(key_parts)))
        return ":".join(key_parts)

    def _is_throttled(self, times):
        return times > self.threshold

    def is_throttled(self, *occurrence_key) -> bool:
        """
        Determines if occurrence has exceeded threshold within wait time and should be
        throttled.

        :param occurrence_key: key used to look up the occurrence.
        :return: Bool to indicate if the occurrence is over the threshold (True) or not
                (False).
        """
        occurrence_key = self._key(*occurrence_key)
        return self._is_throttled(self._occurrences[occurrence_key].times)

    def occurrence(self, *occurrence_key) -> bool:
        """
        Marks that an occurrence has happened.

        :param occurrence_key: key used to look up the occurrence.
        :return: Bool to indicate if the occurrence is over the threshold (True) or not
                (False).
        """
        occurrence_key = self._key(*occurrence_key)
        occurrence = self._occurrences[occurrence_key]
        times = occurrence.times
        now = int(time.time())

        if now - occurrence.since < self.wait:
            times += 1
        else:
            times = 0

        self._occurrences[occurrence_key] = Occurrence(now, times)

        return self._is_throttled(times)

    def reset(self):
        """
        Resets / clears all throttlers.
        """
        self._occurrences.clear()


class DefaultThrottle(Throttle):
    # Default threshold if none specified at init time.
    THRESHOLD = 2

    # Default wait if none specified at init time.
    WAIT = 5

    def __init__(self, wait: int = WAIT, threshold: int = THRESHOLD):
        """
        :param wait: Time in seconds between occurrences.  Defaults to WAIT.
        :param threshold: Number of times occurrences can happen within the wait
                          period.  Defaults to THRESHOLD.
        """
        super().__init__(wait, threshold)


class DontThrottle(DefaultThrottle):
    """
    A Throttler class which says it throttles but doesn't.
    """
    def __init__(self, *args, **kwargs):
        super().__init__()

    def occurrence(self, *occurrence_key):
        return False

    def is_throttled(self, *occurrence_key):
        return False
