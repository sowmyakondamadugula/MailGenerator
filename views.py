from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import UserLogin
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
#from google.cloud import translate_v2 as translate
from googletrans import Translator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def mainpage_view(request):
    return render(request, 'mainpage.html')  # make sure this file is inside the templates folder

# Create your views here.
def about(request):
    return HttpResponse("this is about page")
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")


def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        user_name=request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request,'index.html',{'message':'passwords do not match!please try again'})
            

        # Check if user already exists
        if UserLogin.objects.filter(email=email).exists():
            return render(request,'index.html',{'message':'user already exist! please login'})
            
        
        # Save new user
        user = UserLogin(email=email, password=password,user_name=user_name)
        user.save()
        return render(request,'index.html',{'message':"Registration successful. You can now log in."})
        
    else:
        return render(request,'index.html',{'message':"Invalid request method."})


        
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

def register_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'index.html', {'message': 'Passwords do not match! Please try again.'})

        # Check if user already exists
        if UserLogin.objects.filter(email=email).exists():
            return render(request, 'index.html', {'message': 'User already exists! Please log in.'})

        # Hash the password before saving
        user = UserLogin(email=email, password=make_password(password), user_name=user_name)
        user.save()

        return render(request, 'index.html', {'message': "Registration successful. You can now log in."})

    return render(request, 'index.html', {'message': "Invalid request method."})



def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        try:
            # Try to fetch the user
            user = UserLogin.objects.get(email=email, password=password)
            return render(request, 'index.html', {'message': f'Welcome, {user.user_name}!'})
            print(user.user_name)
        except UserLogin.DoesNotExist:
            return HttpResponse("Invalid email or password.")
    else:
        return HttpResponse("Invalid request method.")
def mainpage(request):
    return render(request,'mainpage.html')



@csrf_exempt
# views.py


@csrf_exempt
 
@csrf_exempt
def translate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        body = data.get('body', '')
        lang = data.get('lang', 'en')

        translator= Translator()#translate.Client()

        # Only translate non-empty strings
        translated_body = translator.translate(body, src=lang, dest='en').text if body else ''
        translated_to = translator.translate(data.get('to', ''), src=lang, dest='en').text if data.get('to', '') else ''
        translated_subject = translator.translate(data.get('subject', ''), src=lang, dest='en').text if data.get('subject', '') else ''

        return JsonResponse({
            'to': translated_to,
            'subject': translated_subject,
            'body': translated_body
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

from django.core.mail import send_mail


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to = data.get('to')
        subject = data.get('subject', 'No Subject')
        body = data.get('body', '')

        if not to:
            return JsonResponse({'error': 'Recipient email is required.'}, status=400)

        try:
            send_mail(
                subject,
                body,
                'your_email@gmail.com',  # From email
                [to],                    # Recipient list
                fail_silently=False,
            )
            return JsonResponse({'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
