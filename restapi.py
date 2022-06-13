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
            return {"result":"OK"}
          else:
            return {"result":" Error"}
      else:
            print(type(new))
            return {"result":"Given number is not an integer"}

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
        return {"result:":avg}
    else:
        return{"result":"no numbers in the array"}
@app.get("/numbers/sum")
async def sum():
    s=0
    if numbers!=[]:
        for i in numbers:
            s=s+i
        return {"result:":s}
    else:
        return {"result:":"no numbers in the array"}
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
        return {"result:":st}
    else:
        return {"result:":"no numbers in the array"}
def getnumbers():
    if numbers!=[]:
      return numbers
