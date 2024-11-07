from django.shortcuts import render
from .form import ResumeForm
from .models import Resume
from django.views import View

class HomeView(View):
    def get(self,request):
        form = ResumeForm
        return render(request, 'home.html', {'form':form})

