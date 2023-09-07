import datetime

def get_current_datetime():
    now = datetime.datetime.now()
    return now

def create_datetime(var, format_str=None):
    """
    support formations inlcuding:
    (1) list: [year, month, day ]
    (2) str, will need to specify format_str:
        example:
            1) var = "Friday the 13th, Oct, 1989", format_str = "%A the %dth, %b, %Y"
            2) var = "07/03/90", format_str = "%m/%d/%y"

    """
    if isinstance(var, list):
        year, month, day = var
        datetime_ = datetime.datetime(year, month, day)
        return datetime_
    
    if isinstance(var, str):
        datetime_ = datetime.datetime.strptime(var, format_str)

        

def convert_datetime_str_format(org_text, org_format, new_format):
    datetime_ = datetime.datetime.strptime(org_text, org_format)
    new_text = datetime_.strftime(new_format)
    return new_text


def get_year(datetime_):
    return datetime_.year

def get_month(datetime_):
    return datetime_.month

def get_day(datetime_):
    return datetime_.day

