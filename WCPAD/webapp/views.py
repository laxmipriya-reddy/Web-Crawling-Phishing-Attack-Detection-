
from django.shortcuts import render,redirect
from sklearn.naive_bayes import BernoulliNB
from sklearn.neural_network import MLPClassifier
from django.http import HttpResponse, request
from .models import onlineuser
from .models import dataset
from .models import graph
from django.core import serializers
from django.template import Context
import xlrd
import numpy as np
import pandas as pd
import sys
import time
from sklearn import metrics
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt;
from .urlaction import URLCheck
from .Prediction import predict_nn

def home(request):
	return render(request, 'index.html')
def userhomedef(request):
	if "useremail" in request.session:
		uid=request.session["useremail"]
		d=onlineuser.objects.filter(email__exact=uid)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

	
def adminhomedef(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
		return render(request, 'admin_home.html')

	else:
		return render(request, 'admin.html')

	

def userlogoutdef(request):
	try:
		del request.session['useremail']
	except:
		pass
	return render(request, 'user.html')
def adminlogoutdef(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')	
	
def adminlogindef(request):
	return render(request, 'admin.html')

def userlogindef(request):
	return render(request, 'user.html')

def signupdef(request):
	return render(request, 'signup.html')
def usignupactiondef(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=onlineuser.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'signup.html',{'msg':"Email Already Registered"})
	else:
		d=onlineuser(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})
def userloginactiondef(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=onlineuser.objects.filter(email__exact=uid)
			request.session['useremail']=uid
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')
def adminloginactiondef(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')
def uploaddataset(request):
	if "adminid" in request.session:
		

		return render(request, 'upload.html')

	else:
		return render(request, 'admin.html')
def xlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="F:\\"+file
		print(file,'---------------------------------------------------------------------')
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		dataset.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			f5 = sheet.cell(r, 5).value
			f6 = sheet.cell(r, 6).value
			f7 = sheet.cell(r, 7).value
			f8 = sheet.cell(r, 8).value
			f9 = sheet.cell(r, 9).value
			f10 = sheet.cell(r, 10).value
			f11 = sheet.cell(r, 11).value
			f12 = sheet.cell(r, 12).value
			f13 = sheet.cell(r, 13).value
			f14 = sheet.cell(r, 14).value
			f15 = sheet.cell(r, 15).value
			f16 = sheet.cell(r, 16).value
			res = sheet.cell(r, 17).value
			d=dataset(v1=f0,v2=f1,v3=f2,v4=f3,v5=f4,v6=f5,v7=f6,v8=f7,v9=f8,v10=f9,v11=f10,v12=f11,v13=f12,v14=f13,v15=f14,v16=f15,v17=f16,res=res)
			d.save()
		return render(request, 'upload.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')

def predictions(request):
	if "adminid" in request.session:
		
		return render(request, 'predictions.html')

	else:
		return render(request, 'admin.html')
def nntest(request):
	if "adminid" in request.session:
		return render(request, 'nntest.html')

	else:
		return render(request, 'admin.html')
def naivetest(request):
	if "adminid" in request.session:
		return render(request, 'naivetest.html')
	else:
		return render(request, 'admin.html')




def naiveprediction(request):
	if "adminid" in request.session:
		
		
		file=request.POST['tfile']
		file="F:\\"+file
		trainset = []
		y_train = []
		trainset.clear()
		y_train.clear()
            
		data=dataset.objects.all()
		for d in data:
			x_train = []
			x_train.clear()
			x_train.append(float(d.v1))
			x_train.append(float(d.v2))
			x_train.append(float(d.v3))
			x_train.append(float(d.v4))
			x_train.append(float(d.v5))
			x_train.append(float(d.v6))
			x_train.append(float(d.v7))
			x_train.append(float(d.v8))
			x_train.append(float(d.v9))
			x_train.append(float(d.v10))
			x_train.append(float(d.v11))
			x_train.append(float(d.v12))
			x_train.append(float(d.v13))
			x_train.append(float(d.v14))
			x_train.append(float(d.v15))
			x_train.append(float(d.v16))
			x_train.append(float(d.v17))
			
			y_train.append([d.res])
			trainset.append(x_train)

                
			#print(d.v1,d.v2)
		trainset = np.array(trainset)
		y_train = np.array(y_train)
		tf = pd.read_csv(file)
		print(tf)
		url = tf['URL']
		U1 = np.array(url)
		res = tf['Result']
		R1 = np.array(res)
		tf = tf.drop(['URL'], 1)
		tf = tf.drop(['Result'], 1)
		testdata = np.array(tf)
		print(testdata)
		testdata = testdata.reshape(len(testdata), -1)
		nv = BernoulliNB()
		nv.fit(trainset, y_train)
		s = time.clock()
		result = nv.predict(testdata)  # Predicting 
		print(result)
		
		act=[]
		for r in R1:
			r=float(r)
			act.append(str(r))

		print(act,'<<<<<<<<<<<<<<<<<<<<<<<<<<')
		accuracy = accuracy_score(act, result)
		print(accuracy,'%Acuracy')
		accuracy=int(accuracy*100)
		#s=graph.objects.update(naive=accuracy)
		s=graph.objects.all().delete()
		d=graph(naive=accuracy,nn=0)
		d.save()
		
                
		return render(request, 'nbresults.html',{'msg':accuracy})

	else:
		return render(request, 'admin.html')


def nnprediction(request):
	if "adminid" in request.session:
		
		
		file=request.POST['tfile']
		file="F:\\"+file
		trainset = []
		y_train = []
		trainset.clear()
		y_train.clear()
            
		data=dataset.objects.all()
		for d in data:
			x_train = []
			x_train.clear()
			x_train.append(float(d.v1))
			x_train.append(float(d.v2))
			x_train.append(float(d.v3))
			x_train.append(float(d.v4))
			x_train.append(float(d.v5))
			x_train.append(float(d.v6))
			x_train.append(float(d.v7))
			x_train.append(float(d.v8))
			x_train.append(float(d.v9))
			x_train.append(float(d.v10))
			x_train.append(float(d.v11))
			x_train.append(float(d.v12))
			x_train.append(float(d.v13))
			x_train.append(float(d.v14))
			x_train.append(float(d.v15))
			x_train.append(float(d.v16))
			x_train.append(float(d.v17))
			
			y_train.append([d.res])
			trainset.append(x_train)

                
			#print(d.v1,d.v2)
		trainset = np.array(trainset)
		y_train = np.array(y_train)
		tf = pd.read_csv(file)
		url = tf['URL']
		U1 = np.array(url)
		res = tf['Result']
		R1 = np.array(res)
		tf = tf.drop(['URL'], 1)
		tf = tf.drop(['Result'], 1)
		testdata = np.array(tf)
		testdata = testdata.reshape(len(testdata), -1)
		nv = MLPClassifier()
		nv.fit(trainset, y_train)
		s = time.clock()
		result = nv.predict(testdata)  # Predicting 
		print(result)
		
		act=[]
		for r in R1:
			r=float(r)
			act.append(str(r))

		print(act,'<<<<<<<<<<<<<<<<<<<<<<<<<<')
		accuracy = accuracy_score(act, result)
		print(accuracy,'%Acuracy')
		accuracy=int(accuracy*100)
		s=graph.objects.update(nn=accuracy)
               
		return render(request, 'nnresults.html',{'msg':accuracy})
	else:
		return render(request, 'admin.html')

def graphview(request):
	if "adminid" in request.session:
		performance=[]
		row=graph.objects.all()
		for r in row:
			performance.append(r.naive)
			performance.append(r.nn)
		objects = ('Naive','NN')
		y_pos = np.arange(len(objects))
		print(performance)
		plt.bar(y_pos, performance, align='center', alpha=0.5)
		plt.xticks(y_pos, objects)
		plt.ylabel('%')
		plt.title('Performance of Naive, ANN ')
		plt.show()
	return redirect('predictions')

def prediction(request):
	if "useremail" in request.session:
		return render(request, 'usearch.html')
	else:
		return redirect('userlogout')
def getprediction(request):
	url=request.POST['url']
	u=URLCheck()
	res= u.validation(url)
	if res==True:
		pass
	else:
		return render(request, 'search.html',{'msg':"Enter Valid URL"})
	#---------------------
	if URLCheck.ipaddress(url):
		f1 = 1
	else:
		f1 = 0
	#---------------------
	if URLCheck.favicon(url):
		f8 = 1
	else:
		f8 = 0
	#---------------------
	if URLCheck.extractPort(url):
		f9 = 0
	else:
		f9 = 1
	#---------------------
	print("length of url==" , len(url))
	if len(url)>24:f2=0
	else:f2=1
    #---------------------
	if url.find('@') == -1:f4 = 0
	else:f4 = 1
	#-----------------------
	if url.count('//') > 7:f5 = 0
	else:f5 = 1
    #------------------
	# --------------------
	if url.find('-') == -1:f6 = 1
	else:f6 = 0
        # --------------------
	if url.count('.') > 2:f7 = 0
	else:f7 = 1
        # --------------------
	if url.find('https') ==-1:f10 = 0
	else:f10 = 1
        # --------------------
	if url.find('mailto') == -1:f15 = 0
	else:f15 = 1
    ####################################
	row1 = ["f1", "f2", "f4", "f5", "f6", "f7","f8", "f9", "f10", "f15"]
	row=[f1,f2,f4,f5,f6,f7,f8,f9,f10,f15]
	print(row,"<<<<<<<<Row")
	import csv
	with open('F://test.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(row1)
		writer.writerow(row)
		csvFile.close()
	res=predict_nn()
	print(res)
	
	if float(res)>0:
		m='Legitimate Website'
	else:
		m='Phishing Website'

	return render(request, 'usearch2.html',{'msg':m,'url':url})	
	#return render(request, 'usearch2.html')	


        
        








# Create your views here. naiveprediction
