from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import DesignForm
from .models import design


# Create your views here.
def home(request):
    dgn = design.objects.all()
    items = {
        'design': dgn
    }
    return render(request, 'index.html', items)


def detail(request, itemid):
    item_det = design.objects.get(id=itemid)
    return render(request, 'detail.html', {'itl': item_det})


def add_item(request):
    if request.method == "POST":
        nm = request.POST.get('name', )
        rt = request.POST.get('rate', )
        image = request.FILES['image']
        dgn = design(name=nm, rate=rt, image=image)
        dgn.save()

    return render(request, 'add.html')


def update(request, id):
    item = design.objects.get(id=id)
    form = DesignForm(request.POST or None, request.FILES, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'design': item})


def delete(request, id):
    if request.method == 'POST':
        item = design.objects.get(id=id)
        item.delete()
        return redirect('/')
    return render(request, 'delete.html')
