from django.shortcuts import render
from .forms import LinkModelForm
from .models import Link
from django.shortcuts import redirect


def index(request):
    form = LinkModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        url = obj.short_url
        context = {'url': url, 'form': form}
        return render(request, 'main/index.html', context)
    context = {'form': form}
    return render(request, 'main/index.html', context)


def redirection(request, num):
    short_url = 'shorter/' + str(num) + '/'
    link = Link.objects.get(short_url=short_url)
    return redirect(link.full_url)

