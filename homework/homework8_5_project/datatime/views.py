from django.shortcuts import render
from datetime import datetime

def hw8_5(request):
    return render(request,'datatime/hw8_5.html')


def datatime(request):
    current_datetime = datetime.now()

    return render(request,'datatime/datatime.html', {'data':current_datetime })

# def multiplicationTable(request):


def programmersday(request):
    current_datetime = datetime.now()
    year = current_datetime.year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        number = '12/09'
    else:
        number = '13/09'

    return render(request, 'datatime/programers_day.html', { 'number': number})


def table(request):
    return render(request,'datatime/table.html')


