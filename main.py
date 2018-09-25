from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px 'Tahoma';
                color: hotpink;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                font-family: 'Tahoma';
                font-size: 14px;
                color: hotpink;
            }}

            .button {{
                background-color: hotpink;
                border: 1px solid hotpink;
                border-radius: 10%;
                color: white;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 14px;
                font: 'Tahoma';
            }}      
        </style>
    </head>
    <body>
      <form method="post">
            <label for="rot"><strong> Rotate by:</strong> 
            </label> 
                <input type="text" name="rot" value="0" /> 
        
                <p>
                <textarea name="text">{0}</textarea>       
        
                <p>
                <input type="submit" class="button" value="Submit" />
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    empty = ""
    return form.format(empty)

@app.route("/", methods=['POST'])
def encrypt():
    input_rot = int(request.form['rot'])
    input_text = request.form['text']
    txt_encripted = rotate_string(input_text, input_rot)
    return form.format(txt_encripted)

app.run()