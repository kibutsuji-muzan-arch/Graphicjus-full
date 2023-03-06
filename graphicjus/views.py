from django.shortcuts import render
from django.views import View
from .models import Contact, Services
from pyisemail import is_email as email_validator
# Create your views here.
class home(View):

    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        services = request.POST['services']
        
        if email_validator(address=email, check_dns=True):
            req = Contact.objects.create(name=name,email=email)
            for x in services.rsplit(","):
                y=Services.objects.get(name=x)
                req.service.add(y)
            req.save()
        print(f"{name} {email} {services}")
        return render(request, 'index.html')