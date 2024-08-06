from flask import Flask, request, jsonify
import google.generativeai as genai  # type: ignore


api_key = "AIzaSyDeNQRz13E3kflC6GPjInunOZcKjN4UCiE"


genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    
    data = request.get_json()

    source_lang = data.get('source')
    source_text = data.get('text')
    target_lang = data.get('target')

   
    prompt = f"tranclate source language to traget lanugage  but always give text in roman(english) script and also dont print any extra word just give tranclated text     source {source_lang}:  {source_text}  : {target_lang} give me response in roman(english) script only"

    response = model.generate_content(prompt)
    translated_text = response.text.strip()

   
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
