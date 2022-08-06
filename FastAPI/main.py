from fastapi import FastAPI
import codeBAse.hello as utills

app = FastAPI()


@app.get("/")
def home():

    ans = utills.add(2,3)
    print(ans)

    return {"name":f"{ans}"}