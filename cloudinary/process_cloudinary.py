import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
from dotenv import load_dotenv

load_dotenv()
cloudinary.config(cloud_name=os.getenv('CLOUD_NAME'),
                  api_key=os.getenv('API_KEY'),
                  api_secret=os.getenv('API_SECRET'))

# Uploading to the cloud
response = cloudinary.uploader.upload(
    "./pictures/vUwJ8uu_C1M.jpg", use_filename=True)
print(response)

# asd = cloudinary.CloudinaryImage("sample.jpg").image(transformation=[
#     {'gravity': "face", 'height': 200, 'width': 200, 'crop': "thumb"},
#     {'border': "5px_solid_black", 'radius': 20},
#     {'overlay': "cloudinary_icon_white"},
#     {'flags': "relative", 'width': "0.25", 'crop': "scale"},
#     {'opacity': 50},
#     {'flags': "layer_apply", 'gravity': "north_east", 'x': 10, 'y': 10}
# ])

# print(asd)

# asd = cloudinary.utils.cloudinary_url("sample.jpg",
#                                       width=100,
#                                       height=150,
#                                       crop="fill")
