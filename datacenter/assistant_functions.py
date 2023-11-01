def format_duration(duration):
    '''Returning duration in string format'''
    total_sec = duration.total_seconds()
    seconds_on_day = 86400
    seconds_on_hours = 3600
    seconds_on_minutes = 60
    days = total_sec // seconds_on_day
    hours = int((total_sec - days * seconds_on_day) // seconds_on_hours)
    minutes = int((total_sec - days * seconds_on_day - hours * seconds_on_hours) // seconds_on_minutes)
    seconds = int(total_sec - days * seconds_on_day - hours * seconds_on_hours - minutes * seconds_on_minutes)
    return f'{hours}:{minutes}:{seconds}'
