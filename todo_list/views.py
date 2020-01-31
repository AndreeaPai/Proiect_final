from django.shortcuts import render, redirect
from .models import Todo
from .forms import ListForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'home.html', {'todo_items': todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    print(request.POST)
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date = current_date, text = content)
    #print(created_obj)
    length_of_todos = Todo.objects.all().count()
    #print(length_of_todos)
    return HttpResponseRedirect("/") #redirectionez la homepage

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get( id = todo_id ).delete()
    messages.success(request, ('Item a fost sters!'))
    return HttpResponseRedirect("/")

def edit(request, todo_id):
    if request.method == 'POST':
        item = Todo.objects.get(id=todo_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item a fost editat'))
            return redirect('home')
            #return HttpResponseRedirect('/')
            #return render(request, 'home.html',{'form': form})

# Daca este un post request si form valid atunci redirectioneaza la pagina
# Daca este un post request si form invalid atunci render a bound form


    else:
        item = Todo.objects.get(id = todo_id)
        return render(request, 'edit.html' , {'item': item}) #view returneaza render





