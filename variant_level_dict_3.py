import os
import uuid
from dotenv import load_dotenv
from pricing_dict import artist_royalty_dict
from extract_file_info import extract_file_info
import cloudinary
import cloudinary.uploader
import cloudinary.api
from extract_file_info import extract_file_info
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

#==================================================================
#              Step 1. Upload to Cloudinary & URL
#==================================================================
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

def upload_to_cloudinary(image_path, Cloudinaryfolder):
    load_dotenv()

    cloudinary.config(
        cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key = os.getenv("CLOUDINARY_API_KEY"),
        api_secret = os.getenv("CLOUDINARY_API_SECRET"),
        secure = os.getenv("CLOUDINARY_SECURE").lower() == "true"
    )
    response = cloudinary.uploader.upload(image_path, folder=Cloudinaryfolder)
    public_id = response["public_id"]
    print(f"Uploaded image {public_id} to Cloudinary")
    return public_id
            
def get_image_url_from_cloudinary(public_id):
    resource = cloudinary.api.resource(public_id)
    return resource["url"]


#==================================================================
#                    Variant_level_dictionary 
#==================================================================
def variant_level_dictionary_3(image_filename, output_folder_path,Cloudinaryfolder):
    file_path = os.path.join(output_folder_path, image_filename)
    # Extract image information from filename
    public_id = upload_to_cloudinary(file_path,Cloudinaryfolder)
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    artist= file_info["vendor"]

    # Create a dictionary for the image with all the CSV fields
    image_dict = {
        "Handle":uuid ,
        "Image Src": get_image_url_from_cloudinary(public_id),  # Use the Cloudinary URL
        "Image Alt Text": title,
        "Image Position": image_position,
    }
    
    return image_dict

