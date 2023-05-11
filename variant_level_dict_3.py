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

def upload_to_cloudinary(image_path):
    cloudinary.config(
    cloud_name = "djqvqmqe2",
    api_key = "379169473671185",
    api_secret = "HFgkfTbvvKlD0TGtXmQDLBFBDys",
    secure = True
)
    response = cloudinary.uploader.upload(image_path, folder="product-images/")
    public_id = response["public_id"]
    print(f"Uploaded image {public_id} to Cloudinary")
    return public_id
            
def get_image_url_from_cloudinary(public_id):
    resource = cloudinary.api.resource(public_id)
    return resource["url"]


#==================================================================
#                    Variant_level_dictionary 
#==================================================================
def variant_level_dictionary_3(image_filename, output_folder_path):
    file_path = os.path.join(output_folder_path, image_filename)
    # Extract image information from filename
    public_id = upload_to_cloudinary(file_path)
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
        "Title": title,
        "Body (HTML)": "",
        "Vendor": artist,
        "Product Category": "",
        "Type": product_type,
        "Tags": "Miscellaneous",
        "Published": "TRUE",
        "Option1 Name": "Size",
        "Option1 Value":"N/A",
        "Option2 Name": "",
        "Option2 Value": "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Variant Inventory Qty":10,
        "Variant Inventory Policy": "deny",
        "Variant Fulfillment Service":"manual",
        "Variant Price": 0,
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
        "Variant Inventory Qty":"10",
        "Variant Inventory Policy": "deny",
        "Variant Fulfillment Service":"manual",
    }
    
    return image_dict

