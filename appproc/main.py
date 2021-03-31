from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    mentor_city = request.args.get('city-name')
    if mentor_city:
        mentor_details = data_manager.get_mentors_by_city(mentor_city)
    elif mentor_name:
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details)


@app.route('/applicants', methods=["GET", "POST"])
def applicants_list():
    applicant_details = data_manager.get_applicants()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('applicants.html', applicants=applicant_details)


@app.route('/applicants/delete_by_email', methods=["GET", "POST"])
def delete_by_email():
    email = request.form.get('delete_by_email_ending').lower()
    print(email)
    data_manager.delete_by_email_ending(email)
    return redirect('/applicants')


@app.route('/add-applicant', methods=["GET", "POST"])
def add_new_applicant():
    if request.method == "POST":
        new_record = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "phone_number": request.form.get("phone_number"),
            "email": request.form.get("email"),
            "application_code": request.form.get("application_code")
        }
        data_manager.add_new_applicant(new_record)
        return redirect("/applicants/" + new_record['application_code'])
    return render_template("add_new_applicant.html")



@app.route('/applicants/<application_code>', methods=["GET", "POST"])
def applicants_edit(application_code):
    applicant_details = data_manager.get_applicants_by_code(application_code)
    if request.method == "POST":
        new_number = request.form.get('phone_number')
        if request.form.get('delete') == 'Delete':
            data_manager.delete_applicant(application_code)
            return redirect('/applicants')
        data_manager.edit_phone_number(new_number, application_code)
        applicant_details = data_manager.get_applicants_by_code(application_code)
    return render_template('applicant-edit.html', applicant=applicant_details)
    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')


@app.route('/applicants-phone')
def applicant_by_name():
    applicant_name = request.args.get('applicant-name')
    applicant_email = request.args.get('email-ending')
    applicants_details = None
    if applicant_email:
        applicants_details = data_manager.get_applicant_data_by_email_ending(applicant_email)
    elif applicant_name:    
        applicants_details = data_manager.get_applicant_data_by_name(applicant_name)
    return render_template('applicants-search.html', applicants=applicants_details)


if __name__ == '__main__':
    app.run(debug=True)
