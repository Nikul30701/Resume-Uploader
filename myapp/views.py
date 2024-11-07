from django.shortcuts import render, redirect
from .form import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self,request):
        form = ResumeForm
        candidates = Resume.objects.all()
        return render(request, 'home.html',
                      {'candidates':candidates, 'form':form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')