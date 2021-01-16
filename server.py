from flask import Flask, jsonify,request
from translation import trans

app = Flask(__name__)

@app.route('/v2/translate', methods=['POST'])
def post():
    try:
        text = request.form.get('text')
        print(f">> Sending requests: {text}")

        MAX_LENGTH = 5000
        if len(text) <= MAX_LENGTH:
            result = trans(text.encode("utf-8"))
        else:
            text_list = [
                text[i:i + MAX_LENGTH] for i in range(0, len(text), MAX_LENGTH)
            ]
            result = [trans_list_item(text) for text in text_list]
            result = " ".join(result)
        print(f"<< Succeed: {result[:50]}...")
        json = {
            "translations": [{
                "detected_source_language": "EN",
                "text": f"{result}"
            }]
        }
        result = jsonify(json)
        return result
    except Exception as e:
        print(e)
        return f"Error: {e}"


def trans_list_item(text):
    print(f"  -> Handling: {text[:50]}...")
    result = trans(text.encode("utf-8"))
    print(f"  <- Succeed: {result[:50]}...")
    return result


if __name__ == '__main__':
    app.run(port=1337, debug=False)
