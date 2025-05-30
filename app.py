from flask import Flask, render_template, jsonify, request
from database import *

app = Flask(__name__)

# JOBS = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 10,00,000'
#     },
#     {
#         'id': 2,
#         'title': 'Data Engineer',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 12,00,000'
#     },
#     {
#         'id': 3,
#         'title': 'Data Analyst',
#         'location': 'Bengaluru, India',
#
#     },
#     {
#         'id': 4,
#         'title': 'AI Engineer',
#         'location': 'Bengaluru, India',
#         'salary': 'Rs. 25,00,000'
#     },
#
# ]

@app.route("/")
def hello_aiworld():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def job_page(id):
    job = load_single_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
    data = request.form
    job = load_single_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)