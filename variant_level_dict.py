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

def upload_to_cloudinary(image_path,Cloudinaryfolder):
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
def variant_level_dictionary(image_filename, output_folder_path, Cloudinaryfolder, option, price,image_filename_dict):
    print(image_filename)
       # Check if image filename already exists in dictionary
    if image_filename in image_filename_dict:
        print(image_filename)
        print(True)
        # Retrieve public ID from dictionary and use it to generate the image URL
        public_id = image_filename_dict[image_filename]
        image_url = get_image_url_from_cloudinary(public_id)
    else:
        print(False)
        # Upload image to Cloudinary and get public ID
        image_path = os.path.join(output_folder_path, image_filename)
        public_id = upload_to_cloudinary(image_path, Cloudinaryfolder)
        image_filename_dict[image_filename] = public_id
        # Generate the image URL from the public ID
        image_url = get_image_url_from_cloudinary(public_id)
    
    # Extract image information from filename
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
        "Option1 Value":option,
        "Option2 Name": "",
        "Option2 Value": "",
        "Option3 Name": "",
        "Option3 Value": "",
        "Variant Inventory Qty":10,
        "Variant Inventory Policy": "deny",
        "Variant Fulfillment Service":"manual",
        "Variant Price":price if price else 0,
        "Image Src": image_url,  # Use the Shopify URL
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

