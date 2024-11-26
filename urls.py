from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path('PatientLogin.html', views.PatientLogin, name="PatientLogin"), 
	       path('PatientLoginAction', views.PatientLoginAction, name="PatientLoginAction"),
	       path('Register.html', views.Register, name="Register"), 
	       path('RegisterAction', views.RegisterAction, name="RegisterAction"),
	       path('DoctorLogin.html', views.DoctorLogin, name="DoctorLogin"), 
	       path('DoctorLoginAction', views.DoctorLoginAction, name="DoctorLoginAction"),
	       path('OTPAction', views.OTPAction, name="OTPAction"),
	       path('TrainML', views.TrainML, name="TrainML"),
	       path('DatasetVisualize', views.DatasetVisualize, name="DatasetVisualize"),	   
	       path('PredictDisease', views.PredictDisease, name="PredictDisease"),
	       path('PredictDiseaseAction', views.PredictDiseaseAction, name="PredictDiseaseAction"),	 
	       path('AnalysePatient', views.AnalysePatient, name="AnalysePatient"),	 
]