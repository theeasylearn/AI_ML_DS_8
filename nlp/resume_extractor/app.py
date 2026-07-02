import streamlit as st
import os 
import sys 

# Add project root to path

#has path of this file (app.py)
current_file_path = os.path.abspath(__file__)
#path of the directory which has app.py file 
project_root = os.path.dirname(current_file_path)
#add path so that python will search this path for modules
sys.path.insert(0, project_root)

from src.extractor import extract_resume
from src.pdf_handler import extract_text_from_pdf
import json #(python built in module json )

#set title and layout of the website 
st.set_page_config(page_title="Resume Extractor", layout="wide")

#set heading of page 
st.title("Resume Information Extractor")
#set description below heading 
st.markdown("Upload your resume (PDF or TXT)")

#create button to upload resume 
label = "Choose file"
uploaded_file = st.file_uploader(label, type=["pdf", "txt"])

#if user has selected valid file
if uploaded_file is not None:
    #create variable to store file temporary 
    temp_path = f"temp_{uploaded_file.name}"
    mode = "wb" #write binary
    with open(temp_path,mode) as file:
        #write content of uploaded file into temporary file 
        FileContent = uploaded_file.getbuffer()
        file.write(FileContent)
    
        #check file type
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(temp_path)
        else:
            text = uploaded_file.read().decode("utf-8")
        
        #display message on screen
        st.success("File processed successfully!")
        
        with st.spinner("Extracting data..."):
            result = extract_resume(text, uploaded_file.name)
        
        st.subheader("Contact Info")
        contact = result["contact"]

        st.write(f"**Name:** {contact.get('name') or 'Not found'}")
        st.write(f"**Email:** {contact.get('email') or 'Not found'}")
        st.write(f"**Phone:** {contact.get('phone') or 'Not found'}")
        
        st.subheader("Skills")
        st.write(", ".join(result.get("skills", [])) or "No skills found")
        
        # Education
        st.subheader("🎓 Education")
        edu_list = result.get("education", [])
        if edu_list:
            for edu in edu_list:
                if isinstance(edu, dict):
                    deg = edu.get("degree") or ""
                    yr = edu.get("year") or ""
                    pct = edu.get("percentage") or ""
                    parts = [p for p in [deg, yr, pct] if p]
                    line = " | ".join(parts) if parts else str(edu)
                else:
                    line = str(edu)
                # prevent extremely long repeated text in UI
                if len(line) > 220:
                    line = line[:217] + "..."
                st.write(f"• {line}")
        else:
            st.write("No education details found")

        st.subheader("💼 Experience")
        exp_list = result.get("experience", [])
        if exp_list:
            for exp in exp_list:
                if isinstance(exp, dict):
                    desc = exp.get("description", "")
                    dur = exp.get("duration") or ""
                    if dur:
                        st.write(f"• {desc}  \n  _({dur})_")
                    else:
                        st.write(f"• {desc}")
                else:
                    st.write(f"• {exp}")
        else:
            st.write("No experience found")

        # Certifications
        st.subheader("📜 Certifications")
        certs = result.get("certifications", [])
        if certs:
            for cert in certs:
                c = str(cert)
                if len(c) > 200:
                    c = c[:197] + "..."
                st.write(f"• {c}")
        else:
            st.write("No certifications found")
            
        json_str = json.dumps(result, indent=2)
        st.download_button("Download JSON", json_str, "result.json", "application/json")
        #delete temporary file 
        # if os.path.exists(temp_path):
        #     os.remove(temp_path)