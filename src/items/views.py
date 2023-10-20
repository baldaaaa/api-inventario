
from django.shortcuts import render, redirect
from .models import Carpeta, Item
from .forms import FolderForm, FileForm

def create_folder(request, parent_folder_id=None):
    parent_folder = Folder.objects.get(id=parent_folder_id) if parent_folder_id else None
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent_folder = parent_folder
            folder.save()
            return redirect('directory')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

def create_file(request, folder_id):
    folder = Folder.objects.get(id=folder_id)
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder
            file.save()
            return redirect('directory')
    else:
        form = FileForm()
    return render(request, 'create_file.html', {'form': form, 'folder': folder})

def directory(request):
    folders = Folder.objects.all()
    return render(request, 'directory.html', {'folders': folders})
