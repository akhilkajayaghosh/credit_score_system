from flask import Flask, redirect, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=="POST":
        accounts = request.form.get('acc')
        education = request.form.get('Edu')
        employ=request.form.get('emp')
        # credit_score = (payment_history * 0.35) + (credit_utilization_ratio*0.30)+(accounts*0.15)+(education*0.10)+(employ* 0.10)
        return (f"Accounts: {accounts}, Education: {education},Employment:{employ}")
# Define other routes and backend logic as needed

if __name__ == '__main__':
    app.run(debug=True)