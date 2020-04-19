from datetime import datetime


# filter country name inputs
def filter_country_name(country_name):
    if country_name.islower() == True:
        country_name = country_name.capitalize()
    if len(country_name) < 4:
        country_name = country_name.upper()
    return country_name

# filter date inputs
def filter_date(year, month, day): 
    return f'{year}-{month}-{day}'

# get today date
def get_today_date():
    return datetime.today().date()