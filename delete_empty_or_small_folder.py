import cloudinary
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv

def delete_empty_or_small_folders(folder_name):
    load_dotenv()

    cloudinary.config(
        cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
        api_key = os.getenv("CLOUDINARY_API_KEY"),
        api_secret = os.getenv("CLOUDINARY_API_SECRET"),
        secure = os.getenv("CLOUDINARY_SECURE").lower() == "true"
    )

    # List resources in the specified folder
    resources = cloudinary.api.resources(type="upload", prefix=folder_name, max_results=500)["resources"]

    for resource in resources:
        public_id = resource["public_id"]
        resource_type = resource["type"]
        file_size = resource["bytes"]

        if resource_type == "upload" and file_size < 1000000:
            # Delete small-sized resource (less than 1 MB)
            cloudinary.api.delete_resources(public_id)
            print(f"Deleted resource {public_id}")

    # Check if the folder is empty
    if not resources:
        # Delete the empty folder
        cloudinary.api.delete_folder(folder_name)
        print(f"Deleted empty folder: {folder_name}")

# Example usage
delete_empty_or_small_folders("product-images")
