# чтение данных json с помощью ф-ии loads()
string_json_data = '{"name": "Zophie", "is_cat": true, "mice_caught": 0, "feline_IQ": null}'

import json

json_data_python_value = json.loads(string_json_data)
print(json_data_python_value)

python_value = '{"name": "Zophie", "is_cat": true, "mice_caught": 0, "feline_IQ": null}'

json_data_python_value2 = json.dumps(python_value)
print(json_data_python_value2)