from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model # 사용자가 데이터 베이스 안에 있는 지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

# 회원 가입을 위한 함수
def sign_up_view(request):
    if request.method == "GET":  # url로 온 방식이 GET 방식이면 보여주겠다.
        user = request.user.is_authenticated
        if user:  # user가 존재한다면!
            return redirect("/")
        else:  # 존재하지 않는 다면
            return render(request, 'user/signup.html')

    elif request.method == 'POST':  # 요청이 들어오는 곳!
        # db에 추가되는 기능들이 있으면 좋을 듯.
        # get("이 정보가 없으면", None) None 반환.
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:  # 사용자가 존재하는 경우
                return render(request, 'user/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:  # 존재 X
                UserModel.objects.create_user(username=username, password=password, email=email)
                return redirect('/sign-in')

# 회원가입이 다 되었을 때만 확인 가능
# 로그인 기능
def sign_in_view(request):
    if request.method == 'POST': # 로그인 요청임~
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username= username, password=password) #인증기능 모듈을 먼저

        if me is not None: # 1. 사용자가 있다는 것임
            # request.session['user'] = me.username # 있다면 로그인 세션을 유지해주는 것임~
            auth.login(request, me) # 2. 그럼 사용자 정보를 넣어줘라
            return redirect("/")
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        user= request.user.is_authenticated

        if user:
            return redirect("/")
        else:
            return render(request, 'user/signin.html')

@login_required #사용자가 로그인 되어 있어야 사용가능하다는 것을 알려주는 것이다!
def logout(request):
    auth.logout(request) # 장고 기능 사용하지 않는 다면 session을 통해서 체크해야 된다 하지만 그렇게 하지 않아도 된다고 함
    return redirect("/")

# should move to  another position
def home(request):
    return render(request,'index.html')

# cctv`s function;
def cctv(request):
    return render(request, 'cctv/cctv.html')

