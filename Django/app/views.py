import base64
import json
from django import views
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import *
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg import openapi
from .forms import *
from rest_framework_jwt.settings import api_settings


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
import re
from django.http import QueryDict
from django.http import JsonResponse

from DjangoService.OrcCaptchaService import OrcCaptcha

def process_uploaded_data(data_string):
    # Dùng biểu thức chính quy để tìm kiếm dữ liệu nằm trong chuỗi
    pattern = r"------WebKitFormBoundary.*?Content-Disposition: form-data; name=\"(.*?)\"\r\n\r\n(.*?)\r\n"
    matches = re.findall(pattern, data_string, re.DOTALL)
    # Chuyển đổi thành một từ điển
    data_dict = {name: value for name, value in matches}
    return data_dict

def test_fetch(request):
    uploaded_file = request.FILES['file']  
    base64_data = base64.b64encode(uploaded_file.read()).decode('utf-8')
    engine = request.POST["rdoSelected"]
    if str(uploaded_file).endswith(".png"):
       base64String = f"data:image/png;base64,{base64_data}"
    if str(uploaded_file).endswith(".jpg"):
       base64String = f"data:image/jpg;base64,{base64_data}"
    if str(uploaded_file).endswith(".jpeg"):
       base64String = f"data:image/jpeg;base64,{base64_data}"
    
    result = OrcCaptcha.ImgtoText(base64=base64String, engine=engine)
    print("Result: " + result)
    return JsonResponse({'message': result})


def get_messages(request):
    messages = ["Message 1", "Message 2", "Message 3"]  # Thay thế bằng logic lấy danh sách tin nhắn thực tế
    return JsonResponse({'messages': messages})


def get_data(request):
    data = {
        'message': 'This is the data you requested!',
        'value': 42
    }
    return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    try:
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user = valid_data['user_id']
        customer = Customer.objects.get(user=user)
    except ValidationError as v:
        print("validation error")
        

    serializer = ProfileSerializer(customer)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])  # policy decorator
@renderer_classes([JSONRenderer])       # policy decorator
def check_authenticated(request):
    print(request.META["HTTP_AUTHORIZATION"])
    
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    try:
        valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        user = valid_data['user_id']
        customer = Customer.objects.get(user=user)
    except ValidationError as v:
        print("validation error")

    content = {"auth":"Authenticated", "username": customer.user.username}
    return Response(content)

def redirectPage(request):
    return redirect("/home")

def is_authenticated(request):
    if request.user.is_authenticated:
        return True
    else:
        redirect("/login")
        return False
    
def custom_404(request, exception):
    return render(request, 'app/error/404.html', status=404)

def custom_500(request, exception):
    return render(request, 'app/error/404.html', status=404)

def signinView(request):
    
    if request.method == "GET":
        form = SigninForm(request.GET)
        context = {"form": form}
        return render(request, "app/auth/signin.html", context)
    
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            unname = form.cleaned_data.get("web_username")
            pwd = form.cleaned_data.get("web_password")
            captcha = form.cleaned_data.get("captcha")
            
            user = authenticate(request, username=unname, password=pwd)
   
            if user is not None:
                login(request, user)
                
                refresh = RefreshToken.for_user(user)
                accessToken = refresh.access_token
                
                customer = Customer.objects.get(user=user)
                customer.accessToken = accessToken
                customer.refreshToken = str(refresh)
                customer.save()
                return redirect('/home')
            else:
                messages = ['Username or Password is incorrect!']
                print(messages)
                context = {'messages': messages, "form": form}
                return render(request, "app/auth/signin.html", context)
        else:
            messages = [message for messages in form.errors.values() for message in messages]
            print(messages)
            context = {'messages': messages, "form": form}
            return render(request, "app/auth/signin.html", context)


def signupView(request):
    
    if request.method == 'GET':
        form = SigninForm(request.GET)
        context = {"form": form}
        return render(request, "app/auth/signup.html", context)
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            unname = request.POST.get('web_username')
            email = request.POST.get('web_email')
            pwd1 = request.POST.get('web_password')
            pwd2 = request.POST.get('web_repassword')
            user = User.objects.create_user(unname, email, pwd1)
            user.save()
            context = {"messages": ["Account is successed create"], "form": form}
            return render(request, "app/home/home.html", context)
        else:
            messages = form.errors.values()
            context = {"messages": messages, "form": form}
            return render(request, "app/auth/signup.html", context, )


def homeView(request):
    if is_authenticated(request=request):
        user = request.user
        customer = Customer.objects.get_or_create(user=request.user)
        listProduct = Product.objects.all()
        context = {"products": listProduct, "user": Customer.objects.get(user=request.user), "messages":["Login Successful"]}
        return render(request, "app/home/home.html", context)
    else:
        return redirect('signin')


def captchaView(request):
    if is_authenticated(request=request):
        user = request.user
        context = {}
        return render(request, "app/captcha/captcha.html", context)
    else:
        return redirect('signin')
    
def documentView(request):
    if is_authenticated(request=request):
        user = request.user
        customer = Customer.objects.get(user=user)
    
        context = {"accessToken": customer.accessToken, "refreshToken": customer.refreshToken}
        return render(request, "app/document/document.html", context)
    else:
        return redirect('signin')
    
    
def logoutView(request):
    logout(request)
    return redirect("home")


@api_view(['GET'])
@swagger_auto_schema(responses={200: ProductSerializer(many=True)})
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Create a new book",
    request_body=ProductSerializer,
    responses={201: ProductSerializer},
    manual_parameters=[
        openapi.Parameter(
            'custom_param',  # Thay 'custom_param' bằng tên tham số của bạn
            openapi.IN_QUERY,
            description='A custom parameter description',
            type=openapi.TYPE_STRING,
            default='sample_value',  # Thêm giá trị mẫu cho tham số
        ),
    ]
)
def create_book(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






