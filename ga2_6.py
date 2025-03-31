from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# # Define the path to the JSON file
# json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')

# print(json_file_path)
# # Load student marks from the JSON file
# def load_student_marks():
#     try:
#         with open(json_file_path, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return [{"name": "Default", "marks": 0}] 

STUDENT_DATA = [{"name":"XWffjMi","marks":58},{"name":"sFsz6PGOBc","marks":49},{"name":"hDjH","marks":67},{"name":"ZYVsM4C","marks":60},{"name":"pcVLV","marks":90},{"name":"pAf2HuL5y","marks":54},{"name":"rB8","marks":28},{"name":"oB322","marks":58},{"name":"gpR","marks":32},{"name":"D0MCPnS4MY","marks":26},{"name":"iC1drl83i","marks":33},{"name":"WZslEYo0n0","marks":68},{"name":"CCuEEw","marks":85},{"name":"GQMQ5hpTUx","marks":60},{"name":"N28Q","marks":71},{"name":"varEZRKowz","marks":45},{"name":"9eY","marks":89},{"name":"ch","marks":17},{"name":"9Wcim0pwH","marks":9},{"name":"aNxeZ","marks":34},{"name":"ay","marks":80},{"name":"s3sRx","marks":22},{"name":"3Vg1G0O08J","marks":88},{"name":"WFL2Lk","marks":32},{"name":"i7oigK","marks":10},{"name":"7Oy6D","marks":5},{"name":"ycwLXUX","marks":68},{"name":"wO2K","marks":0},{"name":"DBrMgB69","marks":44},{"name":"WtZPp","marks":77},{"name":"252bb","marks":35},{"name":"Onq02","marks":17},{"name":"L7y","marks":92},{"name":"Ndls8W6vb","marks":74},{"name":"Rp9sFZVzH","marks":90},{"name":"Pg","marks":76},{"name":"9ZZhjYE","marks":92},{"name":"f54J","marks":46},{"name":"8tUohDRN5y","marks":36},{"name":"v3P6VWPA","marks":68},{"name":"P7H","marks":13},{"name":"lZE94UNb","marks":0},{"name":"jnbKLzvCc","marks":41},{"name":"Bsv4w","marks":25},{"name":"WcN","marks":85},{"name":"1Y","marks":23},{"name":"UysqwZ","marks":2},{"name":"Kwd9W","marks":94},{"name":"429cab","marks":20},{"name":"meR11","marks":6},{"name":"A3","marks":1},{"name":"T6","marks":95},{"name":"v","marks":42},{"name":"Rw0n","marks":56},{"name":"21ncW","marks":15},{"name":"I9mzUWo4","marks":65},{"name":"FJH","marks":66},{"name":"Gk","marks":84},{"name":"Dr5i","marks":23},{"name":"DEq7","marks":31},{"name":"dXbH5lc","marks":71},{"name":"8n5uaRNkDa","marks":67},{"name":"YvKEQ","marks":65},{"name":"BA2buyM","marks":92},{"name":"HTwGOKRXFd","marks":64},{"name":"EgAE29DRV","marks":83},{"name":"EwESdNADx","marks":54},{"name":"Ks83","marks":87},{"name":"2ymYS0","marks":86},{"name":"coNWVwT","marks":66},{"name":"zz9qeYuv5","marks":1},{"name":"Gq","marks":45},{"name":"Ys01j","marks":92},{"name":"Invf","marks":63},{"name":"tQ8Q9CuM","marks":24},{"name":"P","marks":72},{"name":"f4j56","marks":42},{"name":"B4rbCh","marks":18},{"name":"whiS","marks":19},{"name":"1f6xQ","marks":86},{"name":"ldpA","marks":91},{"name":"36S8nM","marks":5},{"name":"lkhXo","marks":80},{"name":"ktPOwb6i","marks":25},{"name":"i","marks":88},{"name":"KYL8AAPJ","marks":57},{"name":"jsy","marks":38},{"name":"Akp","marks":58},{"name":"7e0dvmT","marks":30},{"name":"2","marks":4},{"name":"UGrMeSOd17","marks":14},{"name":"PRdU8","marks":20},{"name":"Lx","marks":65},{"name":"jdp5Qma","marks":90},{"name":"xpf3qSFwy","marks":95},{"name":"K1","marks":57},{"name":"gjB","marks":17},{"name":"W2bTMgz7G","marks":89},{"name":"BXc1APlt","marks":41},{"name":"ufjnhT","marks":80}]
def load_student_marks():
    return STUDENT_DATA
@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from the query string
    names = request.args.getlist('name')
    student_marks = load_student_marks()

    # Look for the student marks in the list of dictionaries
    marks = []
    for name in names:
        # Search for the student's mark based on the name
        student = next((item for item in student_marks if item["name"] == name), None)
        
        if student:
            marks.append(student["marks"])
        else:
            marks.append(0)

    return jsonify({"marks": marks})

# if __name__ == '__main__':
#     app.run(debug=True)
