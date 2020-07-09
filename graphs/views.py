from django.db.models import Avg, Q
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GraphData, Student, Month

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# scripts
def test(request):
    years = GraphData.objects.order_by('graph_year')

    distinct_years = years.distinct()

    for y in years:
        months = y.month_set.all()
        for t in month_names:
            if months.filter(month=t).first() == None:
                month_instance = Month.objects.create(month=t, year=y)

    return render(request, 'graphs/test.html')

# page loaders
def swarm(request):
    return render(request, 'graphs/index.html')

def graphs(request):
    return render(request, 'graphs/graphs.html', {'nbar': 'graphs'})

def data_ottawa(request):
    ottawa = GraphData.objects.filter(source_text='Ottawa CDA').order_by('graph_year')

    return render(request, 'graphs/data_ottawa.html', {'ottawa': ottawa, 'nbar': 'data_oy'})

def data_victoria(request):
    victoria = GraphData.objects.filter(source_text='Victoria Gonzales').order_by('graph_year')

    return render(request, 'graphs/data_victoria.html', {'victoria': victoria, 'nbar': 'data_vy'})

def data_m(request):
    years = GraphData.objects.order_by('graph_year').values_list('graph_year', flat=True).distinct()

    return render(request, 'graphs/data_m.html', {'years': years, 'nbar': 'data_m'})

def add_data(request):
    names = Student.objects.all()
    form = request.POST

    return render(request, 'graphs/add_data.html', {'names': names, 'nbar': 'add'})

# ajax requests
def load_months(request):
    year = request.GET.get('year')

    if year != '---------':
        ottawa = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        victoria = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        oevent = vevent = ''
        years = GraphData.objects.filter(graph_year=year)

        for y in years:
            months = y.month_set.all()
            for m in months:
                this_month = Month.objects.filter(year=year, month=m)
                if y.source_text == 'Ottawa CDA':
                    ottawa[month_chooser(m.month)] = Month.objects.get(year=y, month=m, year__source_text="Ottawa CDA")
                    oevent = y.event
                else:
                    victoria[month_chooser(m.month)] = Month.objects.get(year=y, month=m, year__source_text="Victoria Gonzales")
                    vevent = y.event

        return render(request, 'graphs/month_options.html', {'ottawa': ottawa, 'victoria': victoria, 'oevent': oevent, 'vevent': vevent})
    else:
        return render(request, 'graphs/month_options.html')

def load_years(request):
    student_id = request.GET.get('student')
    years = []
    if student_id != '---------':
        years = GraphData.objects.filter(student=student_id).order_by('graph_year')
        return render(request, 'graphs/year_options.html', {'years': years, 'source': years[0]})
    else:
        return render(request, 'graphs/year_options.html')

def save_data(request):
    student_id = request.GET.get('student_id')
    climates = request.GET.getlist('climates[]')
    source = request.GET.get('source')
    temps = list(request.GET.getlist('temps[]'))
    precips = list(request.GET.getlist('precips[]'))

    years = GraphData.objects.filter(student=student_id).order_by('graph_year')
    first_year = years.filter(graph_year=climates[0])
    second_year = years.filter(graph_year=climates[4])
    third_year = years.filter(graph_year=climates[8])
    i = 0

    for y in years:
        update_months(y, temps[i].split(), precips[i].split())
        i += 1

    first_year.update(average_temperature=climates[1], average_precipitation=climates[2], event=climates[3], latitude=climates[12], longitude=climates[13], source_text=source)
    second_year.update(average_temperature=climates[5], average_precipitation=climates[6], event=climates[7], latitude=climates[12], longitude=climates[13], source_text=source)
    third_year.update(average_temperature=climates[9], average_precipitation=climates[10], event=climates[11], latitude=climates[12], longitude=climates[13], source_text=source)

    return render(request, 'graphs/add_data.html')

# helper functions
def update_months(year, temps, precips):

    for m in month_names:
        this_month = Month.objects.filter(year=year, month=m)
        this_temp = float(this_month.values_list('total_temperature', flat=True)[0])
        this_precip = float(this_month.values_list('total_precipitation', flat=True)[0])
        new_temp = float(temps[month_chooser(m)])
        new_precip = float(precips[month_chooser(m)])

        if (this_temp - new_temp) != 0.0:
            this_month.update(total_temperature=new_temp)
        if (this_precip - new_precip) != 0.0:
            this_month.update(total_precipitation=new_precip)

def month_chooser(mon):
    if mon == month_names[0]:
        return 0
    if mon == month_names[1]:
        return 1
    if mon == month_names[2]:
        return 2
    if mon == month_names[3]:
        return 3
    if mon == month_names[4]:
        return 4
    if mon == month_names[5]:
        return 5
    if mon == month_names[6]:
        return 6
    if mon == month_names[7]:
        return 7
    if mon == month_names[8]:
        return 8
    if mon == month_names[9]:
        return 9
    if mon == month_names[10]:
        return 10
    if mon == month_names[11]:
        return 11

# graph APIs
class YearAvgTemp(APIView):

    def get(self, request, format=None):
        climates = GraphData.objects.order_by('graph_year')
        years = climates.values_list('graph_year', flat=True).distinct()

        tempO = {el:0 for el in years}
        tempV = {el:0 for el in years}
        sumTempO = sumTempV = i = j = 0
        avgTotalTempVictoria = avgTotalTempOttawa = 0

        for climate in climates:
            if (climate.source_text == "Ottawa CDA"):
                if climate.average_precipitation != 0.0:
                    i += 1
                    sumTempO += climate.average_temperature
                    tempO[climate.graph_year] = climate.average_temperature
                else:
                    tempO[climate.graph_year] = 0
            else:
                if climate.average_precipitation != 0.0:
                    j += 1
                    sumTempV += climate.average_temperature
                    tempV[climate.graph_year] = climate.average_temperature
                else:
                    tempV[climate.graph_year] = 0

        if i != 0:
            avgTotalTempOttawa = sumTempO/i
        if j != 0:
            avgTotalTempVictoria = sumTempV/j

        newTempO = {k:v - avgTotalTempOttawa if v != 0 else v for (k,v) in tempO.items()}
        newTempV = {k:v - avgTotalTempVictoria if v != 0 else v for (k,v) in tempV.items()}

        data = {
            "climate_labels": years,
            "climate_data1": list(newTempO.values()),
            "climate_data2": list(newTempV.values()),
            "ottawa_average": float('%0.2f'%avgTotalTempOttawa),
            "victoria_average": float('%0.2f'%avgTotalTempVictoria)
        }

        return Response(data)

class OttawaSeasonalAvgPrec(APIView):

    def get(self, request, forma=None):
        return Response(seasonalDiagram("Ottawa CDA"))

class VictoriaSeasonalAvgPrec(APIView):

    def get(self, request, forma=None):
        return Response(seasonalDiagram("Victoria Gonzales"))

class OttawaMonthly(APIView):

    def get(self, request, format=None):
        return Response(climateDiagram("Ottawa CDA"))

class VictoriaMonthly(APIView):

    def get(self, request, format=None):
        return Response(climateDiagram("Victoria Gonzales"))

def climateDiagram(source):
    # average monthly precipitation ottawa
    temps = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # average monthly precipitation victoria
    precs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    s = Month.objects.filter(~Q(year__average_precipitation=0)).filter(year__source_text=source)

    for i in range(len(month_names)):
        temps[i] = s.filter(month=month_names[i]).aggregate(Avg('total_temperature'))['total_temperature__avg'] or 0
        precs[i] = s.filter(month=month_names[i]).aggregate(Avg('total_precipitation'))['total_precipitation__avg'] or 0

    data = {
        'climate_labels': month_names,
        'climate_data1': temps,
        'climate_data2': precs,
    }

    return data

def seasonalDiagram(source):
    winter = ['Jan', 'Feb', 'Dec']
    spring = ['Mar', 'Apr', 'May']
    summer = ['Jun', 'Jul', 'Aug']
    autumn = ['Sep', 'Oct', 'Nov']
    climates = GraphData.objects.order_by('graph_year').filter(source_text=source)
    years = climates.values_list('graph_year', flat=True).distinct()
    s = Month.objects.filter(~Q(year__average_precipitation=0)).filter(year__source_text=source)

    data1 = {el:0 for el in years}
    data2 = {el:0 for el in years}
    data3 = {el:0 for el in years}
    data4 = {el:0 for el in years}

    for climate in climates:
        data1[climate.graph_year] = s.filter(month__in=winter, year__graph_year=climate.graph_year).aggregate(Avg('total_precipitation'))['total_precipitation__avg'] or 0
        print(data1)
        data2[climate.graph_year] = s.filter(month__in=spring, year__graph_year=climate.graph_year).aggregate(Avg('total_precipitation'))['total_precipitation__avg'] or 0
        data3[climate.graph_year] = s.filter(month__in=summer, year__graph_year=climate.graph_year).aggregate(Avg('total_precipitation'))['total_precipitation__avg'] or 0
        data4[climate.graph_year] = s.filter(month__in=autumn, year__graph_year=climate.graph_year).aggregate(Avg('total_precipitation'))['total_precipitation__avg'] or 0

    data = {
        'climate_labels': years,
        'climate_data1': list(data1.values()),
        'climate_data2': list(data2.values()),
        'climate_data3': list(data3.values()),
        'climate_data4': list(data4.values())
    }

    return data
