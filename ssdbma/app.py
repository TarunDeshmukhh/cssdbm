from flask import Flask , render_template , request ,url_for , redirect
import pymysql

app=Flask(__name__) # creating the object of the flask

@app.route('/home')

def home():
 return render_template('home.html')
 
@app.route('/dashboard',methods=['POST','GET'])

def dashboard():
 user=request.form["user"]
 pas=request.form["pass"]
 peru='username'
 perp='password'
 try:
  if(user==peru and pas==perp):
   return render_template('dashboard.html')
  else:
   return "Please Enter Correct Input"
 except Exception:
  return "Error in try Section"
  
@app.route('/visit',methods=["POST","GET"])

def visit():
 t=request.form["teach"] 
 try:
  if (t=="Tech"):
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try: 
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from teach"
    cur.execute(sql)
    data=cur.fetchall()
    return render_template("teachinglist.html",d=data)
  
   except Exception:
    return "Error in Try"
 
  elif (t=="Nontech"):
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try: 
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from nonteach"
    cur.execute(sql)
    data=cur.fetchall()
    return render_template("nonteachinglist.html",d=data)
  
   except Exception:
    return "Error in Try"
 
  elif (t=="Student"):
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try: 
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from stud"
    cur.execute(sql)
    data=cur.fetchall()
    return render_template("studentlist.html",d=data)
  
   except Exception:
    return "Error in Try"
 
  elif (t=="Logout"):
   return render_template('home.html')
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
 
@app.route('/process',methods=["POST","GET"])

def process():
 t=request.form["any"]
 try:
  if (t=="NewRegistraion"):
   return render_template("newregistration.html")
  elif (t=="Back"):
   return render_template("dashboard.html")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in Try"

@app.route('/newrprocess',methods=["POST","GET"])  
def newrprocess():
 t=request.form["any"]
 try:
  if (t=="Back"):
   return render_template("dashboard.html")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in Try"
   
@app.route('/newregis',methods=["POST","GET"])

def newregis():
 t=request.form["any"]
 try:
  if (t=="teach"):
   return render_template("registrationteach.html")
  elif (t=="nonteach"):
   return render_template("registrationnonteach.html")
  elif (t=="stud"):
   return render_template("regisstud.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
  
  
 #--------------------------------------------Teaching Staff Section Start---------------------------------------
  
@app.route('/insertregt',methods=["POST","GET"])

def insertregt():
 t=request.form['any']
 try:
  if (t=="Save"):
   try:
    n=request.form["name"]
    a=request.form["age"]
    g=request.form["gender"]
    e=request.form["education"]
    se=request.form["subexp"]
    jp=request.form["jp"]
    add=request.form["add"]
    aadhar=request.form["aadhar"]
    pan=request.form["pan"]
    acc=request.form["acc"]
    sal=request.form["sal"]
   
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
   
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="insert into teach(name,age,gender,education,subject_expert,job_position,address,aadhar,pan,account_detail,salary)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,a,g,e,se,jp,add,aadhar,pan,acc,sal)
    cur.execute(sql)
    db.commit()
   
    return redirect("/teachl")
    
   except Exception:
    db.rollback()
    return "Error in save Try"
    
  elif (t=="Back"):
   return render_template("newregistration.html")
   
  elif (t=="Logout"):
   return render_template("home.html")
   
  else:
   return "Error in try"
   
 except Exception:
  return "Error in try" 
 
@app.route("/teachl")

def teachl():
 servername="localhost"
 username="root"
 password=""
 dbname="ssdbma"
 try: 
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from teach"
  cur.execute(sql)
  data=cur.fetchall()
  return render_template("teachinglist.html",d=data)
  
 except Exception:
  return "Error in Try"
  
@app.route("/viewteach/<rid>")

def viewteach(rid):
 try:
  servername="localhost"
  username="root"
  password=""
  dbname="ssdbma"
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from teach where id='{}'".format(rid)
  cur.execute(sql)
  data=cur.fetchone()
  return render_template('teacherinfo.html',d=data)
 except Exception:
  db.rollback()
  return "Error in try"
  
@app.route("/tlistprocess",methods=["POST","GET"])

def tlistprocess():
 try:
  t=request.form["any"]
  if (t=="Newregistration"):
   return render_template("newregistration.html")
  elif (t=="Back"):
   return render_template("dashboard.html")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
  
@app.route("/tinfoprocess",methods=["POST","GET"])
   
def tinfoprocess():
 try:
  t=request.form["any"]
  if (t=="Edit"):
   try:
    rid=request.form["rid"]
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from teach where id='{}'".format(rid)
    cur.execute(sql)
    data=cur.fetchone()
    return render_template('updateteach.html',d=data)
   except Exception:
    db.rollback()
    return "Error in try"
  elif (t=="Delete"):
   rid=request.form["rid"]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try:
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="delete from teach where id='{}'".format(rid)
    cur.execute(sql)
    db.commit()
    return redirect("teachl")
  
   except Exception:
    return "Error in try section"
  elif (t=="Back"):
   return redirect("teachl")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
   


@app.route('/updateteach',methods=['POST','GET'])

def updateteach():
 try:
  t=request.form["any"]
  if (t=="Back"):
   return redirect("/teachl")
  elif (t=="Save"):
   rid=request.form["rid"]
   n=request.form["name"]
   a=request.form["age"]
   g=request.form["gender"]
   e=request.form["education"]
   se=request.form["subexp"]
   jp=request.form["jp"]
   add=request.form["add"]
   aadhar=request.form["aadhar"]
   pan=request.form["pan"]
   acc=request.form["acc"]
   sal=request.form["sal"]
   data=[rid,n,a,g,e,se,jp,add,aadhar,pan,acc,sal]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   db=pymysql.connect(servername,username,password,dbname)
   cur=db.cursor()
   sql="update teach set name='{}',age='{}',gender='{}',education='{}',subject_expert='{}',job_position='{}',address='{}',aadhar='{}',pan='{}',account_detail='{}',salary='{}' where id='{}'".format(n,a,g,e,se,jp,add,aadhar,pan,acc,sal,rid)   
   cur.execute(sql)
   db.commit()
   return render_template('teacherinfo.html',d=data)
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  db.rollback()
  return "Error in try"
 # ---------------------------------Teaching Staff Section End---------------------------------------------------
 
 # ---------------------------------Non-Teaching Staff Section Start---------------------------------------------
  
@app.route('/insertregnont',methods=["POST","GET"])

def insertregnont():
 t=request.form['any']
 try:
  if (t=="Save"):
   try:
    n=request.form["name"]
    a=request.form["age"]
    g=request.form["gender"]
    e=request.form["education"]
    jp=request.form["jp"]
    add=request.form["add"]
    aadhar=request.form["aadhar"]
    pan=request.form["pan"]
    acc=request.form["acc"]
    sal=request.form["sal"]
   
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
   
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="insert into nonteach(name,age,gender,education,job_position,address,aadhar,pan,account_detail,salary)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,a,g,e,jp,add,aadhar,pan,acc,sal)
    cur.execute(sql)
    db.commit()
   
    return redirect("/nonteachl")
    
   except Exception:
    db.rollback()
    return "Error in save Try"
    
  elif (t=="Back"):
   return render_template("newregistration.html")
   
  elif (t=="Logout"):
   return render_template("home.html")
   
  else:
   return "Error in try"
   
 except Exception:
  return "Error in try" 
 
@app.route("/nonteachl")

def nonteachl():
 servername="localhost"
 username="root"
 password=""
 dbname="ssdbma"
 try: 
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from nonteach"
  cur.execute(sql)
  data=cur.fetchall()
  return render_template("nonteachinglist.html",d=data)
  
 except Exception:
  return "Error in Try"
  
@app.route("/viewnonteach/<rid>")

def viewnonteach(rid):
 try:
  servername="localhost"
  username="root"
  password=""
  dbname="ssdbma"
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from nonteach where id='{}'".format(rid)
  cur.execute(sql)
  data=cur.fetchone()
  return render_template('nonteacherinfo.html',d=data)
 except Exception:
  db.rollback()
  return "Error in try"
  
@app.route("/nontlistprocess",methods=["POST","GET"])

def nontlistprocess():
 try:
  t=request.form["any"]
  if (t=="Newregistration"):
   return render_template("newregistration.html")
  elif (t=="Back"):
   return render_template("dashboard.html")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
  
@app.route("/nontinfoprocess",methods=["POST","GET"])
   
def nontinfoprocess():
 try:
  t=request.form["any"]
  if (t=="Edit"):
   try:
    rid=request.form["rid"]
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from nonteach where id='{}'".format(rid)
    cur.execute(sql)
    data=cur.fetchone()
    return render_template('updatenonteach.html',d=data)
   except Exception:
    db.rollback()
    return "Error in try"
  elif (t=="Delete"):
   rid=request.form["rid"]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try:
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="delete from nonteach where id='{}'".format(rid)
    cur.execute(sql)
    db.commit()
    return redirect("nonteachl")
  
   except Exception:
    return "Error in try section"
  elif (t=="Back"):
   return redirect("nonteachl")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
   


@app.route('/updatenonteach',methods=['POST','GET'])

def updatenonteach():
 try:
  t=request.form["any"]
  if (t=="Back"):
   return redirect("/nonteachl")
  elif (t=="Save"):
   rid=request.form["rid"]
   n=request.form["name"]
   a=request.form["age"]
   g=request.form["gender"]
   e=request.form["education"]
   jp=request.form["jp"]
   add=request.form["add"]
   aadhar=request.form["aadhar"]
   pan=request.form["pan"]
   acc=request.form["acc"]
   sal=request.form["sal"]
   data=[rid,n,a,g,e,jp,add,aadhar,pan,acc,sal]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   db=pymysql.connect(servername,username,password,dbname)
   cur=db.cursor()
   sql="update nonteach set name='{}',age='{}',gender='{}',education='{}',job_position='{}',address='{}',aadhar='{}',pan='{}',account_detail='{}',salary='{}' where id='{}'".format(n,a,g,e,jp,add,aadhar,pan,acc,sal,rid)   
   cur.execute(sql)
   db.commit()
   return render_template('nonteacherinfo.html',d=data)
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  db.rollback()
  return "Error in try"
 # ---------------------------------Non-Teaching Staff Section End---------------------------------------------------
# ---------------------------------Students Section Start---------------------------------------------
  
@app.route('/insertregs',methods=["POST","GET"])

def insertregs():
 t=request.form['any']
 try:
  if (t=="Save"):
   try:
    n=request.form["name"]
    a=request.form["age"]
    g=request.form["gender"]
    c=request.form["caste"]
    sem=request.form["sem"]
    y=request.form["year"]
    b=request.form["branch"]
    e=request.form["educ"]
    aad=request.form["aadhar"]
    add=request.form["add"]
   
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
   
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="insert into stud(name,age,gender,caste,current_sem,current_year,branch,last_edu,aadhar,address)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(n,a,g,c,sem,y,b,e,aad,add)
    cur.execute(sql)
    db.commit()
   
    return redirect("/studl")
    
   except Exception:
    db.rollback()
    return "Error in save Try"
    
  elif (t=="Back"):
   return render_template("newregistration.html")
   
  elif (t=="Logout"):
   return render_template("home.html")
   
  else:
   return "Error in try"
   
 except Exception:
  return "Error in try" 
 
@app.route("/studl")

def studl():
 servername="localhost"
 username="root"
 password=""
 dbname="ssdbma"
 try: 
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from stud"
  cur.execute(sql)
  data=cur.fetchall()
  return render_template("studentlist.html",d=data)
  
 except Exception:
  return "Error in Try"
  
@app.route("/viewstud/<rid>")

def viewstud(rid):
 try:
  servername="localhost"
  username="root"
  password=""
  dbname="ssdbma"
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from stud where id='{}'".format(rid)
  cur.execute(sql)
  data=cur.fetchone()
  return render_template('studentinfo.html',d=data)
 except Exception:
  db.rollback()
  return "Error in try"
  
@app.route("/slistprocess",methods=["POST","GET"])

def slistprocess():
 try:
  t=request.form["any"]
  if (t=="Newregistration"):
   return render_template("newregistration.html")
  elif (t=="Back"):
   return render_template("dashboard.html")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
  
@app.route("/sinfoprocess",methods=["POST","GET"])
   
def sinfoprocess():
 try:
  t=request.form["any"]
  if (t=="Edit"):
   try:
    rid=request.form["rid"]
    servername="localhost"
    username="root"
    password=""
    dbname="ssdbma"
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="select * from stud where id='{}'".format(rid)
    cur.execute(sql)
    data=cur.fetchone()
    return render_template('updatestud.html',d=data)
   except Exception:
    db.rollback()
    return "Error in try"
  elif (t=="Delete"):
   rid=request.form["rid"]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   try:
    db=pymysql.connect(servername,username,password,dbname)
    cur=db.cursor()
    sql="delete from stud where id='{}'".format(rid)
    cur.execute(sql)
    db.commit()
    return redirect("studl")
  
   except Exception:
    return "Error in try section"
  elif (t=="Back"):
   return redirect("studl")
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  return "Error in try"
   


@app.route('/updatestud',methods=['POST','GET'])

def updatestud():
 try:
  t=request.form["any"]
  if (t=="Back"):
   return redirect("/studl")
  elif (t=="Save"):
   rid=request.form["rid"]
   n=request.form["name"]
   a=request.form["age"]
   g=request.form["gender"]
   c=request.form["caste"]
   sem=request.form["sem"]
   y=request.form["year"]
   b=request.form["branch"]
   e=request.form["educ"]
   aad=request.form["aadhar"]
   add=request.form["add"]
   data=[rid,n,a,g,c,sem,y,b,e,aad,add]
   servername="localhost"
   username="root"
   password=""
   dbname="ssdbma"
   db=pymysql.connect(servername,username,password,dbname)
   cur=db.cursor()
   sql="update stud set name='{}',age='{}',gender='{}',caste='{}',current_sem='{}',current_year='{}',branch='{}',last_edu='{}',aadhar='{}',address='{}' where id='{}'".format(n,a,g,c,sem,y,b,e,aad,add,rid)   
   cur.execute(sql)
   db.commit()
   return render_template('studentinfo.html',d=data)
  elif (t=="Logout"):
   return render_template("home.html")
  else:
   return "Error Occured"
 except Exception:
  db.rollback()
  return "Error in try"
  
@app.route("/searchstud",methods=["POST","GET"])

def searchstud():
 t=request.form["name"]
 servername="localhost"
 username="root"
 password=""
 dbname="ssdbma"
 try: 
  db=pymysql.connect(servername,username,password,dbname)
  cur=db.cursor()
  sql="select * from stud"
  cur.execute(sql)
  data=cur.fetchall()
  for x in range(0,len(data),1):
   y=data[x]
   y=y[1]
   if t==(y):
    d=data[x] 
    return render_template("studentsearchinfo.html",d=d)
    break
   else:
    continue
  return render_template("searchone.html",d=t)
  
 except Exception:
  return "Error in try"
 
 # ----------------------------------Students Section End---------------------------------------------------


'''
for x in range(0,len(data),1):
 y=x[1].split()
 if t==(y[0] or y[1]):
  d=x 
  return render_template("studentlist.html",d=d)
  break
 else:
  continue
return render_template("searchone.html",d=t)



 
 
'''
  

 
   
 
 
 
app.run()