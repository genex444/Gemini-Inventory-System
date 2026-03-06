from django.contrib import admin
from django.urls import path
from .views import Index, SignUpView, Dashboard, AddItem, EditItem, DeleteItem, TransactionLogsView,StatusChartView,SearchView, IncidentDashboardView,ObstacleListView,ObstacleDeleteView,looker_studio_dashboard,BrokenItemsDashboardView
from django.contrib.auth import views as auth_views
from .views import ExportToExcelView,ItemDetailView #SpecificExportToExcelView
from .views import EditSpecificItemStatusView
from . import views
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
    path('transaction-logs/', TransactionLogsView.as_view(), name='transaction-logs'),
    path('export-excel/', ExportToExcelView.as_view(), name='export-excel'),
    path('charts/', StatusChartView.as_view(), name='charts'),
    path('charts1/', views.StatusSpecificItemsView.as_view(), name='charts1'),
    path('item/<int:pk>/detail/', ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('specific-item/edit/<int:pk>/', EditSpecificItemStatusView.as_view(), name='edit-specific-item-status'),
    path('specific-item/delete/<int:pk>/', views.DeleteSpecificItemView.as_view(), name='delete-specific-item'),
    path('search/', SearchView.as_view(), name='search'),
    path('specific-item/delete/<int:pk>/',DeleteItem.as_view(), name='delete-specific-item'),
    path('incident_overview/', IncidentDashboardView.as_view(), name='incident_dashboard'),
    path('location_data/', views.location_data_view, name='location_data'),  # Add this line
    path('clear-location-data/', views.clear_location_data, name='clear_location_data'),
    path('obstacle-list/', ObstacleListView.as_view(), name='obstacle-list'),
    path('obstacle/delete/<int:pk>/', ObstacleDeleteView.as_view(), name='obstacle-delete'),
    path('daily_checklist/', views.Daily_Checklist_View.as_view(), name='daily_checklist'),
    path('looker-studio/', looker_studio_dashboard, name='looker-studio'),
    path('broken-items/', BrokenItemsDashboardView.as_view(), name='broken-items-dashboard'),

    # path('specific-export-excel/', SpecificExportToExcelView.as_view(), name='specific-export-excel'),

]




