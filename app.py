from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def qr_generator():
    return render_template('qr_generator.html')

@app.route('/complaint', methods=['GET', 'POST'])
def complaint_form():
    if request.method == 'POST':
        # Handle complaint submission
        issue = request.form.get('issue')
        location = request.form.get('location')
        image = request.files.get('image')  # Use this to save the image
        pole_no = request.args.get('poleNo')
        pole_area = request.args.get('poleArea')
        pole_location = request.args.get('poleLocation')
        
        # For simplicity, we print the data (save to DB or process as needed)
        print(f"Complaint submitted: Issue={issue}, Location={location}, Pole={pole_no}, {pole_area}, {pole_location}")
        
        return "Complaint Submitted Successfully!"  # Redirect or display a success page
    return render_template(
        'complaint_form.html',
        poleNo=request.args.get('poleNo'),
        poleArea=request.args.get('poleArea'),
        poleLocation=request.args.get('poleLocation')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
