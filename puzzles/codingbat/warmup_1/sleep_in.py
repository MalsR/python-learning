# The parameter weekday is True if it is a weekday,
# and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


class SleepIn:

    def sleep_in(self, weekday, vacation):
        if weekday is False or vacation:
            return True
        else:
            return False
