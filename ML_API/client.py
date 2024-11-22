# # inference script

# import json
# import requests

# # Define the API endpoint
# url = "http://127.0.0.1:8000/predict"

# # Mock data to send to the API
# data = [
#     {
#         "availability": "Ready to move in",
#         "total_sqft": 1500.0,
#         "bath": 2,
#         "balcony": 1,
#         "BHK": 3,
#         "area_type_Carpet_Area": True,
#         "area_type_Plot_Area": False,
#         "area_type_Super_built_up_Area": False
#     },
#     {
#         "availability": "17-May",
#         "total_sqft": 2000.0,
#         "bath": 3,
#         "balcony": 2,
#         "BHK": 4,
#         "area_type_Carpet_Area": False,
#         "area_type_Plot_Area": True,
#         "area_type_Super_built_up_Area": False
#     }
# ]

# # Initialize a list to store predictions
# predictions = []

# # Loop through each record and send a POST request
# for record in data:
#     try:
#         # Convert the record to JSON
#         payload = json.dumps(record)

#         # Send a POST request
#         response = requests.post(url, data=payload, headers={"Content-Type": "application/json"})

#         # Check if the response status code is 200 (OK)
#         if response.status_code == 200:
#             # Parse the JSON response
#             predicted_price = response.json().get("predicted_price")
#             predictions.append(predicted_price)
#         else:
#             # Handle error response
#             print(f"Error: Received status code {response.status_code}")
#             print("Response:", response.text)

#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Print all predictions
# print("Predicted Prices:", predictions)
