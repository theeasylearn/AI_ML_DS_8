# ============================================================
# EasyLearn Academy - Knowledge Base with Topic Priorities
# ============================================================
# 
# Topics are arranged in PRIORITY ORDER (Highest → Lowest)
#
# HOW TO USE:
# When a user query matches keywords from multiple topics,
# the topic with the LOWER priority number wins.
# (1 = Highest priority, 12 = Lowest priority)
# ============================================================

knowledge = {
    'topics': {
        # ─────────────────────────────────────────────
        # Priority 1: CONTACT (Highest)
        # ─────────────────────────────────────────────
        'contact': {
            'priority': 1,
            'keywords': ['contact', 'reach', 'call', 'phone', 'number', 'email', 'whatsapp', 'message', 'enquiry', 'inquiry', 'get in touch', 'help', 'connect', 'talk', 'speak', 'chat', 'customer care', 'helpline', 'toll free', 'reach out', 'how to contact', 'contact details', 'social media', 'facebook', 'instagram', 'linkedin', 'website'],
            'answer': """You can reach us at Eva Surbhi Mall, 105, Waghawadi Road, Bhavnagar. Visit our website https://theeasylearnacademy.com/ for phone, email, and WhatsApp details. We are available Monday to Saturday, 9 AM to 7 PM."""
        },

        # ─────────────────────────────────────────────
        # Priority 2: LOCATION (Very High)
        # ─────────────────────────────────────────────
        'location': {
            'priority': 2,
            'keywords': ['location', 'address', 'where', 'place', 'situated', 'find you', 'directions', 'how to reach', 'map', 'navigate', 'office', 'city', 'state', 'gujarat', 'bhavnagar', 'visit', 'near', 'landmark', 'pincode', 'area', 'road', 'mall', 'institute location', 'academy location', 'institute address', 'academy address', 'where is institute', 'where is academy', 'institute', 'class'],
            'answer': """We are located at Eva Surbhi Mall, 105, Waghawadi Road, opposite Aksharwadi Temple, Bhavnagar, Gujarat - 364002. You can visit us Monday to Saturday. Check our website for more details: https://theeasylearnacademy.com/"""
        },

        # ─────────────────────────────────────────────
        # Priority 3: FEES AND DURATION (Very High)
        # ─────────────────────────────────────────────
        'fees_and_duration': {
            'priority': 3,
            'keywords': ['fees', 'fee', 'cost', 'price', 'charges', 'pricing', 'how much', 'rate', 'amount', 'payment', 'pay', 'installment', 'emi', 'discount', 'scholarship', 'offer', 'affordable', 'duration', 'how long', 'months', 'weeks', 'days', 'length', 'period', 'complete', 'finish', 'course duration', 'course fee', 'total cost'],
            'answer': """Course duration ranges from 1 to 6 months depending on the course. Our fees are very affordable with EMI options available. Please contact us for exact fees and current offers."""
        },

        # ─────────────────────────────────────────────
        # Priority 4: PLACEMENT (High)
        # ─────────────────────────────────────────────
        'placement': {
            'priority': 4,
            'keywords': ['placement', 'job', 'career', 'hire', 'hiring', 'employment', 'internship', 'opportunity', 'recruitment', 'company', 'companies', 'placed', 'get job', 'job support', 'job assistance', 'after course', 'work', 'industry', 'it company', 'salary', 'package', 'fresher', 'campus', 'interview', 'preparation', 'resume', 'cv', 'job ready', '100% placement'],
            'answer': """We provide full placement assistance including resume building, mock interviews, and direct referrals to companies. Many of our students have been placed in good IT companies."""
        },

        # ─────────────────────────────────────────────
        # Priority 5: COURSES OFFERED (High)
        # ─────────────────────────────────────────────
        'courses': {
            'priority': 5,
            'keywords': ['courses', 'course', 'what do you teach', 'program', 'programs', 'subjects', 'curriculum', 'training', 'learn', 'study', 'python', 'mern', 'php', 'full stack', 'ai', 'ml', 'artificial intelligence', 'machine learning', 'data science', 'cyber security', 'ui', 'ux', 'ui/ux', 'web design', 'tally', 'ccc', 'android', 'java', 'asp.net', 'dot net', 'mobile app', 'web development', 'available', 'offer', 'list of courses', 'which course', 'what courses'],
            'answer': """We offer courses in Python, Java, Full Stack MERN, PHP, Web Design, Android Development, AI/ML, Data Science, Cyber Security, UI/UX, CCC, and Tally. Contact us for fees and duration of any course."""
        },

        # ─────────────────────────────────────────────
        # Priority 6: BATCH TIMINGS (Medium-High)
        # ─────────────────────────────────────────────
        'batch_timings': {
            'priority': 6,
            'keywords': ['batch', 'timing', 'schedule', 'time', 'slot', 'session', 'morning', 'evening', 'weekend', 'weekday', 'saturday', 'sunday', 'monday', 'class time', 'when', 'next batch', 'start date', 'new batch', 'online', 'offline', 'flexible', 'timetable', 'availability', 'shift'],
            'answer': """We have morning, afternoon, and evening batches. Weekend batches are also available. New batches start every month. Both online and offline modes are offered."""
        },

        # ─────────────────────────────────────────────
        # Priority 7: ELIGIBILITY (Medium)
        # ─────────────────────────────────────────────
        'eligibility': {
            'priority': 7,
            'keywords': ['eligibility', 'eligible', 'qualify', 'qualification', 'who can join', 'requirements', 'criteria', 'minimum', 'degree', 'student', 'fresher', 'beginner', 'experienced', 'professional', 'working', 'college', '12th', 'graduate', 'undergraduate', 'age', 'background', 'can i join', 'prerequisite', 'prior knowledge', 'anyone', 'no experience'],
            'answer': """Anyone can join - 10th/12th pass students, college students, fresh graduates, and working professionals. No prior coding experience is required for beginners."""
        },

        # ─────────────────────────────────────────────
        # Priority 8: CERTIFICATES (Medium)
        # ─────────────────────────────────────────────
        'certificates': {
            'priority': 8,
            'keywords': ['certificate', 'certification', 'certified', 'degree', 'diploma', 'credential', 'recognition', 'recognized', 'valid', 'government', 'accredited', 'authorized', 'completion certificate', 'course completion', 'industry recognized', 'iso', 'government certified', 'certificate value', 'will i get certificate', 'proof of completion'],
            'answer': """Every student receives a course completion certificate and a live project certificate. These certificates are industry-recognized and help in job applications."""
        },

        # ─────────────────────────────────────────────
        # Priority 9: TRAINING METHODOLOGY (Medium)
        # ─────────────────────────────────────────────
        'training_methodology': {
            'priority': 9,
            'keywords': ['training', 'methodology', 'teaching', 'how do you teach', 'practical', 'theoretical', 'hands on', 'hands-on', 'learn', 'style', 'approach', 'method', 'real world', 'projects', 'live project', 'experience', 'session', 'class', 'lecture', 'workshop', 'learning style', 'mode of training', 'interactive', 'industry ready', 'modern', 'technique'],
            'answer': """We focus on 100% practical training with live industry projects. Classes are conducted in small batches so every student gets personal attention. Our trainers are experienced and we use the latest tools and technologies."""
        },

        # ─────────────────────────────────────────────
        # Priority 10: CORPORATE TRAINING (Low)
        # ─────────────────────────────────────────────
        'corporate_training': {
            'priority': 10,
            'keywords': ['corporate', 'corporate training', 'offshore', 'multinational', 'company training', 'employee training', 'business', 'enterprise', 'organization training', 'b2b', 'team training', 'staff training', 'software development', 'outsourcing', 'project outsource', 'it services', 'development services', 'hire for project', 'custom training', 'group training', 'professional training'],
            'answer': """We offer custom corporate training for company teams as well as offshore development services for web and mobile applications. Feel free to contact us for your requirements."""
        },

        # ─────────────────────────────────────────────
        # Priority 11: ABOUT THE ACADEMY (Low)
        # ─────────────────────────────────────────────
        'about': {
            'priority': 11,
            'keywords': ['about', 'tell me about', 'easylearn', 'academy', 'who are you', 'introduction', 'organization', 'what do you do', 'overview', 'info', 'information', 'background', 'history', 'founded', 'establishment'],
            'answer': """EasyLearn Academy is an IT training institute in Bhavnagar, Gujarat. We focus on practical courses with live projects, especially in web and mobile app development. We also provide corporate training and offshore development services. Our main goal is to make students job-ready with real skills."""
        },

        # ─────────────────────────────────────────────
        # Priority 12: GENERAL FAQ (Lowest)
        # ─────────────────────────────────────────────
        'general_faq': {
            'priority': 12,
            'keywords': ['demo', 'trial', 'free class', 'demo class', 'free demo', 'online', 'offline', 'mode', 'study material', 'notes', 'material', 'book', 'pdf', 'resources', 'doubt', 'doubt session', 'support after course', 'internship', 'what makes you different', 'why easylearn', 'unique', 'best institute', 'advantage', 'benefit', 'special', 'recording', 'recorded lecture', 'revision', 'faq', 'refund', 'cancellation', 'transfer', 'language', 'gujarati', 'hindi', 'english', 'medium'],
            'answer': """We offer free demo classes. Both online and offline training is available. Study material and recorded lectures are provided. We also give doubt support even after course completion. Teaching is done in Gujarati, Hindi, or English as needed."""
        }
    }
}
