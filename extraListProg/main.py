from flask import Flask,request,render_template

app=Flask(__name__)

studentList=[
    {"roll":1,"name":"amit","marks":10},
    {'roll':2,"name":"dev","marks":20}
            ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addStudent')
def addStudent():
    rollFrm=int(request.form['studRoll'])
    nameFrm=request.form['studName']
    marksFrm=int(request.form['studMarks'])

@app.route('/printStudent')
def printStudent():
    return studentList

@app.route('/deleteStudent',methods=["POST"])
def deleteStudent():
    if request.form['studRoll']=='':
        return render_template('index.html')
    rollFrm=int(request.form['studRoll'])
    index=0
    found=False
    for stud in studentList:
        if stud['roll']==rollFrm:
            found=True
            del studentList[index]
        index+=1
    if found==False:
        return f"Roll No. {rollFrm} not found"
    else:
        return studentList

@app.route('/searchStudent',methods=['POST',"GET"])
def searchStudent():
    if request.form['studRoll']=='':
        message=f"<h1>Roll number cannot be blank</h1>"
        message+=f"<a href='/'>Click for home page</a>"
        return message  

    rollFrm=request.form['studRoll']
    found=False
    for stud in studentList:
        if stud['roll']== int(rollFrm):
            found=True
            return stud  
    if found==False:
        return f"<h1>Roll no. {rollFrm} not found</h1>"   
    
@app.route('/insertStudent',methods=["POST"])
def insertStudent():
    rollFrm=request.form['studRoll']
    nameFrm=request.form['studName']
    marksFrm=request.form['studMarks']

    if rollFrm=="" or nameFrm=='' or marksFrm=="":
        message= f"<h1>Please fill all the details</h1>"
        message+= f"<a href='/'>Go back to Home Page</a>" 
        return message
    
    tempDict={}
    tempDict['roll']=int(rollFrm)
    tempDict['name']=nameFrm
    tempDict['marks']=int(marksFrm)
    studentList.append(tempDict)
    return studentList

@app.route("/updateMarks",methods=['POST'])
def updateMarks():
    rollFrm=request.form['studRoll']
    nameFrm=request.form['studName']
    marksFrm=request.form['studMarks']

    if rollFrm=="" or marksFrm=="":
        message= f"<h1>Please fill Roll No. and Marks</h1>"
        message+= f"<a href='/'>Go back to Home Page</a>" 
        return message
    
    #tempDict={}
    #tempDict['roll']=int(rollFrm)
    #tempDict['name']=nameFrm
    #tempDict['marks']=int(marksFrm)
    
    
    for index in range(0,len(studentList)):
        
        if studentList[index]['roll']==int(rollFrm):
            #studentList[index].update(marks=int(marksFrm))
            studentList[index]['marks']=int(marksFrm)
            #studentList[index].update({"hi":f'{marksFrm}','uni':'pu'})
            

            
        
            break
    return studentList

@app.route('/updateStudent',methods=["POST"])
def updateStudent():
    rollFrm=request.form.get('studRoll')
    nameFrm=request.form.get('studName')
    marksFrm=request.form.get('studMarks')

    if rollFrm == '' or nameFrm=='' or marksFrm=='':
        message='<h1>Please fill all the details</h1>'
        message+="<h1><a href='/'>Go to Home Page</a></h1>"
        return message
    
    index=0
    found=False
    for stud in studentList:
        if stud.get('roll')==int(rollFrm):
            found=True
            stud['name']=nameFrm
            stud['marks']=int(marksFrm)
            studentList[index]=stud
            return studentList
        if found==False:
            message= f"<h1>Roll No. {rollFrm} not found<br>"
            message+="<a href='/'>Go to Home</a></h1>"
            return message








if __name__=='__main__':
    app.run(debug=True)