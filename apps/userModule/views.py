from django.shortcuts import render

def user_list(request):
    users = User.objects.all()
    return render(request, "userModule/user_list.html",{"users": users})


def user_create(request):
    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')

    else:
        form = UserForm()
    return render(request, 'userModule/user_form.html', {'form': form})


def user_update(request, pk):
    pass

def user_delete(request, pk):