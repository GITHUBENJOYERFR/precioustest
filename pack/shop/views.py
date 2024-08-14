from django.shortcuts import render
from datetime import datetime
def main_index(request):
    context = {
        'current_date': datetime.today().date(),  # Текущая дата
        'current_time': datetime.now().time(),
    }
    return render(request, 'shop/main.html',context)
