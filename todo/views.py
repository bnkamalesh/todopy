from todo.models import Todo
from django.template import Context, loader
from django.http import HttpResponse

# Create your views here.
def index(request):
	t = loader.get_template('index.html')
	c = Context({
	})
	return HttpResponse(t.render(c))
	
def home(request):
	# no one is logged in
	if request.user.is_authenticated() == False:
		return HttpResponse('You must be logged in <a href="accounts/login">log in</a>')
	
	t = loader.get_template('home.html')
	c = Context({
	})
	return HttpResponse(t.render(c))
	
def ajax(request):
	# no one is logged in
	if request.user.is_authenticated() == False:
		return HttpResponse('You must be logged in <a href="accounts/login">log in</a>')

	# delete a todo
	if request.GET.has_key('delete_id'):
		Todo.objects.get(id=request.GET.get('delete_id')).delete()
		
	# change the status of a todo
	if request.GET.has_key('change_status'):
		item = Todo.objects.get(id=request.GET.get('change_status'))
		item.done = True
		item.save()
	
	# post a new todo
	if request.GET.has_key('title') and request.GET.has_key('description'):
		new_item = Todo(title=request.GET.get('title'), description=request.GET.get('description'), done=False, user=request.user)
		new_item.save()

	# render todo list
	todo_list = Todo.objects.filter(user=request.user.id).order_by('done')

	t = loader.get_template('list.html')
	c = Context({
		'todo_list': todo_list
	})

	return HttpResponse(t.render(c))
