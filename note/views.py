from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from note.models import Note


def home(request):
    all_notes = Note.objects.all()
    return render(request, 'home.html', {'notes': all_notes})


def add(request):
    return render(request, 'add.html')


def save_note(request):
    note_content = str.strip(request.POST['note_content'])
    note_id = request.POST['note_id']
    if 3 < len(note_content) < 1000:
        try:
            if note_id:
                note = Note.objects.get(pk=note_id)
            else:
                note = Note()
            note.note = note_content
            note.save()
            return HttpResponseRedirect(reverse('home'))
        except:
            return render(request, 'add.html', {'error_message': 'Internal server error', 'note_content': note_content})
    else:
        return render(request, 'add.html', {'error_message': 'Note length is invalid', 'note_content': note_content})


def edit(request, note_id):
    edit_note = Note.objects.get(pk=note_id)
    print(edit_note.note)
    return render(request, 'add.html', {'note_content': edit_note.note, 'note_id': note_id})


def delete(request, note_id):
    del_note = Note.objects.get(pk=note_id)
    try:
        del_note.delete()
    except:
        pass
    all_notes = Note.objects.all()
    return render(request, 'home.html', {'notes': all_notes})
