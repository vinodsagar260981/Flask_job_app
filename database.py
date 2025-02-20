import sqlalchemy
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()


# print(sqlalchemy.__version__)
db_connection_string = os.getenv('DB_RENDER_PASSWORD')

engine = create_engine(db_connection_string)

# print(engine)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        print("type(result):", type(result))

        jobs = []
        keys = ['id', 'title', 'location', 'salary', 'currency', 'responsibilities', 'skills']

        for row in result.all():
            jobs.append(dict(zip(keys, row)))

        # print(result_dicts)
        return jobs

def load_single_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id= :val"), {'val': id})

        rows = result.all()
        keys = ['id', 'title', 'location', 'salary', 'currency', 'responsibilities', 'skills']
        if len(rows) == 0:
            return None
        else:
            return dict(zip(keys, rows[0]))


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, likedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :likedin_url, :education, :work_experience, :resume_url)")

        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'likedin_url': data['likedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })

        conn.commit()




    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result_all):", type(result_all))
    # print("result_all: ", result_all)
    # first_result = result_all[0]
    # print("type(first_result):", type(first_result))
    #
    # keys = ['id', 'job_title', 'location', 'salary', 'currency', 'responsibilities', 'skills']
    # first_result_dict = dict(zip(keys, result_all[0]))
    # print("type(first_result_dict) : ", type(first_result_dict))
    # print(first_result_dict)
