import cloudinary
import cloudinary.uploader
import cloudinary.api
from extract_file_info import extract_file_info
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

import requests
import openai
import re
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

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
#              Product_level_dictionary
#==================================================================

def product_level_dictionary(image_filename, output_folder_path, Cloudinaryfolder):
    file_path = os.path.join(output_folder_path, image_filename)
    public_id = upload_to_cloudinary(file_path, Cloudinaryfolder)
    # Extract image information from filename
    file_info = extract_file_info(image_filename)
    aspect_ratio = file_info["aspect_ratio"]
    uuid = file_info["uuid"]
    product_type = file_info["product_type"]
    title = file_info["title_var"]
    image_position = file_info["image_position_var"]
    artist= file_info["vendor"]
    option1_values = file_info["option1_values"]
    option1_prices = file_info["option1_prices"]
    # Create a dictionary for the image with all the CSV fields
    image_dict = {
        "Handle":uuid ,
        "Title": title,
        "Body (HTML)": "",
        "Vendor": artist,
        "Product Category": "",
        "Type": product_type,
        "Tags": "Miscellaneous",
        "Published": "TRUE",
        "Option1 Name": "Size",
        "Option1 Value":option1_values[0] if option1_values else "",
        "Variant Inventory Qty":10,
        "Variant Inventory Policy": "deny",
        "Variant Fulfillment Service":"manual",
        "Variant Price":option1_prices[0] if option1_prices else "",
        "Image Src": get_image_url_from_cloudinary(public_id),  # Use the Cloudinary URL
        "Image Alt Text": title,
        "Gift Card": "FALSE",
        "SEO Title": "",
        "SEO Description": "",
        "Variant Image": "",
        "Variant Weight Unit": "kg",
        "Variant Tax Code": "",
        "Cost per item": "",
        "Included / United Arab Emirates": "TRUE",
        "Included / International": "FALSE",
        "Price / International": "",
        "Compare At Price / International": "",
        "Status": "active",
        "Image Position": image_position,

    }
    return image_dict

# def test_product_level_dictionary(output_folder_path):
#     file_name = "1.5--12345--canvas--abstract--1--Jane_Doe.jpg"
#     output = product_level_dictionary(file_name,output_folder_path=output_folder_path)
#     print(output)

# test_product_level_dictionary()