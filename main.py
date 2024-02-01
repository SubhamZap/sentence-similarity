from flask import Flask, request
from predict import convert_sen_to_vec, cosine

app = Flask(__name__)

@app.route('/')
def demo():
    return 'You can calculate similarity score of two sentences by redirecting to ---> http://127.0.0.1:5000/score'

@app.route('/score', methods = ['POST'])
def evaluate_sim_score():
    data = request.get_json()
    if 'text1' in data and 'text2' in data:
        text1 = data['text1']
        text2 = data['text2']
        text1_emb = convert_sen_to_vec(text1)
        text2_emb = convert_sen_to_vec(text2)
        score = cosine(text1_emb, text2_emb)
        response = {'similarity_score': score}
        return response

if __name__ == "__main__":
    app.run(debug=True)