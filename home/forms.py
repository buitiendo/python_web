from django import forms
import re #thư viện dùng để kiểm tra xem username đã tồn tại chưa có gì đặc biệt không
from django.contrib.auth.models import User #lấy thư viện User ra
from django.core.exceptions import ObjectDoesNotExist #thư viện lấy ra lỗi
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    def clean_password2(self):
      if 'password1' in self.cleaned_data:
          password1 = self.cleaned_data['password1'] #lấy dữ liệu từ cleaned_data
          password2 = self.cleaned_data['password2']
          if password1 == password2 and password1: #and password1 tránh trường hợp người dùng chỉ gõ dấu cách liên tục(dấu cách như là không nhập)
              return password2
      raise forms.ValidationError('Mật khẩu không hợp lệ') #Nếu không trả về lỗi raise kiểu forms.ValidationError với nội dung mật khẩu không hợp lệ
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username): # r'^\w+$' : kiểm tra toàn bộ chuỗi, tất cả các ký tự username là ký tự thường =>(not) có ký tự đặc biệt
            raise forms.ValidationError('Tên tài khoản có ký tự đặc biệt')
        try: # Kiểm tra xem username này đã bị trùng chưa?
            User.objects.get(username=username)
        except ObjectDoesNotExist: #nếu trả lỗi này chứng tỏ username chưa tồn tại=> trả về username
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại") #ngược lại tức là có tồn tại username rồi và trả về lỗi
    def save(self): #hàm tạo ra tài khoản
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
