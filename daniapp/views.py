from django.shortcuts import render, redirect
from .models import *
from .form import *


# Create your views here.


def index(request):
    forums = Forums.objects.all()
    count = forums.count()
    discussions= []
    for i in forums:
        discussions.append(i.discussion_set.all())

    context = {'forums': forums,
               'count': count,
               'discussions': discussions}
    return render(request, 'index.html', context)

    def forumAdd(request):
        form = createForum()
        if request.method == 'POST':
            form = createForum(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'forumAdd.html', context)


    def discussionAdd(request):
        form = discussForm()
        if request.method == 'POST':
            form = discussForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form':form}
        return render(request, 'discussionAdd.html', context)

