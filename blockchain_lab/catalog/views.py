from django.shortcuts import render
from .forms import TableForm
from django.shortcuts import redirect

'''def index(request):
    return render(request, 'catalog/homePage.html')'''

def model_form_upload(request):
    if request.method == 'POST':
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TableForm()
    return render(request, 'catalog/homePage.html', {
        'form': form
    })