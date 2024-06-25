
from flask import Flask, request, jsonify, render_template
from groq import Groq

def generate_answer(question):

    prompt = f"{question}\n\nAnswer this question briefly with example"

    # Initialize the Groq client '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'
    #client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    client = Groq(api_key='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')

    # Create the chat completion request
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    # Extract and return the generated answer
    answer = chat_completion.choices[0].message.content
    return answer

app = Flask(__name__) # Initialize the flask App


@app.route('/', methods=['POST'])
def predict():
    
    question = request.get_json() # {"question" : ".............."}
    
    answer = generate_answer(question['question'])
    
    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)
