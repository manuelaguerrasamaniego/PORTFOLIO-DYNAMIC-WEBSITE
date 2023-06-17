from django.shortcuts import render, redirect
from django.contrib import messages
from portfolio.models import Contact, Blogs, Internship

# Create your views here.
def home(request):
    return render(request, 'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}

    return render(request, 'handleblog.html', context)


def about(request):
    return render(request, 'about.html')

def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request, "Please login to access this page")
        return redirect('/auth/login/')

    if request.method=="POST":

        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fcompany=request.POST.get('company')
        foffer=request.POST.get('offer')
        fstart=request.POST.get('start')
        fend=request.POST.get('end')

        query=Internship(name=fname, email=femail, company=fcompany,
                        offer=foffer, start=fstart, end=fend)
        query.save()
        messages.success(request, "Thank you for submiting your offer. I will get back to you soon!")
        return redirect('/internshipdetails')

    return render(request, 'intern.html')


def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,
                      phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request, "Thanks for reaching out. I will get back to you soon!")
        
        
        return redirect('/contact')

    return render(request, 'contact.html')