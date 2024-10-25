import base64 
import json 
 
def image_to_json(image_path): 
    # Step 1: Read the image file 
    with open(image_path, "rb") as image_file: 
        # Step 2: Encode the image to Base64 
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8') 
    # Step 3: Create a JSON object 
    json_data = { 
        "image_data": encoded_string 
    }      
    return json.dumps(json_data) 
 
# Usage 
image_path = 'C:/Users/BLAUPLUG/Documents/Python_programs/json/tiger.jpg' 
json_output = image_to_json(image_path) 
print(json_output) 
