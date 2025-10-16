from flask import Flask, request, jsonify, render_template
from dora.persona.basic import BasicPersona, get_text_from_response
import logging


persona = BasicPersona(name="TestUser", description="A test user persona.")
app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route('/chat-ui')
def chat_ui():
    return render_template('chat.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print(f"User message: {user_message}")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    response = persona.request_w_tools(user_message)
    resp_text = get_text_from_response(response)
    # print(json.dumps(response, indent=4))
    return jsonify({
        "response": resp_text
    })


if __name__ == '__main__':
    app.run(debug=True)
