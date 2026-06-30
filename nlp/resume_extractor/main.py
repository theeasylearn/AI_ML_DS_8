import os
import sys

# Add current directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.extractor import extract_resume
from src.pdf_handler import extract_text_from_pdf
import json

def main():
    print("=== Resume Information Extractor ===\n")
    
    # Create folders
    os.makedirs("data/samples", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    sample_dir = "data/samples"
    files = [f for f in os.listdir(sample_dir) if f.endswith(('.txt', '.pdf'))]
    
    if not files:
        print("❌ No resume files found in 'data/samples/' folder.")
        print("Please add at least one .txt or .pdf resume.")
        print("\nYou can also try the web app:")
        print("   streamlit run app.py")
        return
    
    print(f"Found {len(files)} resume(s). Starting extraction...\n")
    
    for filename in files:
        filepath = os.path.join(sample_dir, filename)
        
        try:
            if filename.lower().endswith('.pdf'):
                print(f"📄 Processing PDF: {filename}")
                text = extract_text_from_pdf(filepath)
            else:
                print(f"📝 Processing TXT: {filename}")
                with open(filepath, "r", encoding="utf-8") as f:
                    text = f.read()
            
            result = extract_resume(text, filename)
            
            output_filename = filename.rsplit('.', 1)[0] + "_extracted.json"
            output_path = os.path.join("output", output_filename)
            
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            
            print(f"✅ Success: {filename}")
            print(f"   → Saved to: {output_path}\n")
            
        except Exception as e:
            print(f"❌ Error with {filename}: {e}\n")
    
    print("🎉 Processing completed! Check the 'output' folder.")

if __name__ == "__main__":
    main()