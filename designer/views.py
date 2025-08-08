
from django.shortcuts import render, redirect
from .forms import CustomizationForm

def editor(request):
    if request.method == 'POST':
        form = CustomizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editor')
    else:
        form = CustomizationForm()
    return render(request, 'designer/editor.html', {'form': form})
