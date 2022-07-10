from flask import Flask, render_template, jsonify, request, url_for, redirect
import process

# mockup database
# history is a list of question-answer object
history = []

app = Flask(__name__)
app.config['SECRET_KEY'] = '38234023094'

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html', **locals())



@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
	if request.method == "POST":
		the_question = request.form['question']
		if the_question.strip() == '':
			response = 'You do not seem to ask me anything'
		else:
			response = process.chatbot_response(the_question)

		history_item = {
			"question": the_question,
			"answer": response
		}

		history.append(history_item)

	return render_template('index.html', history=history)






if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8888', debug=True)




