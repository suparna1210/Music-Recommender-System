from flask import Flask, request
app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    client_id = request.form['client-id']
    client_secret = request.form['client-secret']
    mind = request.form['mind']
    memorable = request.form['memorable']
    sleeping = request.form['sleeping']
    challenging = request.form['challenging']
    advice = request.form['advice']
    
    # Call your sentiment analysis function here and pass in the form data as arguments
    print(client_id, client_secret, mind, memorable, sleeping, challenging, advice)

    # return 'Sentiment analysis complete.'
if __name__ == '__main__':
    app.run(debug=True)