import os
from pricing_dict import artist_royalty_dict

product_sizes = {
    "acrylic": {
        "Portrait": [
            {"size": "24x30cm", "ratio": 1.25, "price": 144},
            {"size": "32x40cm", "ratio": 1.25, "price": 256},
            {"size": "48x60cm", "ratio": 1.25, "price": 576},
            {"size": "64x80cm", "ratio": 1.25, "price": 1024},
        ],
        "Landscape": [
            {"size": "30x24cm", "ratio": 1.25, "price": 144},
            {"size": "40x32cm", "ratio": 1.25, "price": 256},
            {"size": "60x48cm", "ratio": 1.25, "price": 576},
            {"size": "80x64cm", "ratio": 1.25, "price": 1024},
        ],
        "Square": [
            {"size": "24x24cm", "ratio": 1.0, "price": 115.2},
            {"size": "40x40cm", "ratio": 1.0, "price": 320},
            {"size": "60x60cm", "ratio": 1.0, "price": 720},
            {"size": "80x80cm", "ratio": 1.0, "price": 1280},
        ],
    },
    "canvas": {
        "Portrait": [
            {"size": "100x150cm", "ratio": 0.67, "price": 750},
            {"size": "80x120cm", "ratio": 0.67, "price": 480},
            {"size": "60x90cm", "ratio": 0.67, "price": 270},
            {"size": "40x60cm", "ratio": 0.67, "price": 120},
            {"size": "100x140cm", "ratio": 0.71, "price": 700},
            {"size": "80x112cm", "ratio": 0.71, "price": 448},
            {"size": "60x84cm", "ratio": 0.71, "price": 252},
            {"size": "50x70cm", "ratio": 0.71, "price": 175},
            {"size": "105x140cm", "ratio": 0.75, "price": 735},
            {"size": "90x120cm", "ratio": 0.75, "price": 540},
            {"size": "60x80cm", "ratio": 0.75, "price": 240},
            {"size": "54x72cm", "ratio": 0.75, "price": 194.4},
            {"size": "120x150cm", "ratio": 0.8, "price": 900},
            {"size": "80x100cm", "ratio": 0.8, "price": 400},
            {"size": "60x75cm", "ratio": 0.8, "price": 225},
            {"size": "40x50cm", "ratio": 0.8, "price": 100},
        ],
    },
    "canvas": {
        "Landscape": [
            {"size": "150x100cm", "ratio": 1.5, "price": 750},
            {"size": "120x80cm", "ratio": 1.5, "price": 480},
            {"size": "90x60cm", "ratio": 1.5, "price": 270},
            {"size": "60x40cm", "ratio": 1.5, "price": 120},
            {"size": "140x105cm", "ratio": 1.33, "price": 735},
            {"size": "120x90cm", "ratio": 1.33, "price": 540},
            {"size": "80x60cm", "ratio": 1.33, "price": 240},
            {"size": "72x54cm", "ratio": 1.33, "price": 194.4},
            {"size": "150x120cm", "ratio": 1.25, "price": 900},
            {"size": "100x80cm", "ratio": 1.25, "price": 400},
            {"size": "75x60cm", "ratio": 1.25, "price": 225},
            {"size": "50x40cm", "ratio": 1.25, "price": 100},
            {"size": "140x100cm", "ratio": 1.4, "price": 700},
            {"size": "112x80cm", "ratio": 1.4, "price": 448},
            {"size": "84x60cm", "ratio": 1.4, "price": 252},
            {"size": "70x50cm", "ratio": 1.4, "price": 175}
        ]
    },
    "Poster": {
        "Portrait": [
            {"size": "16x12in", "ratio": 0.75, "price": 18.58},
            {"size": "24x18in", "ratio": 0.75, "price": 41.81},
            {"size": "40x30in", "ratio": 0.75, "price": 116.13}
        ],
        "Landscape": [
            {"size": "12x16in", "ratio": 1.33, "price": 18.58},
            {"size": "18x24in", "ratio": 1.33, "price": 41.81},
            {"size": "30x40in", "ratio": 1.33, "price": 116.13}
        ]
    },
    "wallpaper": {
        "Portrait": [
            {"size": "60x120cm", "ratio": 0.5, "price": 180},
            {"size": "60x250cm", "ratio": 0.24, "price": 375},
            {"size": "60x305cm", "ratio": 0.2, "price": 457.5},
            {"size": "120x250cm", "ratio": 0.48, "price": 750},
            {"size": "120x305cm", "ratio": 0.39, "price": 915}
        ]
    },
}

stationary = {
    "Notebook": [
        {"size": "A5 - Portrait", "price": 25},
        {"size": "A4 - Portrait", "price": 25}
    ],
    "Pre-Sketchbook": [
        {"size": "A4 - Portrait", "price": 25}
    ],
    "Greeting Card": [
        {"size": "A5", "price": 25}
    ],
    "Mugs": [
        {"size": "Standard", "price": 35}
    ],
    "Stickers": [
        {"size": "Set of 5 Different Stickers", "price": 25},
        {"size": "5cm x 5cm", "price": 50}
    ]
}






def extract_file_info(file_path):
    # Extract file name from file path
    file_name = os.path.basename(file_path)
    # Split file name into parts based on delimiter
    file_parts = file_name.split("--")

    # Extract variables from file parts
    aspect_ratio = float(file_parts[0])
    uuid = file_parts[1]
    product_type = file_parts[2]
    title_var = file_parts[3]
    image_position_var = int(file_parts[4])
    artist_name = os.path.splitext(file_parts[5])[0]

    # Derive orientation from aspect ratio
    if aspect_ratio < 1:
        orientation = "Portrait"
    elif aspect_ratio > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Create dictionary containing the extracted variables
    file_info = {
        "aspect_ratio": aspect_ratio,
        "uuid": uuid,
        "product_type": product_type,
        "title_var": title_var,
        "image_position_var": image_position_var,
        "vendor": artist_name,
        "option1_name": "Size",
    }

    # Extract option 1 values and prices if product type is supported
    if product_type.lower() in ["canvas", "poster", "acrylic", "wallpaper"]:
        option1_values, option1_prices = extract_option1Value_wallArt(file_info, product_type, orientation)
        artist_price = artist_royalty_dict.get(artist_name, 1)
        print(artist_price)
        if "OBL Display SS" in file_info["vendor"].lower():
            shutterstock_price = 257.0
            option1_prices = [round(p + shutterstock_price, 2) for p in option1_prices]
        else:
            option1_prices = [round(p * artist_price, 2) for p in option1_prices]
        file_info["option1_values"] = option1_values
        file_info["option1_prices"] = option1_prices
    return file_info


def extract_option1Value_wallArt(file_info, product_type, orientation):
    # Derive orientation from aspect ratio
    aspect_ratio = file_info['aspect_ratio']
    if aspect_ratio < 1:
        orientation = "Portrait"
    elif aspect_ratio > 1:
        orientation = "Landscape"
    else:
        orientation = "Square"

    # Define the option values based on the product type and orientation
    if product_type.lower() in ["canvas", "poster", "acrylic", "wallpaper"] and orientation in product_sizes[product_type.lower()]:
        option1_values = []
        option1_prices = []
        for dimensions in product_sizes[product_type.lower()][orientation]:
            option_aspect_ratio = dimensions['ratio']
            # Check if the aspect ratio of the canvas size matches the aspect ratio of the image
            if abs(aspect_ratio - option_aspect_ratio) < 0.00001:
                option1_values.append(dimensions['size'])
                option1_prices.append(dimensions['price'])
    elif product_type.lower() in stationary and not orientation:
        option1_values = []
        option1_prices = []
        for item in stationary[product_type.lower()]:
            option1_values.append(item['size'])
            option1_prices.append(item['price'])
    else:
        option1_values = []
        option1_prices = []

    return option1_values, option1_prices



# def extract_option1Value_wallArt(file_info, product_type, orientation):
#     # Derive orientation from aspect ratio
#     aspect_ratio = file_info['aspect_ratio']
#     if aspect_ratio < 1:
#         orientation = "Portrait"
#     elif aspect_ratio > 1:
#         orientation = "Landscape"
#     else:
#         orientation = "Square"

#     # Define the option values based on the product type and orientation
#     if product_type.lower() in ["canvas", "poster", "acrylic", "wallpaper"] and orientation in product_sizes[product_type.lower()]:
#         option1_values = []
#         option1_prices = []
#         for dimensions in product_sizes[product_type.lower()][orientation]:
#             option1_values.append(dimensions['size'])
#             option1_prices.append(dimensions['price'])
#     elif product_type.lower() == "canvas" and orientation in product_sizes[product_type.lower()]:
#         option1_values = []
#         option1_prices = []
#         for dimensions in product_sizes[product_type.lower()][orientation]:
#             size_parts = dimensions['size'].split('x')
#             width_cm = float(size_parts[0])
#             height_cm = float(size_parts[1])
#             aspect_ratio_tolerance = dimensions['ratio'] * 0.01
#             aspect_ratio_min = dimensions['ratio'] - aspect_ratio_tolerance
#             aspect_ratio_max = dimensions['ratio'] + aspect_ratio_tolerance
#             if abs(aspect_ratio - (width_cm / height_cm)) <= aspect_ratio_tolerance:
#                 option1_values.append(dimensions['size'])
#                 option1_prices.append(dimensions['price'])
#     elif product_type.lower() in stationary and not orientation:
#         option1_values = []
#         option1_prices = []
#         for item in stationary[product_type.lower()]:
#             option1_values.append(item['size'])
#             option1_prices.append(item['price'])
#     else:
#         option1_values = []
#         option1_prices = []

#     return option1_values, option1_prices


def extract_price_stationary(file_info, product_type):
    if product_type.lower() in stationary:
        option1_values = []
        option1_prices = []
        for item in stationary[product_type.lower()]:
            option1_values.append(item['size'])
            option1_prices.append(item['price'])
    else:
        option1_values = []
        option1_prices = []

    return option1_values, option1_prices



def test_extract_file_info():
    file_path = "1.5--d2c9bf--canvas--Sunset--1--Artist 1.jpg"
    actual_file_info = extract_file_info(file_path)

    

