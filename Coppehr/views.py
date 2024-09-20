from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from datetime import date

from .forms import UserLoginForm
from .models import Event, Resource, PostStatus, PostCategory, HealthTip
from .utils import (get_announcements, get_home_page_events, get_events,
                    get_upcoming_events, get_resources, get_calendar_events, get_health_tips)

MAX_EVENTS_PER_PAGE = 3
MAX_RESOURCES_PER_PAGE = 6
LATEST_RESOURCES_COUNT = 3
CALENDAR_BASE_URL = 'https://calendar.google.com/calendar/u/0/r/day/'


def user_login(request):
    errors = None
    form = UserLoginForm()
    next_page = request.GET.get('next', 'coppehr:home')
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_page)
            else:
                errors = "Your password and username don't match.\nPlease try again."
    return render(request, 'coppehr/pages/login.html', {'form': form, 'errors': errors})


@login_required(login_url='coppehr:login')
def user_logout(request):
    logout(request)
    return redirect('coppehr:login')


@login_required(login_url='coppehr:login')
def home(request):
    health_tips = get_health_tips()
    health_f, health_o = get_home_page_events(PostCategory.HEALTH)
    friendship_f, friendship_o = get_home_page_events(PostCategory.FRIENDSHIP)
    support_f, support_o = get_home_page_events(PostCategory.SUPPORT)
    return render(request, 'coppehr/pages/home.html', {
        'health_f': health_f,
        'health_o': health_o,
        'friendship_f': friendship_f,
        'friendship_o': friendship_o,
        'support_f': support_f,
        'support_o': support_o,
        'health_tips': health_tips
    })


@login_required(login_url='coppehr:login')
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.calendar_url = CALENDAR_BASE_URL + event.date.strftime("%Y/%-m/%-d")
    return render(request, 'coppehr/pages/events/detail.html', {'event': event})


@login_required(login_url='coppehr:login')
def resource_detail(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    return render(request, 'coppehr/pages/resources/detail.html', {'resource': resource})


@login_required(login_url='coppehr:login')
def healthtips_detail(request, healthtips_id):
    healthtips = get_object_or_404(HealthTip, pk=healthtips_id)
    return render(request, 'coppehr/pages/healthtips/detail.html', {'healthtips': healthtips})


@login_required(login_url='coppehr:login')
def saved_resources(request):
    return render(request, 'coppehr/pages/resources/saved.html')


@login_required(login_url='coppehr:login')
def calendar(request):
    weeks, items = get_calendar_events()
    return render(request, 'coppehr/pages/calendars/calendar.html', {'items': items})


@login_required(login_url='coppehr:login')
def archives(request):
    return render(request, 'coppehr/pages/archives/archives.html')


@login_required(login_url='coppehr:login')
def about(request):
    return render(request, 'coppehr/pages/about.html')


@login_required(login_url='coppehr:login')
def health_events(request):
    announcements_h = get_announcements(PostCategory.HEALTH)
    upcoming_e = get_upcoming_events(PostCategory.HEALTH)
    events = get_events(PostCategory.HEALTH)
    paginator = Paginator(events, MAX_EVENTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    health_e = paginator.page(page_number)
    return render(request, 'coppehr/pages/events/health.html', {
        'announcements_h': announcements_h,
        'health_e': health_e,
        'upcoming_e': upcoming_e})


@login_required(login_url='coppehr:login')
def health_resources(request):
    resources = get_resources(PostCategory.HEALTH).filter(status=PostStatus.PUBLISHED)
    health_f = resources.order_by('?').first()
    latest_r = list(resources.order_by('-release_date')[:LATEST_RESOURCES_COUNT])
    paginator = Paginator(resources, MAX_RESOURCES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    health_r = paginator.page(page_number)
    return render(request, 'coppehr/pages/resources/health_resource.html', {
        'health_f': health_f,
        'health_r': health_r,
        'latest_r': latest_r
    })


@login_required(login_url='coppehr:login')
def friendship_events(request):
    announcements_f = get_announcements(PostCategory.FRIENDSHIP)
    upcoming_e = get_upcoming_events(PostCategory.FRIENDSHIP)
    events = get_events(PostCategory.FRIENDSHIP)
    paginator = Paginator(events, MAX_EVENTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    friendship_e = paginator.page(page_number)
    return render(request, 'coppehr/pages/events/friendship.html', {
        'announcements_f': announcements_f,
        'friendship_e': friendship_e,
        'upcoming_e': upcoming_e})


@login_required(login_url='coppehr:login')
def friendship_resources(request):
    resources = get_resources(PostCategory.FRIENDSHIP).filter(status=PostStatus.PUBLISHED)
    friendship_f = resources.order_by('?').first()
    latest_r = list(resources.order_by('-release_date')[:LATEST_RESOURCES_COUNT])
    paginator = Paginator(resources, MAX_RESOURCES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    friendship_r = paginator.page(page_number)
    return render(request, 'coppehr/pages/resources/friendship_resource.html', {
        'friendship_f': friendship_f,
        'friendship_r': friendship_r,
        'latest_r': latest_r
    })


@login_required(login_url='coppehr:login')
def support_events(request):
    announcements_s = get_announcements(PostCategory.SUPPORT)
    upcoming_e = get_upcoming_events(PostCategory.SUPPORT)
    events = get_events(PostCategory.SUPPORT)
    paginator = Paginator(events, MAX_EVENTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    support_e = paginator.page(page_number)
    return render(request, 'coppehr/pages/events/support.html', {
        'announcements_s': announcements_s,
        'support_e': support_e,
        'upcoming_e': upcoming_e})


@login_required(login_url='coppehr:login')
def support_resources(request):
    resources = get_resources(PostCategory.SUPPORT)
    support_f = resources.order_by('?').first()
    latest_r = list(resources.order_by('-release_date')[:LATEST_RESOURCES_COUNT])
    paginator = Paginator(resources, MAX_RESOURCES_PER_PAGE)
    page_number = request.GET.get('page', 1)
    support_r = paginator.page(page_number)
    return render(request, 'coppehr/pages/resources/support_resource.html', {
        'support_f': support_f,
        'support_r': support_r,
        'latest_r': latest_r
    })
