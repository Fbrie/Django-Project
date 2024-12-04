import urllib.request
import json
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
    """Renders the homepage with weather data fetched via OpenWeather API."""
    data = {}  # Initialize an empty dictionary to store weather data
    
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '287135a8d3e008251727bf82ed1c43dd'  # Replace with your actual API key
        
        try:
            # Fetch data from OpenWeather API
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            ).read()
            list_of_data = json.loads(source)

            # Parse weather data to pass to the template
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
                "temp": f"{list_of_data['main']['temp']} °C",
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": list_of_data['weather'][0]['icon'],
            }
        except Exception as e:
            # Handle cases where the API call fails
            messages.error(request, "Failed to fetch weather data. Please try again.")
            print(f"Error fetching weather data: {e}")  # For debugging purposes

    return render(request, "main/index.html", data)


def register(request):
    """Handles user registration with additional profile creation."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user and hash password
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save profile and link it to the user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')  # Redirect to login page
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, "main/register.html", {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def members_list(request):
    """Displays a list of all registered users."""
    users = User.objects.all()  # Fetch all users
    return render(request, "main/members_list.html", {'users': users})


def user_detail(request, user_id):
    """Displays detailed information for a specific user."""
    user = get_object_or_404(User, id=user_id)
    return render(request, "main/user_detail.html", {'user': user})


def test_view(request):
    """Renders a test template."""
    return render(request, "main/test_template.html")



 


