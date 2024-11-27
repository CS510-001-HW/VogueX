# VogueX
# Copyright (c) 2024 Group 84: Aditi Reddy, Ashwin Ramesh Kannan, Bhuvan Kurra, Devesh Vaidya
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import pandas as pd

# Load the dataset
data = pd.read_csv("website/datasets/fashion-dataset/styles.csv", on_bad_lines='skip')

# Aggregate mappings for each feature
aggregations = {
    'gender': {
        'Boys': 'Boys',
        'Girls': 'Girls',
        'Men': 'Men',
        'Women': 'Women',
        'Unisex': 'Unisex'
    },
    'masterCategory': {
        'Accessories': 'Accessories',
        'Apparel': 'Clothing',
        'Footwear': 'Personal',
        'Free Items': 'Other',
        'Sporting Goods': 'Other',
        'Home': 'Personal',
        'Personal Care': 'Personal'
    },
    'subCategory' : {
        'Accessories': 'Accessories',
        'Apparel Set': 'Clothing',
        'Bags': 'Accessories',
        'Bath and Body': 'Personal Care',
        'Beauty Accessories': 'Beauty',
        'Belts': 'Accessories',
        'Bottomwear': 'Clothing',
        'Cufflinks': 'Accessories',
        'Dress': 'Clothing',
        'Eyes': 'Beauty',
        'Eyewear': 'Accessories',
        'Flip Flops': 'Footwear',
        'Fragrance': 'Personal Care',
        'Free Gifts': 'Accessories',
        'Gloves': 'Accessories',
        'Hair': 'Beauty',
        'Headwear': 'Accessories',
        'Home Furnishing': 'Home and Living',
        'Innerwear': 'Clothing',
        'Jewellery': 'Accessories',
        'Lips': 'Beauty',
        'Loungewear and Nightwear': 'Clothing',
        'Makeup': 'Beauty',
        'Mufflers': 'Accessories',
        'Nails': 'Beauty',
        'Perfumes': 'Personal Care',
        'Sandal': 'Footwear',
        'Saree': 'Clothing',
        'Scarves': 'Accessories',
        'Shoe Accessories': 'Accessories',
        'Shoes': 'Footwear',
        'Skin': 'Beauty',
        'Skin Care': 'Beauty',
        'Socks': 'Clothing',
        'Sports Accessories': 'Sporting Goods',
        'Sports Equipment': 'Sporting Goods',
        'Stoles': 'Accessories',
        'Ties': 'Accessories',
        'Topwear': 'Clothing',
        'Umbrellas': 'Accessories',
        'Vouchers': 'Other',
        'Wallets': 'Accessories',
        'Watches': 'Accessories',
        'Water Bottle': 'Accessories',
        'Wristbands': 'Accessories',
    },
    'articleType' : {
        'Accessory Gift Set': 'Gifts and Special Occasions',
        'Baby Dolls': 'Miscellaneous',
        'Backpacks': 'Miscellaneous',
        'Bangle': 'Accessories',
        'Basketballs': 'Sporting Goods',
        'Bath Robe': 'Clothing',
        'Beauty Accessory': 'Personal Care',
        'Belts': 'Accessories',
        'Blazers': 'Clothing',
        'Body Lotion': 'Personal Care',
        'Body Wash and Scrub': 'Personal Care',
        'Booties': 'Footwear',
        'Boxers': 'Clothing',
        'Bra': 'Clothing',
        'Bracelet': 'Accessories',
        'Briefs': 'Clothing',
        'Camisoles': 'Clothing',
        'Capris': 'Clothing',
        'Caps': 'Accessories',
        'Casual Shoes': 'Footwear',
        'Churidar': 'Clothing',
        'Clothing Set': 'Clothing',
        'Clutches': 'Accessories',
        'Compact': 'Personal Care',
        'Concealer': 'Personal Care',
        'Cufflinks': 'Accessories',
        'Cushion Covers': 'Home and Living',
        'Deodorant': 'Personal Care',
        'Dresses': 'Clothing',
        'Duffel Bag': 'Miscellaneous',
        'Dupatta': 'Clothing',
        'Earrings': 'Accessories',
        'Eye Cream': 'Personal Care',
        'Eyeshadow': 'Personal Care',
        'Face Moisturisers': 'Personal Care',
        'Face Scrub and Exfoliator': 'Personal Care',
        'Face Serum and Gel': 'Personal Care',
        'Face Wash and Cleanser': 'Personal Care',
        'Flats': 'Footwear',
        'Flip Flops': 'Footwear',
        'Footballs': 'Sporting Goods',
        'Formal Shoes': 'Footwear',
        'Foundation and Primer': 'Personal Care',
        'Fragrance Gift Set': 'Gifts and Special Occasions',
        'Free Gifts': 'Gifts and Special Occasions',
        'Gloves': 'Accessories',
        'Hair Accessory': 'Accessories',
        'Hair Colour': 'Personal Care',
        'Handbags': 'Accessories',
        'Hat': 'Accessories',
        'Headband': 'Accessories',
        'Heels': 'Footwear',
        'Highlighter and Blush': 'Personal Care',
        'Innerwear Vests': 'Clothing',
        'Ipad': 'Miscellaneous',
        'Jackets': 'Clothing',
        'Jeans': 'Clothing',
        'Jeggings': 'Clothing',
        'Jewellery Set': 'Accessories',
        'Jumpsuit': 'Clothing',
        'Kajal and Eyeliner': 'Personal Care',
        'Key chain': 'Accessories',
        'Kurta Sets': 'Clothing',
        'Kurtas': 'Clothing',
        'Kurtis': 'Clothing',
        'Laptop Bag': 'Miscellaneous',
        'Leggings': 'Clothing',
        'Lehenga Choli': 'Clothing',
        'Lip Care': 'Personal Care',
        'Lip Gloss': 'Personal Care',
        'Lip Liner': 'Personal Care',
        'Lip Plumper': 'Personal Care',
        'Lipstick': 'Personal Care',
        'Lounge Pants': 'Clothing',
        'Lounge Shorts': 'Clothing',
        'Lounge Tshirts': 'Clothing',
        'Makeup Remover': 'Personal Care',
        'Mascara': 'Personal Care',
        'Mask and Peel': 'Personal Care',
        'Mens Grooming Kit': 'Personal Care',
        'Messenger Bag': 'Miscellaneous',
        'Mobile Pouch': 'Miscellaneous',
        'Mufflers': 'Accessories',
        'Nail Essentials': 'Personal Care',
        'Nail Polish': 'Personal Care',
        'Necklace and Chains': 'Accessories',
        'Nehru Jackets': 'Clothing',
        'Night suits': 'Clothing',
        'Nightdress': 'Clothing',
        'Patiala': 'Clothing',
        'Pendant': 'Accessories',
        'Perfume and Body Mist': 'Personal Care',
        'Rain Jacket': 'Clothing',
        'Rain Trousers': 'Clothing',
        'Ring': 'Accessories',
        'Robe': 'Clothing',
        'Rompers': 'Clothing',
        'Rucksacks': 'Miscellaneous',
        'Salwar': 'Clothing',
        'Salwar and Dupatta': 'Clothing',
        'Sandals': 'Footwear',
        'Sarees': 'Clothing',
        'Scarves': 'Accessories',
        'Shapewear': 'Clothing',
        'Shirts': 'Clothing',
        'Shoe Accessories': 'Footwear',
        'Shoe Laces': 'Footwear',
        'Shorts': 'Clothing',
        'Shrug': 'Clothing',
        'Skirts': 'Clothing',
        'Socks': 'Footwear',
        'Sports Sandals': 'Footwear',
        'Sports Shoes': 'Footwear',
        'Stockings': 'Footwear',
        'Stoles': 'Accessories',
        'Suits': 'Clothing',
        'Sunglasses': 'Accessories',
        'Sunscreen': 'Personal Care',
        'Suspenders': 'Clothing',
        'Sweaters': 'Clothing',
        'Sweatshirts': 'Clothing',
        'Swimwear': 'Clothing',
        'Tablet Sleeve': 'Miscellaneous',
        'Ties': 'Accessories',
        'Ties and Cufflinks': 'Accessories',
        'Tights': 'Clothing',
        'Toner': 'Personal Care',
        'Tops': 'Clothing',
        'Track Pants': 'Clothing',
        'Tracksuits': 'Clothing',
        'Travel Accessory': 'Home and Living',
        'Trolley Bag': 'Home and Living',
        'Trousers': 'Clothing',
        'Trunk': 'Home and Living',
        'Tshirts': 'Clothing',
        'Tunics': 'Clothing',
        'Umbrellas': 'Accessories',
        'Waist Pouch': 'Accessories',
        'Waistcoat': 'Clothing',
        'Wallets': 'Accessories',
        'Watches': 'Accessories',
        'Water Bottle': 'Miscellaneous',
        'Wristbands': 'Accessories'
    },
    'baseColour': {
        'Black': 'Dark',
        'Blue': 'Dark',
        'Beige': 'Light',
        'Brown': 'Dark',
        'Bronze': 'Dark',
        'Burgundy': 'Dark',
        'Charcoal': 'Dark',
        'Coffee Brown': 'Dark',
        'Copper': 'Dark',
        'Cream': 'Neutral',
        'Fluorescent Green': 'Light',
        'Gold': 'Neutral',
        'Green': 'Light',
        'Grey': 'Neutral',
        'Grey Melange': 'Neutral',
        'Khaki': 'Neutral',
        'Lavender': 'Light',
        'Lime Green': 'Light',
        'Magenta': 'Light',
        'Maroon': 'Dark',
        'Mauve': 'Light',
        'Metallic': 'Other',
        'Multi': 'Other',
        'Mushroom Brown': 'Neutral',
        'Mustard': 'Light',
        'Navy Blue': 'Dark',
        'Nude': 'Neutral',
        'Off White': 'Neutral',
        'Olive': 'Light',
        'Orange': 'Light',
        'Peach': 'Light',
        'Pink': 'Light',
        'Purple': 'Light', 
        'Red': 'Dark',
        'Rose': 'Light',
        'Rust': 'Dark',
        'Sea Green': 'Light',
        'Silver': 'Neutral',
        'Skin': 'Neutral',
        'Steel': 'Neutral',
        'Tan': 'Neutral',
        'Taupe': 'Neutral',
        'Teal': 'Light',
        'Turquoise Blue': 'Light',
        'Unknown': 'Other', 
        'White': 'Neutral',
        'Yellow': 'Light'
    },
    'season': {
        'Fall': 'Fall',
        'Winter': 'Winter',
        'Summer': 'Summer',
        'Spring': 'Spring',
        'Unknown': 'Other'
    },
    'usage': {
        'Casual': 'Casual',
        'Ethnic': 'Ethnic',
        'Formal': 'Other',
        'Home': 'Casual',
        'Party': 'Party',
        'Smart Casual': 'Casual',
        'Sports': 'Other',
        'Travel': 'Other',
        'Unknown': 'Other'
    }
}

# Apply aggregations to the dataset
for feature, mapping in aggregations.items():
    data[feature] = data[feature].replace(mapping)

# Display the updated dataset for verification
# print(data[features_to_encode].head())

# Save the modified dataset if needed
data.to_csv("website/datasets/fashion-dataset/agg_styles.csv", index=False)
