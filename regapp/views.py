from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        e_mail = request.POST.get('email', '')
        password_1 = request.POST.get('password', '')
        password_2 = request.POST.get('confirm_password', '')

        # Error message to display in the form
        error_message = None

        if password_1 != password_2:
            error_message = "Passwords do not match."
        elif User.objects.filter(username=user_name).exists():
            error_message = "Username is already taken."
        elif User.objects.filter(email=e_mail).exists():
            error_message = "Email is already registered."
        else:
            # Create user if no errors
            user = User.objects.create_user(username=user_name, email=e_mail, password=password_1)
            user.save()
            print("User created")
            return redirect('/')  # Redirect to homepage or any other page after successful signup

        # Pass the error message to the index.html template
        context = {
            'error_message': error_message,
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
# def signup(request):

#     if request.method=='POST':
#         user_name = request.POST['username']
#         e_mail = request.POST['email']
#         password_1 = request.POST['password']
#         password_2 = request.POST['confirm_password']

#         print("Signup form submitted")
#         print(f"Username: {user_name}, Email: {e_mail}")

#         if password_1==password_2:
#             if User.objects.filter(username=user_name).exists():
#                 # messages.error(request, "Username is already taken.")
#                 messages.info(request,"Username taken")
#                 return redirect('/')
#             elif User.objects.filter(email=e_mail).exists():
#                 # messages.error(request, "Email is already in use.")
#                 messages.info(request,"Email taken")
#                 return redirect('/')
#             else:
#                 user = User.objects.create_user(username=user_name, email=e_mail, password=password_1)
#                 user.save()
#                 print("user created")
#                 # messages.success(request, "Account created successfully! Please log in.")
#                 return redirect('/')  # Redirect to login form after success
                
#         else:
#             messages.info(request,"Passwords aren't matching")
#             return redirect('/')


        
        
#     else:
#         return render(request,'index.html')

def login(request):
    if request.method=='POST':
        u_name=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=u_name,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request, 'success.html', {'message': 'Logged in successfully'})
            # return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'error.html', {'message': 'Invalid_credentials'})
            # return redirect('login')
        
    else:
        return render(request,'index.html')



# def login(request):
#     return render(request, 'index.html')

# def signup(request):
#     return render(request, 'index.html')


