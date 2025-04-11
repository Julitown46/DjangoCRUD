from pickletools import read_decimalnl_long

from django.http import Http404
from django.shortcuts import render

from .models import Score
from .forms import ScoreForm

# Create your views here.
def index(request):
    context = {}
    form = ScoreForm()
    scores = Score.objects.all()
    context['scores'] = scores
    context['title'] = "Home Page"
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST.get('save')
            if not pk:
                form = ScoreForm(request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score)
            form.save()
            form = ScoreForm()
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Score.objects.get(id=pk)
            score.delete()
        elif 'edit' in request.POST:
            pk = request.POST.get('edit')
            score = Score.objects.get(id=pk)
            form = ScoreForm(instance=score)

    context['form'] = form
    return render(request, 'index.html', context)

def about(request):
    context = {}
    context['title'] = "About Page"
    return render(request, 'about.html', context)