import os
from dotenv import load_dotenv

# in bash export RTU="123456"
print(os.environ.get("RTU"))

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)