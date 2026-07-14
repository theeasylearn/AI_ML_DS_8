# ============================================================
# EasyLearn Academy - Comprehensive Knowledge Base with Topic Priorities
# ============================================================
# 
# Topics are arranged in PRIORITY ORDER (Highest → Lowest)
#
# HOW TO USE:
# When a user query matches keywords from multiple topics,
# the topic with the LOWER priority number wins.
# (1 = Highest priority)
#
# UPDATED:
# - Dedicated high-priority topics (priority 3) for each specific course
#   with duration, timings, fees, and detailed syllabus topics.
# - General fees_and_duration moved to priority 4 (fallback only).
# - Specific course answers are given first when relevant keywords match.
# ============================================================

knowledge = {
    'topics': {
        # ─────────────────────────────────────────────
        # Priority 1: CONTACT (Highest)
        # ─────────────────────────────────────────────
        'contact': {
            'priority': 1,
            'keywords': ['contact', 'reach', 'call', 'phone', 'number', 'email', 'whatsapp', 'message', 'enquiry', 'inquiry', 'get in touch', 'help', 'connect', 'talk', 'speak', 'chat', 'customer care', 'helpline', 'toll free', 'reach out', 'how to contact', 'contact details', 'social media', 'facebook', 'instagram', 'linkedin', 'website', 'mobile no', 'email address', 'what is your email', 'what is your mobile','mobile'],
            'answer': """You can reach us at Eva Surbhi Mall, 105, Waghawadi Road, opposite Aksharwadi Temple, Bhavnagar, Gujarat - 364002. 
            Phone/WhatsApp: 9662512857
            Website: https://theeasylearnacademy.com/
            We are available Monday to Saturday, 9 AM to 7 PM. Feel free to call or WhatsApp for quick enquiry!"""
        },

        # ─────────────────────────────────────────────
        # Priority 2: LOCATION (Very High)
        # ─────────────────────────────────────────────
        'location': {
            'priority': 2,
            'keywords': ['location', 'address', 'where', 'place', 'situated', 'find you', 'directions', 'how to reach', 'map', 'navigate', 'office', 'city', 'state', 'gujarat', 'bhavnagar', 'visit', 'near', 'landmark', 'pincode', 'area', 'road', 'mall', 'institute location', 'academy location', 'institute address', 'academy address', 'where is institute', 'where is academy', 'institute', 'class'],
            'answer': """We are located at Eva Surbhi Mall, 105, Waghawadi Road, opposite Aksharwadi Temple, Bhavnagar, Gujarat - 364002. 
You can visit us Monday to Saturday, 9 AM to 7 PM. Check our website for Google Maps link: https://theeasylearnacademy.com/"""
        },

        # ─────────────────────────────────────────────
        # Priority 3: SPECIFIC COURSES (High Priority)
        # Each course has its own dedicated topic so specific queries are answered first
        # ─────────────────────────────────────────────

        # Python Course
        'python_course': {
            'priority': 3,
            'keywords': ['python course', 'python syllabus', 'python details', 'python duration', 'python fees', 'python topics', 'learn python', 'python training', 'python class', 'python batch', 'python program', 'python full course', 'python programming', 'python for beginners','python'],
            'answer': """Python Course (Job-Oriented)
• Duration: 3 months
• Timings: 2 hours per session
• Fees: ₹7500 (EMI available)

Comprehensive Topics:
• Python Fundamentals (Variables, Data Types, Operators, Input/Output)
• Control Flow (if-else, loops)
• Functions, Modules & Packages
• Strings, Lists, Tuples, Dictionaries, Sets
• File Handling & Exception Handling
• Object-Oriented Programming (OOP)
• Introduction to Libraries (NumPy, Pandas)
• Mini Projects: Calculator, File Manager, Simple Games, Data Analysis scripts

Perfect for beginners aiming for software development or data roles. Includes live projects and certificate."""
        },

        # MERN Full Stack
        'mern_course': {
            'priority': 3,
            'keywords': ['mern course', 'mern stack', 'mern syllabus', 'mern details', 'mern duration', 'mern fees', 'full stack mern', 'react node course', 'mern training', 'mern full stack development'],
            'answer': """MERN Full Stack Development
• Duration: 6 months
• Timings: 2 hours per session
• Fees: ₹25000 (EMI available)

Comprehensive Topics:
• HTML5, CSS3, Responsive Design & Bootstrap
• JavaScript ES6+ (Variables, Functions, Promises, Async/Await)
• React.js (Components, JSX, Hooks, State Management, Routing, Redux)
• Node.js & Express.js (Backend Development, REST APIs, Middleware)
• MongoDB (Database Design, CRUD Operations, Aggregation, Mongoose)
• Authentication & Authorization (JWT, Sessions)
• Full-Stack Integration Projects
• Deployment (Render, Netlify, Vercel)
• Capstone Project: E-commerce / Social Media App

Become a complete Full Stack Developer. Includes live projects & placement assistance."""
        },

        # AI/ML Course
        'ai_ml_course': {
            'priority': 3,
            'keywords': ['ai ml course', 'ai course', 'ml course', 'artificial intelligence course', 'machine learning course', 'ai syllabus', 'ml syllabus', 'ai fees', 'ai duration', 'ai ml training'],
            'answer': """AI & Machine Learning Course
• Duration: 8 months
• Timings: 2 hours per session
• Fees: ₹40000 (EMI available)

Comprehensive Topics:
• Python for Data Science & ML
• Data Preprocessing, Cleaning & Visualization (Pandas, Matplotlib, Seaborn)
• Statistics & Probability for ML
• Supervised Learning (Regression, Classification - Linear, Logistic, Decision Trees, Random Forest, SVM)
• Unsupervised Learning (Clustering - K-Means, Hierarchical)
• Neural Networks & Deep Learning basics
• TensorFlow / Keras for building models
• Model Evaluation, Hyperparameter Tuning
• Real-world Projects: Image Classifier, House Price Prediction, Chatbot basics
• Deployment of ML Models

Ideal for students wanting careers in AI/ML/Data roles. Strong practical focus with projects."""
        },

        # Data Science
        'data_science_course': {
            'priority': 3,
            'keywords': ['data science course', 'data science syllabus', 'data science fees', 'data science duration', 'data science training'],
            'answer': """Data Science Course
• Duration: 8 months
• Timings: 2 hours per session
• Fees: ₹41000 (EMI available)

Comprehensive Topics:
• Statistics, Probability & Linear Algebra
• Python/R for Data Analysis
• Data Visualization (Tableau/Power BI basics + Python libraries)
• Data Wrangling & ETL
• Machine Learning Fundamentals
• SQL & Database Management
• Big Data Concepts (Introduction to Spark/Hadoop)
• Predictive Modeling & Time Series
• Capstone Projects & Business Case Studies
• Dashboard Creation & Storytelling with Data

Prepare for Data Analyst / Data Scientist roles with hands-on projects."""
        },

        # Cyber Security
        'cyber_security_course': {
            'priority': 3,
            'keywords': ['cyber security','cyber security course', 'cybersecurity syllabus', 'ethical hacking course', 'cyber security fees', 'cyber security duration'],
            'answer': """Cyber Security Course
• Duration: 8 months
• Timings: 2 hours per session
• Fees: ₹42000 (EMI available)

Comprehensive Topics:
• Networking Fundamentals & Protocols
• Operating Systems Security (Linux/Windows)
• Ethical Hacking & Penetration Testing
• Kali Linux Tools (Nmap, Metasploit, Wireshark, Burp Suite)
• Web Application Security & OWASP Top 10
• Cryptography & Encryption
• Malware Analysis basics
• Incident Response & Forensics
• Secure Coding Practices
• Real Projects & CTF Challenges

Build skills for Cybersecurity Analyst / Ethical Hacker roles."""
        },

        # Flutter Mobile App Development
        'flutter_course': {
            'priority': 3,
            'keywords': ['flutter','flutter course', 'flutter syllabus', 'flutter details', 'flutter duration', 'flutter fees', 'mobile app development flutter', 'flutter training'],
            'answer': """Flutter Mobile App Development
• Duration: 6 months
• Timings: 2 hours per session
• Fees: ₹25000 (EMI available)

Comprehensive Topics:
• Dart Programming Language Fundamentals
• Flutter Widgets, Layouts & Navigation
• State Management (Provider, Riverpod, Bloc)
• Firebase Integration (Auth, Firestore, Storage)
• REST API Integration & JSON Parsing
• Responsive & Adaptive UI Design
• Animations & Custom Widgets
• App Deployment (Play Store & App Store)
• Capstone Project: Full-featured Mobile App (e.g., E-commerce, Social App)

Become a cross-platform mobile developer with one codebase."""
        },

        # Digital Marketing
        'digital_marketing_course': {
            'priority': 3,
            'keywords': ['digital marketing','digital marketing course', 'digital marketing syllabus', 'digital marketing fees', 'seo course', 'social media marketing course'],
            'answer': """Digital Marketing Course
• Duration: 6 months
• Timings: 2 hours per session
• Fees: ₹25000 (EMI available)

Comprehensive Topics:
• Digital Marketing Fundamentals & Strategy
• SEO (On-page, Off-page, Technical)
• Google Ads & PPC Campaigns
• Social Media Marketing (Facebook, Instagram, LinkedIn, YouTube)
• Content Marketing & Copywriting
• Email Marketing & Automation
• Analytics & Google Analytics 4
• Affiliate Marketing & Influencer Marketing
• Campaign Planning & ROI Measurement
• Live Projects & Client Campaigns

Perfect for marketing careers or business owners wanting to grow online presence."""
        },

        # C Programming
        'c_course': {
            'priority': 3,
            'keywords': ['c course', 'c programming', 'c syllabus', 'c language course', 'learn c programming'],
            'answer': """C Programming Course
• Duration: 1.5 months
• Timings: 2 hours per session
• Fees: ₹4500

Comprehensive Topics:
• C Fundamentals & History
• Data Types, Variables, Constants, Operators
• Input/Output (printf, scanf)
• Control Structures (if, switch, loops)
• Functions & Recursion
• Arrays & Strings
• Pointers & Memory Management
• Structures & Unions
• File Handling
• Mini Projects

Strong foundation for system programming and competitive coding."""
        },

        # C++ Programming
        'cpp_course': {
            'priority': 3,
            'keywords': ['c++','c++ course', 'cpp course', 'c plus plus', 'c++ syllabus', 'learn c++', 'c++ programming'],
            'answer': """C++ Programming Course
• Duration: 1.5 months
• Timings: 2 hours per session
• Fees: ₹4500

Comprehensive Topics:
• C++ Basics & Differences from C
• OOP Concepts (Classes, Objects, Inheritance, Polymorphism, Encapsulation, Abstraction)
• Constructors & Destructors
• Operator Overloading
• Templates & STL (Standard Template Library)
• Exception Handling
• File I/O
• Pointers & Dynamic Memory
• Mini Projects

Ideal for game development, competitive programming, and software engineering foundation."""
        },

        # Java Programming
        'java_course': {
            'priority': 3,
            'keywords': ['java','java course', 'java syllabus', 'java programming', 'core java', 'java training'],
            'answer': """Java Programming Course
• Duration: 3 months
• Timings: 2 hours per session
• Fees: ₹7500

Comprehensive Topics:
• Java Fundamentals & JVM
• Data Types, Variables, Operators
• Control Flow & Loops
• OOP in Java (Classes, Inheritance, Interfaces, Abstract Classes)
• Exception Handling
• Collections Framework (List, Set, Map)
• Multithreading basics
• File Handling & JDBC basics
• Mini Projects & GUI intro (Swing/JavaFX)

Strong base for Android development, enterprise applications, and backend roles."""
        },

        # CCC (Course on Computer Concepts)
        'ccc_course': {
            'priority': 3,
            'keywords': ['ccc','ccc course', 'ccc syllabus', 'ccc details', 'course on computer concepts', 'ccc fees'],
            'answer': """CCC (Course on Computer Concepts)
• Duration: 3 months
• Timings: 2 hours per session
• Fees: ₹5000

Comprehensive Topics:
• Computer Fundamentals & History
• Operating Systems (Windows basics)
• MS Office (Word, Excel, PowerPoint)
• Internet & Email
• Digital Literacy & Cybersecurity basics
• Typing & Practical Applications
• Government Exam Preparation Focus

Government-recognized certificate course. Great for beginners and government job aspirants."""
        },

        # Tally with GST
        'tally_course': {
            'priority': 3,
            'keywords': ['tally','tally course', 'tally syllabus', 'tally with gst', 'tally erp 9', 'tally prime', 'accounting course tally'],
            'answer': """Tally Course (with GST)
• Duration: 3 months
• Timings: 2 hours per session
• Fees: ₹5000

Comprehensive Topics:
• Accounting Fundamentals
• Tally Prime / ERP 9 Interface
• Creating Company, Ledgers & Vouchers
• GST (CGST, SGST, IGST) Entries & Returns
• Inventory Management
• Payroll
• Financial Statements & Reports
• TDS, TCS basics
• Practical Billing & Invoicing Projects

Perfect for accounting careers, small business owners, and Tally certification."""
        },

        # ─────────────────────────────────────────────
        # Priority 4: FEES AND DURATION (General - Fallback only)
        # ─────────────────────────────────────────────
        'fees_and_duration': {
            'priority': 4,
            'keywords': ['fees', 'fee', 'cost', 'price', 'charges', 'pricing', 'how much', 'rate', 'amount', 'payment', 'pay', 'installment', 'emi', 'discount', 'scholarship', 'offer', 'affordable', 'duration', 'how long', 'months', 'weeks', 'days', 'length', 'period', 'complete', 'finish', 'course duration', 'course fee', 'total cost'],
            'answer': """Our course durations range from 1.5 to 8 months depending on the program. Fees are very affordable with EMI options available. Contact us at 9662512857 or visit https://theeasylearnacademy.com/ for exact current fees and special offers."""
        },

        # ─────────────────────────────────────────────
        # Priority 5: PLACEMENT (High)
        # ─────────────────────────────────────────────
        'placement': {
            'priority': 5,
            'keywords': ['placement', 'job', 'career', 'hire', 'hiring', 'employment', 'internship', 'opportunity', 'recruitment', 'company', 'companies', 'placed', 'get job', 'job support', 'job assistance', 'after course', 'work', 'industry', 'it company', 'salary', 'package', 'fresher', 'campus', 'interview', 'preparation', 'resume', 'cv', 'job ready', '100% placement'],
            'answer': """We provide full placement assistance including resume building, mock interviews, LinkedIn profile optimization, and direct referrals to IT companies. Many of our students have been placed in good companies with packages starting from 2.5-6 LPA depending on the course and skills. We also offer internship support."""
        },

        # ─────────────────────────────────────────────
        # Priority 6: COURSES OFFERED (General Overview)
        # ─────────────────────────────────────────────
        'courses': {
            'priority': 6,
            'keywords': ['courses', 'course', 'what do you teach', 'program', 'programs', 'subjects', 'curriculum', 'learn', 'study', 'python', 'mern', 'php', 'full stack', 'ai', 'ml', 'artificial intelligence', 'machine learning', 'data science', 'cyber security', 'ui', 'ux', 'ui/ux', 'web design', 'tally', 'ccc', 'android', 'java', 'asp.net', 'dot net', 'mobile app', 'web development', 'available', 'offer', 'list of courses', 'which course', 'what courses'],
            'answer': """We offer the following job-oriented courses:
• Python Programming (3 months)
• MERN Full Stack Development (6 months)
• AI/ML (8 months)
• Data Science (8 months)
• Cyber Security (8 months)
• Flutter Mobile App Development (6 months)
• Digital Marketing (6 months)
• C Programming (1.5 months)
• C++ Programming (1.5 months)
• Java Programming (3 months)
• CCC (3 months)
• Tally with GST (3 months)

All courses include practical projects, certificates, and placement support. Contact us for detailed syllabus and current offers."""
        },

        # ─────────────────────────────────────────────
        # Priority 7: BATCH TIMINGS (Medium-High)
        # ─────────────────────────────────────────────
        'batch_timings': {
            'priority': 7,
            'keywords': ['batch', 'timing', 'schedule', 'time', 'slot', 'session', 'morning', 'evening', 'weekend', 'weekday', 'saturday', 'sunday', 'monday', 'class time', 'when', 'next batch', 'start date', 'new batch', 'online', 'offline', 'flexible', 'timetable', 'availability', 'shift'],
            'answer': """We have Morning, Afternoon, and Evening batches available. Weekend batches are also offered for working professionals. New batches start every month. Both Online and Offline modes are available. Flexible timings can be discussed. Call us at 9662512857 to know the current batch schedule."""
        },

        # ─────────────────────────────────────────────
        # Priority 8: ELIGIBILITY (Medium)
        # ─────────────────────────────────────────────
        'eligibility': {
            'priority': 8,
            'keywords': ['eligibility', 'eligible', 'qualify', 'qualification', 'who can join', 'requirements', 'criteria', 'minimum', 'degree', 'student', 'fresher', 'beginner', 'experienced', 'professional', 'working', 'college', '12th', 'graduate', 'undergraduate', 'age', 'background', 'can i join', 'prerequisite', 'prior knowledge', 'anyone', 'no experience'],
            'answer': """Anyone can join our courses! 
• 10th/12th pass students
• College students (any stream)
• Fresh graduates
• Working professionals looking to upskill

No prior coding experience is required for most beginner courses. We start from basics. For advanced courses like AI/ML, basic computer knowledge helps."""
        },

        # ─────────────────────────────────────────────
        # Priority 9: CERTIFICATES (Medium)
        # ─────────────────────────────────────────────
        'certificates': {
            'priority': 9,
            'keywords': ['certificate', 'certification', 'certified', 'degree', 'diploma', 'credential', 'recognition', 'recognized', 'valid', 'government', 'accredited', 'authorized', 'completion certificate', 'course completion', 'industry recognized', 'iso', 'government certified', 'certificate value', 'will i get certificate', 'proof of completion'],
            'answer': """Every student receives:
• Course Completion Certificate
• Live Project Certificate
• Internship Certificate (if applicable)

These certificates are industry-recognized and help in job applications and higher studies. We also provide guidance for government-recognized certifications where relevant (e.g., CCC)."""
        },

        # ─────────────────────────────────────────────
        # Priority 10: TRAINING METHODOLOGY (Medium)
        # ─────────────────────────────────────────────
        'training_methodology': {
            'priority': 10,
            'keywords': ['training', 'methodology', 'teaching', 'how do you teach', 'practical', 'theoretical', 'hands on', 'hands-on', 'learn', 'style', 'approach', 'method', 'real world', 'projects', 'live project', 'experience', 'session', 'class', 'lecture', 'workshop', 'learning style', 'mode of training', 'interactive', 'industry ready', 'modern', 'technique'],
            'answer': """We focus on **100% Practical Training** with live industry projects. 
• Small batch sizes for personal attention
• Experienced trainers
• Latest tools and technologies
• Daily practice + weekly projects
• Doubt clearing sessions
• Both theory + hands-on in every class

Our goal is to make every student job-ready with real skills."""
        },

        # ─────────────────────────────────────────────
        # Priority 11: CORPORATE TRAINING (Low)
        # ─────────────────────────────────────────────
        'corporate_training': {
            'priority': 11,
            'keywords': ['corporate', 'corporate training', 'offshore', 'multinational', 'company training', 'employee training', 'business', 'enterprise', 'organization training', 'b2b', 'team training', 'staff training', 'software development', 'outsourcing', 'project outsource', 'it services', 'development services', 'hire for project', 'custom training', 'group training', 'professional training'],
            'answer': """We offer custom corporate training programs for company teams as well as offshore software development services for web and mobile applications. We can design tailored courses for your employees. Feel free to contact us at 9662512857 for your requirements."""
        },

        # ─────────────────────────────────────────────
        # Priority 12: ABOUT THE ACADEMY (Low)
        # ─────────────────────────────────────────────
        'about': {
            'priority': 12,
            'keywords': ['about', 'tell me about', 'easylearn', 'academy', 'who are you', 'introduction', 'organization', 'what do you do', 'overview', 'info', 'information', 'background', 'history', 'founded', 'establishment'],
            'answer': """EasyLearn Academy (also known as IT Experts Academy) is a leading IT training institute in Bhavnagar, Gujarat. 
We specialize in practical, job-oriented courses in programming, web development, mobile apps, AI/ML, Data Science, and Cybersecurity. 
Our mission is to make quality IT education accessible and affordable for students in smaller cities, with strong focus on hands-on projects and placement support."""
        },

        # ─────────────────────────────────────────────
        # Priority 13: GENERAL FAQ (Lowest)
        # ─────────────────────────────────────────────
        'general_faq': {
            'priority': 13,
            'keywords': ['demo', 'trial', 'free class', 'demo class', 'free demo', 'online', 'offline', 'mode', 'study material', 'notes', 'material', 'book', 'pdf', 'resources', 'doubt', 'doubt session', 'support after course', 'internship', 'what makes you different', 'why easylearn', 'unique', 'best institute', 'advantage', 'benefit', 'special', 'recording', 'recorded lecture', 'revision', 'faq', 'refund', 'cancellation', 'transfer', 'language', 'gujarati', 'hindi', 'english', 'medium'],
            'answer': """• Free Demo Classes available
• Both Online and Offline training modes
• Study material + Recorded lectures provided
• Doubt support even after course completion
• Teaching in Gujarati, Hindi, or English as needed
• Affordable fees with EMI options
• Strong focus on practical projects and job readiness

What makes us different: Personal attention in small batches + real industry projects + placement assistance.

Call/WhatsApp 9662512857 for any other questions!"""
        }
    }
}
