from django.shortcuts import render
from todo.models import *
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse

# Create your views here.
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        # logged in
        login(request, user)
        context = {
            'status' : 1,
            'first_name' : user.first_name,
        }
        return JsonResponse(context)
    else:
        context = {
            'status' : 0,
            'message' : 'Invalid username or password'
        }
        return JsonResponse(context)

def user_logout(request):
    logout(request)
    return HttpResponse(1)

def user_register(request):
    data = request.POST
    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
    return HttpResponse(1)

def users_all(request):
    users = User.objects.all()
    context = {
        'status' : 1,
        'users' : users,
    }
    return JsonResponse(context)

def user_friends(request):
    friends = request.user.person.friends.all()
    return HttpResponse(1)

def user_friends_add(request):
    data = request.POST
    friendid = data['id']
    friend = Person.objects.get(id=friendid)
    person = request.user.person
    person.friends.add(person)
    person.save()
    return HttpResponse(1)

def user_friends_delete(request):
    data = request.POST
    friendid = data['id']
    friend = Person.objects.get(id=friendid)
    person = request.user.person
    person.friends.delete(person)
    person.save()
    return HttpResponse(1)

def user_home(request):
    import datetime
    now = datetime.datetime.now()
    user = request.user
    todos = Todo.objects.filter(assigned_to=user.person, due_date__gte=now, completed=False)
    return HttpResponse(todos)

def todo_add(request):
    data = request.POST
    content = data['content']
    assigned_to = data['assigned_to_username']
    assigned_by = request.user.person
    due_date = data['due_date']
    todo = Todo.objects.create(content=content, assigned_to=assigned_to, assigned_by=assigned_by, due_date=due_date)
    return HttpResponse(1)

def todo_delete(request):
    data = request.POST
    todoid = data['id']
    Todo.objects.delete(id=todoid)
    return HttpResponse(1)

def todo_completed(request):
    data = request.POST
    todoid = data['id']
    Todo.objects.get(id=todoid).update(completed=True)
    return HttpResponse(1)
