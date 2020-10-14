from django.shortcuts import render,HttpResponse

# Create your views here.
#form creation

def html_form(request):
    if request.method=="POST":
        firstname = request.POST.get('first name',None)
        lastname = request.POST.get('last name',None)
        email = request.POST.get('email',None)
        degree = request.POST.get('degree',None)
        education = request.POST.get('education',None)
        address = request.POST.get('address',None)
        x= User.objects.create_user( firstname=firstname,lastname=lastname,email=email,degree=degree,education=education,address=address)
        x.save()   
        print("data saved") 
    return render(request,'html_form.html')

#register data 

def save_data(request):
    return render(request,'save_data.html')

#cancel register

def cancel_data(request):
    return redirect('html_form.html')

