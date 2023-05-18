# Pytho Program To convert Python Object to JSON Object.
import json
data = {'Name': 'Deepak', 'Age': 26, 'Technology': 'Python Developer'}
json_Object = json.dumps(data)

# To convert JSON object to Python Object, we use Loads method.