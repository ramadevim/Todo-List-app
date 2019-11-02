from django.shortcuts import render,redirect

# Create your views here.
from .models import Todo
from justtodo.forms import TodoForm
from django.views.decorators.http import require_POST

def index(request):
	todo_list=Todo.objects.order_by('id')
	
	form=TodoForm()

	context={'todo_list':todo_list,'form':form}
	
	return render(request,'todo/index.html',context)

@require_POST
def addTodo(request):
	form = TodoForm(request.POST)

	# print(request.POST['text'])

	if form.is_valid():
		new_todo = Todo(text=request.POST['text'])
		new_todo.save()

	return redirect('justtodo:index')

def completetodo(request,todo_id):
	todo=Todo.objects.get(pk=todo_id)
	todo.complete=True
	todo.save()

	return redirect('justtodo:index')

def deletecomplete(request):
	Todo.objects.filter(complete__exact=True).delete()

	return redirect('justtodo:index')

def deleteall(request):
	Todo.objects.all().delete()

	return redirect('justtodo:index')
