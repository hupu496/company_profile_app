from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Webdev,Mobdev,Cloud,UI_UX,Video_editing,CMS,HDR,Contact
from cmpy_profile.functions import handle_uploaded_file
from django.core.mail import send_mail

def Home(request):
    return render(request, 'company/home.html')
def Services(request):
    return render(request, 'company/services.html')
def About(request):
    return render(request, 'company/about.html')
def Contacts(request):
    if request.method == 'POST':
        contact = Contact(request.POST, request.FILES)
        name=request.POST.get('name')
        email=request.POST.get('email')
        description=request.POST.get('description')
        files=request.POST.get(handle_uploaded_file(request.FILES['file']))
        contverify=Contact(cont_name=name,cont_email=email,cont_desc=description,cont_file=files)
        contverify.save()
        msg="thanks for contacting the my compnay if any update or information regards your .I will inform you "
        send_mail(
            'jaish company',
            msg,
            '<jaishcompany@gmail.com>',
            [email],
            fail_silently=False
        )
        return redirect('Submission')
    return render(request, 'company/contact.html')
def Blog(request):
    return render(request, 'company/blog.html')

def submission(request):
    return render(request, 'company/submission.html')

def Webapp(request):
    webdev=Webdev.objects.all()
    n=len(webdev)
    params={'range':range(0,n), 'webdevs':webdev}
    return render(request, 'services/web_dev.html',params)

def Mobapp(request):
    mobdev= Mobdev.objects.all()
    n=len(mobdev)
    params={'range':range(0,n), 'mobdevs':mobdev}
    return render(request, 'services/mobile_dev.html',params)

def Cloud(request):
    cloud = Cloud.objects.all()
    n=len(cloud)
    params= {'range':range(0,n),'clouds':cloud}
    return render(request, 'services/Cloud.html',params)

def Ui_Ux(request):
    ui = UI_UX.objects.all()
    n=len(ui)
    params = {'range':range(0,n),'uis':ui}
    return render(request, 'services/Ui_Ux.html',params)

def Video_edit(request):
    video = Video_editing.objects.all()
    n=len(video)
    params = {'range':range(0,n),'videos':video}
    return render(request, 'services/video_edit.html',params)

def Cms(request):
    cms = CMS.objects.all()
    n=len(cms)
    params = {'range':range(0,n),'cmss':cms}
    return render(request, 'services/cms.html',params)

def Hdr(request):
    hdr = HDR.objects.all()
    n=len(hdr)
    params = {'range':range(0,n),'hdrs':hdr}
    return render(request, 'services/hdr.html',params)
