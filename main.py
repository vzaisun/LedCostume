from fastapi import FastAPI, HTTPException
from firebase_admin import credentials, db, initialize_app
from DataInput import DataInputMain
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



# Configure CORS
origins = [
    "http://localhost:3000",
    # Add other origins as needed
]




firebase_credentials = {
   "type": "service_account",
    "project_id": "ledcostume-da444",
    "private_key_id": "28890dc3efd493f3efd995a29cddad789249af12",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDaRdrABKQrBQB4\nf5cssBqTaz5Irxz1mM1FUlocrE66sMZlgYC8p5o+ruPQJohGRojPR0/RMETLksM8\n6jZMk7jYMYOTzPmlCCaGerTswPSRTN8swrVhN8QL4256sf15L2gs9Sz5bKHRbWAl\n23abbM0wKc4+Kyfd6+vzbqGMZbazuDWYA76v2XG6RhS47M5JuoMLF/zhVUT1yVWV\nuYr5yv3ZuRhNG9uWRxaKWql6tH9R0yeYIK68z2hXrs0Q2YwEW8ZhDLk+iKSgcM0d\ntCJoZQcP+VN/X3bYT3vMAz3G2dGJwUlYKfokTYtYX6RQWhmfNKcvaRVnpHztosHS\njaHzXpvVAgMBAAECggEADscN8VQfHT6AcqgIvyDJG9P16ovYhRQsSZYyvaA40FDp\njbO/2IXsXnQOvmftb/yUhJwKXlpLPhEYoMYmmPajXBe2FcqZ2D9+BDrIhwLlS/UN\nYwVnrEZPQpLKRwpH4+1+uxR6UAS3y+sAyG9cT1eFaM5bxT+8ujyfw+Jok43LWc1t\n50HF0y3wyIjkb6dIy9bKilNh2Arut1jzcclf0b4CLV/RicNs6k7A+DtyQz+rPNnr\noP5MtFBzPrLnSbxcD8PU9ClNeLBlkTG81YvsyO48R1Ywc7DsQ0kQJIfVGkaDZTcK\ncMAzmY7GTNKRXMqmgmavx56svyQdF/fUUg0MsvuMwQKBgQDx2XHmUgI8tFhJnWTL\nDdow7J138QiU1kPYP5ywMGPrhqXNvPEdPSJM8XUSHss7+jSGACPsSiCCbE7NxpKV\nU7rIteKVVd5cvBYA+tfocZiiUvqfe1572qS1oFeJp9ehjDIDMUlDp+2bPAgdT4R7\nNjeiQpsnCe1yq1iGl9TrJmTa8QKBgQDnC0RpXGlpnXV/YMiMmjvr0PBTd9eFH3ui\nrmYm8Ifn1nNrPlrwVDNtKwS4CG2XUY1o8Mleiigk6mK1sKbAcqs4LGPqcYd5l6iD\nXUNeb8l/IVwvFugdp5Cc4hvjFHjjcVTnqCOQIaduqaYKtDZqmHYdMpdUNhXhO17t\nhNcidfRnJQKBgFnIyfohc+cpZKVfoy2m5NvI2+TNPMxUhzde1kKqlE253Q/2FuUt\n7u/1q+qgN/76MkmU/8EW+96vasoF8CEzxmIA9C9Qg46V3O1cMo9+rJWGjLhsSnVc\nhE1RS241O14j9+UrhPFzBEjfDnwjKyG6zQiWBZeGnfo2FlVRRKBPzp1hAoGAWssI\ntUbFfeWMuOO1q9soVQEkkAh2PzAiC8nxBrhbD/YsISa94deU5f+TuSZGusInieel\nmms8X1VkOPYUcWgedNKs6QJ4NIYuiIDr6n6PdlALw82CpbSllaEdSF1RLD/rF6Xx\nY8B15XzxbR9oivci41JwOX2Pl5UXNsuPJ1GnG6kCgYBVIxVyjOSiiglNmMVY3LXs\n45JYxk6k3/jwtZHxlV1WvMPeFMuR7JZ6I9zmpcz/a40R7h60p+ZBDNFrAsLEml3g\nENcj2R1CKTQJSuQ+pIFKRYsrhZkKgx1kmMOg33UUO1P7dL4L/uIYQPgT4mwWIj7c\nm8+SNEGnqqPgKoSFmTQA5Q==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-lekip@ledcostume-da444.iam.gserviceaccount.com",
    "client_id": "116540224852342633854",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lekip%40ledcostume-da444.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}


cred = credentials.Certificate(firebase_credentials)
initialize_app(cred, {
    'databaseURL': 'https://ledcostume-da444-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

class EffectInput(BaseModel):
    new_data: str



def get_effect_data():
    data_path = '/effect'
    ref = db.reference(data_path)
    return ref.get()

def update_effect_data(new_data):
    data_path = '/effect'
    ref = db.reference(data_path)
    ref.set(new_data)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/root")
async def root():
    return get_effect_data()

@app.post("/add_effect")
async def add_effect(effect_input: EffectInput):
    new_data = effect_input.new_data
    print(new_data)
    existing_data = str(get_effect_data()) 
    
    updated_data = existing_data + str(new_data)
    
    # Update the effect data in the database
    update_effect_data(updated_data)

    return {"message": "Effect added successfully"}