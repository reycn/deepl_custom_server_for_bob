from pypt import trans
from sanic import Sanic
from sanic.response import json

app = Sanic("DeepL API")

@app.route('/v2/translate', methods=["GET"])
async def get_translate(request, lang_tgt='EN', lang_src='ZH'):
    if request.args.get('lang_tgt'):
        lang_tgt = request.args.get('lang_tgt')
    if request.args.get('lang_src'):
        lang_src = request.args.get('lang_src')
    if request.args.get('text'):
        text_to_translate = request.args.get('text')
        print(f'>> Request: {text_to_translate}')
        result = await trans(text_to_translate, lang_tgt=lang_tgt, lang_src=lang_src)
        print(f'<< Response: {result}')
    else:
        result = "未找到需要翻译的词句 Text to translate not found"
        print(">> Request error: Text not found")
    return json(text_to_dict(result, lang_src))

@app.route('/v2/translate', methods=["POST"])
async def post_translate(request, lang_tgt='EN', lang_src='ZH'):
    if request.form.get('lang_tgt'):
        lang_tgt = request.form.get('lang_tgt')
    if request.form.get('lang_src'):
        lang_src = request.form.get('lang_src')
    if request.body:
        text_to_translate = request.form.get('text')
        print(f'>> Request: {text_to_translate}')
        result = await trans(text_to_translate, lang_tgt=lang_tgt, lang_src=lang_src)
        print(f'<< Response: {result}')
    else:
        result = "未找到需要翻译的词句 Text to translate not found"
        print(">> Request error: Text not found")
    return json(text_to_dict(result, lang_src))

def text_to_dict(string, lang_src):
    dct = {"translations":[{  "detected_source_language": lang_src,"text": string}]}
    return dct


app.run(host="0.0.0.0", port=1337)