from flask import Flask, request
app = Flask(__name__)    # flask application module name.

@app.route('/query_example')    # create the route for query.
def query_example():
    language =  request.args.get('language')  # request object through args.get
    framework = request.args['framework']
    website = request.args.get('website')
    return '''<h1> The Language is : {} </h1>
              <h1> The framework is : {} </h1>
              <h1> The website is : {}  </h1>'''.format(language,framework, website)

@app.route('/form_example', methods=['POST','GET'])     # create the form route with using methods.
def form_example():
    if request.method == 'POST':
        language =  request.form.get('language')
        framework = request.form['framework']
        return '<h1> The language is {}. The framework is {}.</h1>'.format(language,framework)
    return '''<form method="POST" action="">
    Language <input types="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit">
    </form>'''

# run in Postman software.
@app.route('/json_example', methods=['POST'])  # json object code with post methods.
def json_example():
    req_data = request.get_json()

    language = req_data['language']
    framework = req_data['framework']
    python_version = req_data['version_info']['python']
    example = req_data['example'][0]
    boolean_test = req_data['boolean_test']

    return '''<h1>
    The language value is {}.
    The framework value is {}.
    The python version is {}.
    The example at 0 index is {}.
    The boolean value is {}.
    </h1>'''.format(language, framework, python_version, example, boolean_test)
if __name__ == '__main__':
    app.run(debug=True, port=5000)       # use the port 5000.