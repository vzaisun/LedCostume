from fastapi import FastAPI, HTTPException
from firebase_admin import credentials, db, initialize_app
from DataInput import DataInputMain

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\sgvij\\Downloads\\credentials.json")
initialize_app(cred, {
    'databaseURL': 'https://ledcostume-da444-default-rtdb.asia-southeast1.firebasedatabase.app/'
})



def get_effect_data():
    data_path = '/effect'
    ref = db.reference(data_path)
    return ref.get()

def update_effect_data(new_data):
    data_path = '/effect'
    ref = db.reference(data_path)
    ref.set(new_data)

app = FastAPI()

@app.get("/root")
async def root():
    return int(get_effect_data())


@app.post("/add_effect")
async def add_effect():
    new_data = DataInputMain()
    existing_data = str(get_effect_data()) 
    
    
    updated_data = existing_data  + str(new_data)
    
    # Update the effect data in the database
    update_effect_data(updated_data)

    return {"message": "Effect added successfully"}

