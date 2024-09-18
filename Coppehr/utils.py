from datetime import date, timedelta
from .models import Announcement, Event, Resource, PostStatus, PostCategory, HealthTip


def _get_date_for_monday_of_this_week():
    today = date.today()
    return today - timedelta(days=today.weekday())


def _format_release_date(date):
    # Format date as: October 15
    return date.strftime('%B %d')


def get_announcements():
    announcements = Announcement.objects \
        .filter(status=PostStatus.PUBLISHED) \
        .filter(release_date__lte=date.today()) \
        .filter(expiration_date__gte=date.today()) \
        .order_by('expiration_date')
    return announcements


def get_home_page_events(category):
    monday_this_week = _get_date_for_monday_of_this_week()
    events = Event.objects \
        .filter(category=category) \
        .filter(status=PostStatus.PUBLISHED) \
        .filter(release_date__gte=monday_this_week) \
        .filter(date__gte=date.today()) \
        .exclude(title__istartswith='This Week of') \
        .order_by('date')
    featured = None
    others = []
    if events.exists():
        featured = events.first()
        if events.count() > 1:
            others = events[1:4]
    return (featured, others)


def get_calendar_events():
    MAX_NUMBER_OF_WEEKS = 4
    EVENTS_PER_ROW = 3
    monday_this_week = _get_date_for_monday_of_this_week()
    weeks = [monday_this_week + timedelta(weeks=i)  # get the monday date of coming 4 weeks
             for i in range(0, MAX_NUMBER_OF_WEEKS)]
    items = []
    for w in weeks:
        rdate = _format_release_date(w)
        events = Event.objects \
            .filter(release_date=w) \
            .filter(status=PostStatus.PUBLISHED) \
            .order_by('date', 'time')
        groups = [events[i:i + EVENTS_PER_ROW]
                  for i in range(0, len(events), EVENTS_PER_ROW)]
        items.append({
            'date': rdate,
            'groups': groups
        })
    return weeks, items


def get_events(category):
    monday_this_week = _get_date_for_monday_of_this_week()
    events = Event.objects \
        .filter(category=category) \
        .filter(status=PostStatus.PUBLISHED) \
        .filter(release_date__gte=monday_this_week) \
        .order_by('date')
    return events


def get_upcoming_events(category):
    MIN_WEEKS_AHEAD = 1
    MAX_WEEKS_AHEAD = 10
    monday_this_week = _get_date_for_monday_of_this_week()
    events = Event.objects \
        .filter(category=category) \
        .filter(status=PostStatus.PUBLISHED) \
        .filter(release_date__gte=monday_this_week + timedelta(weeks=MIN_WEEKS_AHEAD)) \
        .filter(release_date__lte=monday_this_week + timedelta(weeks=MAX_WEEKS_AHEAD)) \
        .order_by('date')
    return events


def get_resources(category):
    resources = Resource.objects \
        .filter(category=category) \
        .filter(status=PostStatus.PUBLISHED) \
        .order_by('updated_on', 'release_date', 'created_on')
    return resources


def get_health_tips():
    health_tips = HealthTip.objects \
        .filter(status=PostStatus.PUBLISHED) \
        .filter(release_date__lte=date.today()) \
        .filter(expiration_date__gte=date.today()) \
        .order_by('expiration_date') \
        .first()
    return health_tips
