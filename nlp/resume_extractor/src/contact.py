import re
#this function extract name, email, phone and location from resume
def extract_contact_info(doc):
    # create dictionary with empty keys 
    info = {"name": None, "email": None, "phone": None, "location": None}
    full_text = doc.text
    lines = [] #empty list 
    
    all_lines = full_text.split('\n') #split return list which has all lines of resumes
    
    for single_line in all_lines:
        #remove extra space if any 
        single_line = single_line.strip()
        if single_line !=None:
            lines.append(single_line)

    # Email theeasylearn@gmail.com
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', full_text)
    if email_match!=None:
        #copy email address from email_match into info['email']
        info["email"] = email_match.group()

    # Phone
    phone_match = re.search(r'(\+91|0)?[\s-]?(\d{10})', full_text)
    if phone_match!=None:
        #copy phone from phone match into phone
        info["phone"] = phone_match.group(2)

    # NAME - Take first line (most reliable for real resumes)
    if lines:
        name_line = lines[0]
        # remove phone and email from name line if they are on same line
        name_line = re.sub(r'(\+91|0)?[\s-]?\d{10}','',name_line)
        name_line = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', name_line)
        info["name"] = name_line.strip()
    return info