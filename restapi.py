from fastapi import FastAPI                                                                                                                                             

app = FastAPI()

numbers=[]

@app.get("/")
async def showMessage():
    return {"response":"HOME"}

@app.post("/numbers")

async def addnumber(new):
  if type(new) == str:
      if '.' not in new:
          if new.isdigit():
            numbers.append(int(new))
            return {"response":numbers}
          else:
            return {"reponse":"Result Error"}
      else:
            print(type(new))
            return {"reponse":"Given number is not an integer"}

@app.get("/return")
async def showvalues():
    return getnumbers()
@app.get("/numbers/average")
async def average():
    c=0
    s=0
    avg = 0.0 
    if numbers!=[]:
        for i in numbers:
            s = s+i
            c=c+1
        avg = s/c
        return {"reponse:":avg}
    else:
        return{"response":"no numbers in the array"}
@app.get("/numbers/sum")
async def sum():
    s=0
    if numbers!=[]:
        for i in numbers:
            s=s+i
        return {"reponse:":s}
    else:
        return {"response:":"no numbers in the array"}
@app.get("/numbers/stddev")
async def std():
    s=0
    st = 0.0
    avg=0.0
    c=0
    if numbers!=[]:
        for i in numbers:
            s=s+i
            c=c+1
        avg=s/c
        for i in numbers:
            sd_s=avg-i
            st = st + (sd_s*sd_s)
        return {"reponse:":st}
    else:
        return {"response:":"no numbers in the array"}
def getnumbers():
    if numbers!=[]:
      return numbers
