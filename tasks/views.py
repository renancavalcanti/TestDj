import requests
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        response = requests.post(
            'http://127.0.0.1:5000/v1/users/login',
            json={'email': email, 'password': password}
        )
        if response.status_code == 200:
            request.session['token'] = response.json().get('token')
            return redirect('tasks')
        else:
            return render(request, 'login.html', {'error': 'Login failed'})
    return render(request, 'login.html')

def fetch_tasks(request):
    token = request.session.get('token')
    headers = {'x-access-token': token}

    created_tasks = requests.get(
        'http://127.0.0.1:5000/v1/tasks/createdby', headers=headers
    ).json()
    assigned_tasks = requests.get(
        'http://127.0.0.1:5000/v1/tasks/assignedto', headers=headers
    ).json()

    print(created_tasks, assigned_tasks)
    
    return render(request, 'tasks.html', {
        'created_tasks': created_tasks['allTasks'],
        'assigned_tasks': assigned_tasks['allTasks']
    })

def create_task(request):
    if request.method == 'POST':
        description = request.POST['description']
        assigned_to_uid = request.POST['assigned_to']
        token = request.session.get('token')
        headers = {'x-access-token': token}

        response = requests.post(
            'http://127.0.0.1:5000/v1/tasks',
            headers=headers,
            json={'description': description, 'assignedToUid': assigned_to_uid}
        )
        return redirect('tasks')
    return render(request, 'create_task.html')

def delete_task(request, task_id):
    token = request.session.get('token')
    headers = {'x-access-token': token}

    requests.delete(
        f'http://127.0.0.1:5000/v1/tasks/{task_id}',
        headers=headers
    )
    return redirect('tasks')

def mark_task_done(request, task_id):
    token = request.session.get('token')
    headers = {'x-access-token': token}

    requests.patch(
        f'http://127.0.0.1:5000/v1/tasks/{task_id}',
        headers=headers,
        json={'done': True}
    )
    return redirect('tasks')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        
        response = requests.post(
            'http://127.0.0.1:5000/v1/users/signup',
            json={'email': email, 'password': password, 'name': name}
        )
        
        if response.status_code == 200:
            return redirect('login')  # Redireciona para a página de login após cadastro bem-sucedido
        else:
            return render(request, 'signup.html', {'error': 'Signup failed. Please try again.'})
    
    return render(request, 'signup.html')