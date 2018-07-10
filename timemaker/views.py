from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Content
from django.db.models import Count
import datetime
import csv
from io import TextIOWrapper, StringIO
from django.urls import reverse_lazy
from django.views import generic
from .forms import CSVUploadForm

def index_template(request):
    d = {
        'today': datetime.date.today(),
        '1day': datetime.date.today() - datetime.timedelta(1),
        '2day': datetime.date.today() - datetime.timedelta(2),
        '3day': datetime.date.today() - datetime.timedelta(3),
        '4day': datetime.date.today() - datetime.timedelta(4),
        '5day': datetime.date.today() - datetime.timedelta(5),
        '6day': datetime.date.today() - datetime.timedelta(6),
        '7day': datetime.date.today() - datetime.timedelta(7),
        'today_internet': Content.objects.filter(date=datetime.date.today()).count(),
        '1day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(1)).count(),
        '2day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(2)).count(),
        '3day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(3)).count(),
        '4day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(4)).count(),
        '5day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(5)).count(),
        '6day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(6)).count(),
        '7day_internet': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(7)).count(),
        'youmaketoday': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(1)).count() - Content.objects.filter(date=datetime.date.today()).count(),
        'youmakeweek': Content.objects.filter(date=datetime.date.today()-datetime.timedelta(7)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(8)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(9)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(10)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(11)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(12)).count() + Content.objects.filter(date=datetime.date.today()-datetime.timedelta(13)).count() - Content.objects.filter(date=datetime.date.today()).count() -  Content.objects.filter(date=datetime.date.today()-datetime.timedelta(1)).count() - Content.objects.filter(date=datetime.date.today()-datetime.timedelta(2)).count() - Content.objects.filter(date=datetime.date.today()-datetime.timedelta(3)).count() - Content.objects.filter(date=datetime.date.today()-datetime.timedelta(4)).count() - Content.objects.filter(date=datetime.date.today()-datetime.timedelta(5)).count() - Content.objects.filter(date=datetime.date.today()-datetime.timedelta(6)).count(),
        'actname1': Content.objects.filter(date=datetime.date.today()).values('site').annotate(total=Count('site')).order_by('-total')[0],
        'actname2': Content.objects.filter(date=datetime.date.today()).values('site').annotate(total=Count('site')).order_by('-total')[1],
        'actname3': Content.objects.filter(date=datetime.date.today()).values('site').annotate(total=Count('site')).order_by('-total')[2],
        'actname4': Content.objects.filter(date=datetime.date.today()).values('site').annotate(total=Count('site')).order_by('-total')[3],
        'actname5': Content.objects.filter(date=datetime.date.today()).values('site').annotate(total=Count('site')).order_by('-total')[4],
    }
    return render(request, 'index.html', d)

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            Content(),
            Content.id = line[0]
            Content.site = line[1]
            Content.url = line[2]
            Content.date = line[3]
            Content.start = line[4]
            Content.end = line[5]
            Content.save()

        return render(request, 'upload.html')

    else:
        return render(request, 'upload.html')

class PostImport(generic.FormView):
    template_name = 'import.html'
    success_url = reverse_lazy('timemaker:index_template')
    form_class = CSVUploadForm
 
    def form_valid(self, form):
        # csv.readerに渡すため、TextIOWrapperでテキストモードなファイルに変換
        csvfile = TextIOWrapper(form.cleaned_data['file'])
        reader = csv.reader(csvfile)
        # 1行ずつ取り出し、作成していく
        for row in reader:
            content = Content()
            content.id = row[0]
            content.site = row[1]
            content.url = row[2]
            content.date = row[3]
            content.start = row[4]
            content.end = row[5]
            content.save()
        return super().form_valid(form)
