import os
from dotenv import load_dotenv, dotenv_values

# in bash export RTU="123456"
print(os.environ.get("RTU"))

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
print(SECRET_KEY)

# OR

config = dotenv_values(".env")
