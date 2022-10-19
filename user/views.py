from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_logout(request):
    logout(request)
    return redirect('profile')
def profile(request):
    return render(request, './user/profile.html')


def user_login(request):
    username, message = '', ''
    if request.method == 'POST':
        if request.POST.get('login'):  # 按下登入按鈕
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 檢查帳號密碼是否為空
            if username == '' or password == '':
                message = '帳號跟密碼不能為空'
            else:
                # 檢查資料庫是否有該使用者
                # 匹配密碼進行登入
                user = authenticate(
                    request, username=username, password=password)
                if user is None:
                    if User.objects.filter(username=username):
                        message = '密碼有誤'
                    else:
                        message = '帳號有誤'
                else:
                    login(request, user)
                    message = '登入中'
                    return redirect('profile')
        elif request.POST.get('register'):
            return redirect('register')
    return render(request, './user/login.html', {'message': message, 'username': username})


# Create your views here.


def user_register(request):

    form = UserCreationForm()
    message = ''

    if request.method == 'GET':
        print('GET')
    elif request.method == 'POST':
        print('POST')
        print(request.POST)
        username = (request.POST.get('username'))
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) < 8:
            message = '密碼少於8個字元'

        elif password1 != password2:
            message = '兩次密碼不相同'
        else:
            if User.objects.filter(username=username).exists():
                message = '帳號重複'
            else:
                User.objects.create_user(
                    username=username, password=password1).save()
                message = ('註冊成功')
        # 註冊功能
        # 兩次密碼是否相同
        # 密碼不能少於8個字元
        # 使用者名稱不能重複
        # 進行註冊

    return render(request, './user/register.html', {'form': form, 'message': message})
