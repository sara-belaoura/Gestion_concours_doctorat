"""

The `urlptterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.urls import path,re_path
from app import views
from app import viewsDE
from app import viewsDPGR
from app import viewsCorrecteur
from django.conf.urls import include
app_name = "app"

urlpatterns = [
   
    path('calculer_resul_module_epr', views.calculer_resul_module_epr,name='calculer_resul_module_epr'),
    path('R_DPGR/', views.R_DPGR, name='R_DPGR'),
    path('affichage_resultat_spec', views.affichage_resultat_spec, name='affichage_resultat_spec'),
    path('calculer_Resultat_final/', views.calculer_Resultat_final, name='calculer_Resultat_final'),
    path('calculer_resul_module/', views.calculer_resul_module, name='calculer_resul_module'),
    path('create_epreuve/', views.create_epreuve, name='create_epreuve'),
    path('coder/', views.coder, name='coder'),
    path('generer_code/', views.generer_code, name='generer_code'),
    #path('creer_sp/', views.create_specialite, name='creer_sp'),
    path('corriger/', views.ajouter_note, name='corriger'),

    path('signup/', views.signup, name='signup'),
    path('correction/',views.correction,name="correction"),
   # path('login/', views.login_page, name='login_page'),
   # path('loginacc/', views.loginn, name='loginacc'),
   # path('accounts/', include('django.contrib.auth.urls')),
   
    path('redirection/', views.redirection, name='redirection'),

    #path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('importFile/', views.importFile, name='importFile'),
    path('uploadFile/', views.uploadFile, name='uploadFile'),
    path('downloadFile/<str:filename>', views.downloadFile, name='downloadFile'),
    path('', views.index),
    #coté DE 
    path('AccueilDE/', viewsDE.AccueilDE, name='AccueilDE'),
    
    path('affecterSallesSIQ/', viewsDE.affecterSalleSIQ,name='affecterSallesSIQ'),
    path('affecterSallesSIT/', viewsDE.affecterSalleSIT,name='affecterSallesSIT'),
   
    path('affecterSurveillant/', viewsDE.affecterSurveillant,name='affecterSurveillant'),
    path('releverAbscence/', viewsDE.releverAbscence, name='releverAbscence'),
    path('downloadListCan/', viewsDE.downloadListCan, name='downloadListCan'),

    #coté DPGR
    path('AccueilDPGR/', viewsDPGR.AccueilDPGR, name='AccueilDPGR'),
    path('ImporterCanSIQ/', viewsDPGR.ImporterCanSIQ, name='ImporterCanSIQ'),
    path('ImporterCanSIT/', viewsDPGR.ImporterCanSIT, name='ImporterCanSIT'),
    path('ImporterCorriges/', viewsDPGR.ImporterCorriges, name='ImporterCorriges'),
    path('ImporterEns/', viewsDPGR.ImporterEns, name='ImporterEns'),
    path('dashboard_DPGR/', viewsDPGR.dashboard_DPGR, name='dashboard_DPGR'),
    path('Mesdocuments_DPGR/', viewsDPGR.Mesdocuments_DPGR, name='Mesdocuments_DPGR'),
    
    
    #coté Correcteur 
    path('AccueilCorrecteur/', viewsCorrecteur.AccueilCorrecteur, name='AccueilCorrecteur'),
    path('Correction/', viewsCorrecteur.Correction, name='Correction'),
    path('dashboard_correcteur/', viewsCorrecteur.dashboard_correcteur, name='dashboard_correcteur')

]
"""path('validerSalles/<str:filename>', views.validerSalles, name='validerSalles'),"""







