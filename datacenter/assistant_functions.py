SECONDS_ON_DAY = 86400
SECONDS_ON_HOUR = 3600
SECONDS_ON_MINUTE = 60


def format_duration(duration):
    '''Returning duration in string format'''
    total_sec = duration.total_seconds()
    days = total_sec // SECONDS_ON_DAY
    hours = int((total_sec - days * SECONDS_ON_DAY) // SECONDS_ON_HOUR)
    minutes = int((total_sec - days * SECONDS_ON_DAY - hours * SECONDS_ON_HOUR) // SECONDS_ON_MINUTE)
    seconds = int(total_sec - days * SECONDS_ON_DAY - hours * SECONDS_ON_HOUR - minutes * SECONDS_ON_MINUTE)
    return f'{hours}:{minutes}:{seconds}'
