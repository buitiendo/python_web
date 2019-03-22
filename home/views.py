from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

def index(request):
    return render(request,'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST': #khi method POST là lúc ng dùng click nút đăng ký,
        form = RegistrationForm(request.POST) #gọi dữ liệu ng dùng nhập vào form
        if form.is_valid(): # khi form.is_valid nó sẽ tự động gọi các hàm có phương thức clean_ => chứng tỏ các phương thức kiểm tra dữ liệu người dùng nhập vào hợp lệ
            form.save()
            return HttpResponseRedirect('/') # tạo tài khoản thành công thì redirect nguời dùng về trang chủ
    return render(request, 'pages/register.html', {'form': form})
