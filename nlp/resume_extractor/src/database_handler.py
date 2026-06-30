import json

import mysql.connector as connector
from datetime import datetime

def store_data_into_database(result):
    print("Function called...")
    
    try:
        # Database Connection
        database = connector.connect(
            host='localhost',
            user='root',
            passwd='',           # Add your password if any
            database='ai_ml_ds_5',
            port='3306'
        )
        cursor = database.cursor()
        print('✅ Database connection created successfully!')

        # 1. Insert into main resumes table
        insert_resume = "INSERT INTO resumes (filename, extracted_at, raw_json) VALUES (%s, %s, %s)"
        extracted_at = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute(insert_resume, (result.get('filename'),extracted_at,json.dumps(result)))
        
        resume_id = cursor.lastrowid  # Get the auto-generated ID
        print(f"Resume inserted with ID: {resume_id}")

        # 2. Insert Contact Information
        contact = result.get('contact', {})
        insert_contact = """
            INSERT INTO resume_contact (resume_id, name, email, phone, location)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_contact, (
            resume_id,
            contact.get('name'),
            contact.get('email'),
            contact.get('phone'),
            contact.get('location')
        ))
        print("Contact info stored")

        # 3. Insert Skills
        skills = result.get('skills', [])
        if skills:
            insert_skill = "INSERT INTO resume_skills (resume_id, skill) VALUES (%s, %s)"
            skill_values = [(resume_id, skill) for skill in skills]
            cursor.executemany(insert_skill, skill_values)
            print(f"{len(skills)} skills stored")

        # 4. Insert Education
        education_list = result.get('education', [])
        if education_list:
            insert_edu = """
                INSERT INTO resume_education 
                (resume_id, degree, institution, year)
                VALUES (%s, %s, %s, %s)
            """
            edu_values = []
            for edu in education_list:
                if isinstance(edu, dict) == True:
                    edu_values.append((
                        resume_id,
                        edu.get('degree'),
                        edu.get('institution'),
                        edu.get('year')
                    ))
                else:
                    edu_values.append((resume_id, str(edu), None, None))
            
            cursor.executemany(insert_edu, edu_values)
            print(f"✅ {len(edu_values)} education records stored")

        # 5. Insert Experience
        experience_list = result.get('experience', [])
        if experience_list:
            insert_exp = """
                INSERT INTO resume_experience 
                (resume_id, job_title, company, duration, description)
                VALUES (%s, %s, %s, %s, %s)
            """
            exp_values = []
            for exp in experience_list:
                if isinstance(exp, dict) == True:
                    exp_values.append((
                        resume_id,
                        exp.get('job_title') or exp.get('position'),
                        exp.get('company'),
                        exp.get('duration'),
                        exp.get('description')
                    ))
                else:
                    exp_values.append((resume_id, None, None, None, str(exp)))
            
            cursor.executemany(insert_exp, exp_values)
            print(f"✅ {len(exp_values)} experience records stored")

        # 6. Insert Certifications
        certifications = result.get('certifications', [])
        if certifications:
            insert_cert = """
                INSERT INTO resume_certifications 
                (resume_id, certification_name, issuing_org, year)
                VALUES (%s, %s, %s, %s)
            """
            cert_values = [(resume_id, cert, None, None) for cert in certifications]
            cursor.executemany(insert_cert, cert_values)
            print(f"✅ {len(certifications)} certifications stored")

        # Commit all changes
        database.commit()
        print("🎉 All resume data stored successfully!")

    except connector.Error as e:
        print('❌ Database Error occurred:')
        print(f"Error Code: {e.errno}")
        print(f"Message: {e.msg}")
        if database:
            database.rollback()
        
    except Exception as e:
        print('❌ Unexpected Error:', str(e))
        if database:
            database.rollback()
    
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'database' in locals() and database.is_connected():
            database.close()
            print("🔌 Database connection closed.")