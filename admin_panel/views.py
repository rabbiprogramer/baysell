from django.shortcuts import render

def admin_list (request):
    return render(request ,'admin_panel/admin_list.html')
