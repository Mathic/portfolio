from django.urls import path

from . import views

urlpatterns = [
    # running scripts
    path('test', views.test, name='test'),

    # page loaders
    path('', views.swarm, name='swarm'),
    path('swarm', views.graphs, name='graphs'),
    path('data_ottawa', views.data_ottawa, name='data_ottawa'),
    path('data_victoria', views.data_victoria, name='data_victoria'),
    path('data_month', views.data_m, name='data_month'),
    path('add1', views.add_data, name='add_data'),
    # for base template:
    # <!-- <li class="nav-item {% if nbar == 'add' %}active{% endif %}">
    # <a class="nav-link" href="{% url 'add_data' %}">Add</a>
    # </li> -->

    # ajax requests
    path('ajax/load-months', views.load_months, name='ajax_load_months'),
    path('ajax/load-years', views.load_years, name='ajax_load_years'),
    path('ajax/save-data', views.save_data, name='ajax_save_data'),

    # graph APIs
    path('api/chart/year_avg_temp', views.YearAvgTemp.as_view(), name='year_avg_temp'),
    path('api/chart/ottawa_seasonal', views.OttawaSeasonalAvgPrec.as_view(), name='ottawa_seasonal'),
    path('api/chart/victoria_seasonal', views.VictoriaSeasonalAvgPrec.as_view(), name='victoria_seasonal'),
    path('api/chart/ottawa_monthly', views.OttawaMonthly.as_view(), name='ottawa_monthly'),
    path('api/chart/victoria_monthly', views.VictoriaMonthly.as_view(), name='victoria_monthly'),
]
