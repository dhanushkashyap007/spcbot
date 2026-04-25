# College Enquiry Chatbot – St. Philomena College (Autonomous), Puttur

**Developed by:** Dept. of Computer Science, SPC Puttur  
**Tech Stack:** Python · Flask · NLTK · JSON · HTML · CSS · JavaScript

---

## Project Structure

```
spc_chatbot/
├── app.py            ← Flask backend (Python)
├── intents.json      ← All chatbot intents & responses (JSON)
├── index.html        ← Frontend webpage (HTML/CSS/JS)
├── requirements.txt  ← Python dependencies
└── README.md         ← This file
```

---

## Setup & Run (Local)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Flask Server
```bash
python app.py
```

Server runs at: **http://127.0.0.1:5000**

### 3. Open in Browser
Visit `http://127.0.0.1:5000` in Chrome, Firefox, or Edge.

---

## Integration into spcputtur.ac.in

### Option A – Floating Chat Widget (Recommended)
Add the following snippet anywhere inside `<body>` on the college website:

```html
<!-- SPC Chatbot Widget -->
<script>
  (function() {
    // Adjust this URL to your deployed Flask server
    var CHATBOT_URL = 'http://YOUR_SERVER_IP:5000';

    var btn = document.createElement('div');
    btn.innerHTML = '💬';
    btn.style.cssText = 'position:fixed;bottom:24px;right:24px;width:56px;height:56px;background:#0d1f3c;border:2px solid #c9a84c;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:24px;cursor:pointer;z-index:9999;box-shadow:0 4px 16px rgba(0,0,0,.3);';

    var iframe = document.createElement('iframe');
    iframe.src = CHATBOT_URL;
    iframe.style.cssText = 'position:fixed;bottom:90px;right:24px;width:400px;height:580px;border:none;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,.3);z-index:9998;display:none;';

    var open = false;
    btn.onclick = function() {
      open = !open;
      iframe.style.display = open ? 'block' : 'none';
    };

    document.body.appendChild(iframe);
    document.body.appendChild(btn);
  })();
</script>
```

### Option B – Embed as Full Page
Link directly to the chatbot page or embed the `index.html` as an iframe on a dedicated page of the website.

---

## Intents Covered (42 Intents)

| # | Intent Tag | Description |
|---|-----------|-------------|
| 1 | greeting | Hello, Hi, Hey |
| 2 | goodbye | Bye, Exit |
| 3 | thanks | Thank you |
| 4 | college_name | Full name of college |
| 5 | college_history | Founded year, founder |
| 6 | vision_mission | Vision and mission |
| 7 | accreditation | NAAC, ISO, Autonomous status |
| 8 | contact | Phone, email, address |
| 9 | location | College location, address |
| 10 | admission | How to apply |
| 11 | admission_eligibility | Eligibility criteria |
| 12 | ug_courses | All UG programs |
| 13 | pg_courses | All PG programs |
| 14 | bca_course | BCA details |
| 15 | bcom_course | B.Com details |
| 16 | bba_course | BBA details |
| 17 | ba_course | BA details |
| 18 | bsc_course | B.Sc details |
| 19 | mca_course | MCA details |
| 20 | mcom_course | M.Com details |
| 21 | msw_course | MSW details |
| 22 | msc_physics | M.Sc Physics |
| 23 | msc_maths | M.Sc Mathematics |
| 24 | fee_structure | Fees info |
| 25 | scholarships | Scholarships available |
| 26 | placement | Placement cell |
| 27 | library | Library facilities |
| 28 | hostel | Hostel info |
| 29 | ncc | NCC at SPC |
| 30 | nss | NSS at SPC |
| 31 | sports | Sports facilities |
| 32 | clubs | Student clubs |
| 33 | certificate_courses | Certificate programs |
| 34 | academic_calendar | Exam & semester dates |
| 35 | principal | Principal of the college |
| 36 | anti_ragging | Anti-ragging policy |
| 37 | grievance | Grievance redressal |
| 38 | women_cell | ICC, women support |
| 39 | iqac | IQAC details |
| 40 | exam_results | Results info |
| 41 | syllabus | Curriculum info |
| 42 | autonomous | Autonomous status explained |
| + many more | ... | |

---

## Technology Stack (As per SRS/SDD Documents)

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| NLP | NLTK (tokenization, stemming, stopwords) |
| Database | JSON (intents.json) |
| Server | Flask Local Server |
| Browser | Chrome, Firefox, Edge |

---

## How the NLP Works

1. **User types a message**
2. **Preprocessing:** Text is lowercased → tokenized → stopwords removed → stemmed using PorterStemmer
3. **Intent Classification:** Token overlap (Jaccard similarity) between user tokens and all intent patterns
4. **Response:** Random response from the matched intent
5. **Fallback:** If similarity < 0.3, returns the 'unknown' intent response

---

*St. Philomena College (Autonomous), Puttur – College Enquiry Chatbot Project*
