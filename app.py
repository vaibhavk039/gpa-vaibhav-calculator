from flask import Flask,request,render_template,redirect,abort,url_for
from  werkzeug.debug import get_current_traceback
import json

app = Flask(__name__)

@app.route('/user1')

def user1():
  gpa=request.args['gpa']
  return render_template("/user.html",gpa=gpa)


@app.route('/')

def user():
 
  return render_template("/user.html")
 
 
  



@app.route('/table',methods = ['POST', 'GET'])
def table():
  sub=[]
  inter=[]
  exter=[]
  tot=[]
  grade=[]
  credit=[]
  grades=[]
  sum=0
  leng=0
  sum1=0
  res_list=[]
  gpa=''
  reg=0

  
  if(request.form.get('ch') =='1'):
     gf='may-june2021.json'

  elif(request.form.get('ch') =='2'):
     gf='march2021(firstyear).json'
  elif(request.form.get('ch') =='3'):
     gf='nov-dec2020.json'
  elif(request.form.get('ch')=='4'):
     gf='may-june2020.json'
  elif(request.form.get('ch')=='5'):
     gf='nov-dec2019.json'
  elif(request.form.get('ch')=='6'):
     gf='may-june2019.json'
  elif(request.form.get('ch')=='7'):
     gf='nov-dec2018.json'
  else:    
    gpa="Select a Semester!!"
    return redirect(url_for('user1',gpa=gpa))
  
  f = open (gf, "r")                   
 
  data = json.loads(f.read())
  
  if request.method=="POST": 
       
   reg=request.form.get('reg')
   
   a=[key[0] for key in data.items()]
   
  
   if(reg not in a):
        gpa="Record not found"
        return redirect(url_for('user1',gpa=gpa))
        
   else:
     
        for i in data[reg]:

          sub.append(data[reg][i]['sub'])
          inter.append(data[reg][i]['int'])
          exter.append(data[reg][i]['ext'])
          tot.append(data[reg][i]['tot'])
          grade.append(data[reg][i]['grade'])
          credit.append(data[reg][i]['credit'])
          
     
        for gr in grade:
           if gr =='S':
                grades.append(10)

           elif gr == 'A':
                grades.append(9)
           elif gr == 'B':
                grades.append(8)
           elif gr == 'C':
                grades.append(7)
           elif gr== 'D': 
                grades.append(6)
           elif gr == 'E':
                grades.append(5)
           else:
                  
                grades.append(0)
       
        for i in range(0, len(grades)):
          res_list.append(grades[i] * credit[i])
  
        
        for cr in credit:
          sum=sum+cr
         
        for frg in res_list:
          sum1=sum1+frg
        
        if sum != 0:
          gpa = sum1 / sum
   
        else:
          gpa = 0

        
        gpa=round(gpa,2)
        leng=len(sub)
        
      
      
    
       
       
     
  return render_template("/table.html",sub=sub,inter=inter,exter=exter,tot=tot,grade=grade,credit=credit,gpa=gpa,leng=leng,reg=reg)  
@app.route('/aboutus')

def aboutus():
 
  return render_template("/aboutus.html")
 

if __name__ == '__main__':

     app.run(debug=True)    