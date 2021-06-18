from django.shortcuts import render
from django.views.generic import TemplateView

class MainPage(TemplateView):
    template_name = 'home.html'

def mainpage(request):

    if request.POST['choices'] == 'checkbox':
        String = request.POST['string']
        a=String.splitlines()
        return render(request, "checkbox.html", {"string": a, "input":String})


    elif request.POST['choices'] == 'dropdown':
        String = request.POST['string']
        a = String.splitlines()
        return render(request, "dropdown.html", {"string": a, "input":String})


    elif request.POST['choices'] == 'radio-button':
        String = request.POST['string']
        a = String.splitlines()
        return render(request, "radio.html", {"string": a, "input":String})


    elif request.POST['choices'] == 'textbox':
        String = request.POST['string']
        a = String.splitlines()
        return render(request, "textbox.html", {"string": a, "input":String})






