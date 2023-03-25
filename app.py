from flask import Flask,request,jsonify
app = Flask(__name__)
parking_slot=[]
a = []
d=[]
parking_slot=[]


@app.route('/parking_lot',methods=['POST'])
def parking():
  if request.method=='POST':
      data=request.get_json()
      parking_slot.clear()
      parking_slot.append(data['no_of_slot'])
      a.append([i for i in range(1,parking_slot[0]+1)])
      return jsonify("total slot:"+str(data['no_of_slot']))

@app.route('/parking_lot',methods=['PATCH'])
def increaseparking():
  if request.method=='PATCH':
      data=request.get_json()
      result=parking_slot[0]+data['increment_slot']
      parking_slot.clear()
      parking_slot.append(result)
      a.clear()
      a.append([i for i in range(1, parking_slot[0] + 1)])
      return jsonify("total slot:"+str(result))


@app.route('/park',methods=['POST'])
def allotparking():
  if request.method=='POST':

    data = request.get_json()
    emptyslots = []
    # print(data)

    if len(a)!=0:
      for i in range(0, len(a[0])):
        if i in a[0]:
          emptyslots.append(i)
        else:
          pass
    x = emptyslots
    if len(x) != 0:
      x.sort()
      y="alloted slot is :"+str(x[0])
      # print("alloted slot is", x[0])
      data['slot_number']=x[0]
      d.append(data)
      a[0].remove(x[0])
      emptyslots.remove(x[0])
    else:
        y="parking lot is already full"

    return jsonify(y)

@app.route('/registration_numbers/<color>',methods=['GET'])
def getparking(color):
  if request.method=='GET':
      cars = []
      for i in range(len(d)):
          if d[i]['car_color'] == color:
              cars.append(d[i]['car_reg_no'])
      return jsonify(cars)


@app.route('/clear',methods=['POST'])
def clearparking():
  if request.method == 'POST':
     r = []
     data=request.get_json()
     if data['slot_number']:
       for i in range(len(d)):
          if d[i]['slot_number'] == data['slot_number']:
           # r=d[i]['slot_number']
             del d[i]
     else:

       for j in range(len(d)):
          if d[j]['car_registration_no']==data['car_registration_no']:
             r.append(d[j]['slot_number'])
             print(r)
             del d[j]
     # a[0].append(r[0])

    # result={"freed_slot_number":r}
     return jsonify("freed_slot_number:"+str(r[0]))




if __name__ == "__main__":
    app.run(debug=True)