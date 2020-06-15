from django.http import HttpResponse
from django.shortcuts import render

from chocolate.models import *

# Create your views here.
def chocolate(request):
    cbar = ChocolateBar.objects.order_by('company')
    context = {
        'nbar': 'home',
        'cbar': cbar
    }
    return render(request, 'chocolate/index.html', context)
    # return HttpResponse("Hello, world! You're in the info index.")

def beans(request):
    return render(request, 'chocolate/beans.html', {'nbar': 'beans'})
    # return HttpResponse("Hello, world! You're in the info index.")

def first_time(request):
    file_path = "./chocolate/static/chocolate/data/datasets_1919_3310_flavors_of_cacao.csv"
    df = pd.read_csv(file_path)
    print(df.info())
    chocobars = [ChocolateBar(
            company = df.iloc[row]['company'],
            bar_name = df.iloc[row]['bar_name'],
            ref = df.iloc[row]['ref'].item(),
            date = df.iloc[row]['date'].item(),
            percent = df.iloc[row]['percent'].item(),
            company_location = df.iloc[row]['company_location'],
            rating = df.iloc[row]['rating'].item(),
            bean_type = df.iloc[row]['bean_type'],
            bean_origin = df.iloc[row]['bean_origin'],
        )
        for row in range(len(df))
    ]
    ChocolateBar.objects.bulk_create(chocobars)

    context = {'nbar': 'data',
               'df': df.head()}
    return render(request, 'chocolate/read_data.html', context)
