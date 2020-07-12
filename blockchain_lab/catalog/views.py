from django.shortcuts import render
from .forms import ProcurementForm
from django.shortcuts import redirect
from .models import Procurement

# in your template.html <form> tag must include enctype="multipart/form-data"

'''def index(request):
    return render(request, 'catalog/homePage.html')'''

def model_form_upload(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProcurementForm()
    return render(request, 'catalog/homePage.html', {
        'form': form
    })