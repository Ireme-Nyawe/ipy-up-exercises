from django.shortcuts import render, redirect

tasks = []

def todo_list(request):

    if request.method == 'POST':

        # Add a new task
        if 'add_task' in request.POST:
            task = request.POST.get('task')

            if task:
                tasks.append(task)

        # Delete a task
        elif 'delete_task' in request.POST:
            index = int(request.POST.get('delete_task'))
            if 0 <= index < len(tasks):
                tasks.pop(index)

        return redirect('todo')

    return render(request, 'todo/index.html', {
        'tasks': tasks,
        'total': len(tasks)
    })