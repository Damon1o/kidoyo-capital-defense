from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mepham-hackathon-2026'

SCHOOL    = "Wellington C. Mepham High School"
ORG       = "BMCHSD"
TEAM_NAME = "Capital Defense"
YEAR      = "2026"

MEMBERS = [
    {
        "id": 1, "slug": "member-1",
        "name": "Damon Lin", "role": "Team Captain / HTML, CSS, JS & Python Dev",
        "color": "#C63B2F", "grade": "9th Grade",
        "image": "images/members/sriracha-lime.png",
        "bio": "A guy who likes to code, doesn't sleep much, and is probably the most sleep deprived person on the team. He also has the biggest ego on the team.",
        "long_bio": "One of two 9th graders on the team. This guy has spent his summer in China learning about AI and machine learning. Lowkey the smartest person on the team. (Not biased)",
        "stars": 5, "fact_count": 999,
        "fun_facts": [
            {"label": "Fav Language", "value": "Python",  "percent": 99},
            {"label": "Hours Coded",  "value": "500+",    "percent": 87},
            {"label": "# of hours since last slept", "value": "24",       "percent": 1000},
            {"label": "Common Sense",   "value": "-100%","percent": -100},
        ],
        "tags": ["frontend", "backend", "AI/ML"], "weapon": "Flask + HTML"
    },
    {
        "id": 2, "slug": "member-2",
        "name": "Dagur Moi", "role": "Hatch and Python Dev",
        "color": "#C4742A", "grade": "9th Grade",
        "image": "images/members/caramel-salt.png",
        "bio": "The emotional support of the team, and also a pretty good coder. He's the team mascot. “Emilio Pickle” ~ Dagur Moi",
        "long_bio": "Dagur is one of the smartest people on the team, and also one of the most chill.",
        "stars": 5, "fact_count": 211,
        "fun_facts": [
            {"label": "Emilio Pickle", "value": "Yes",  "percent": 100},
            {"label": "Lost",  "value": "Yes",   "percent": 100},
            {"label": "Damon's Unpaid Worker", "value": "Always", "percent": 100},
            {"label": "Drama Kid",    "value": "Yes",     "percent": 100},
        ],
        "tags": ["hatch", "python", "team mascot"], "weapon": "Hatch"
    },
    {
        "id": 3, "slug": "member-3",
        "name": "Member Name", "role": "Data Scientist & ML Engineer",
        "color": "#1B3A6B", "grade": "12th Grade",
        "image": "images/members/truffle-parmesan.png",
        "bio": "Turns raw data into actionable insights. Brings machine learning expertise and analytical depth to every challenge the team faces.",
        "long_bio": "This member fell in love with data science after AP Statistics and never looked back. They have trained models for three independent research projects and contributed to open-source ML libraries.",
        "stars": 4, "fact_count": 87,
        "fun_facts": [
            {"label": "Fav Library",      "value": "PyTorch", "percent": 90},
            {"label": "Datasets Cleaned", "value": "12",      "percent": 60},
            {"label": "Accuracy Rate",    "value": "94%",     "percent": 94},
            {"label": "Kaggle Rank",      "value": "Top 5%",  "percent": 95},
        ],
        "tags": ["ML", "data", "research"], "weapon": "Python + TensorFlow"
    },
    {
        "id": 4, "slug": "member-4",
        "name": "Member Name", "role": "Systems Architect & DevOps",
        "color": "#5C2A6B", "grade": "11th Grade",
        "image": "images/members/sweet-chilli.png",
        "bio": "Keeps the whole operation running. From cloud infrastructure to CI/CD pipelines, this member makes sure the team's work is always deployed and always up.",
        "long_bio": "Infrastructure is an art form, and this member treats it that way. They set up the entire deployment pipeline from scratch and have never once let a deadline slip due to a server issue.",
        "stars": 4, "fact_count": 63,
        "fun_facts": [
            {"label": "Cloud Provider", "value": "AWS",   "percent": 88},
            {"label": "Uptime",         "value": "99.9%", "percent": 99},
            {"label": "Docker Images",  "value": "30+",   "percent": 75},
            {"label": "Ping (ms)",      "value": "12",    "percent": 98},
        ],
        "tags": ["DevOps", "cloud", "systems"], "weapon": "Docker + Kubernetes"
    },
    {
        "id": 5, "slug": "member-5",
        "name": "Harris Wu", "role": "The Human Popcorn Machine",
        "color": "#023020", "grade": "10th Grade",
        "image": "images/members/cheddar-jalapeno.png",
        "bio": "The human popcorn machine. He's always there to keep the team's spirits up and make sure everyone is having a good time.",
        "long_bio": "Harris is the warm body of the team. He's only here for the free food.",
        "stars": 1, "fact_count": 1,
        "fun_facts": [
            {"label": "Warm Body", "value": "Yes",   "percent": 100},
            {"label": "Definitely Knows How to Code",         "value": "0%", "percent": 0},
            {"label": "Here for the free food",  "value": "Yes",   "percent": 100},
            {"label": "Coding Experience",      "value": "0",    "percent": 0},
        ],
        "tags": ["Minecraft", "Sleep Deprived", "Free Food"], "weapon": "Minecraft Launcher"
    },
    {
        "id": 6, "slug": "member-6",
        "name": "BBQ & Honey", "role": "Savory & Sweet",
        "color": "#8b4513", "grade": "New Flavor",
        "image": "images/members/bbq-honey.png",
        "bio": "A perfect blend of smoky BBQ and sweet honey.",
        "long_bio": "This flavor brings the best of both worlds, providing a savory kick perfectly balanced by a smooth, sweet honey finish.",
        "stars": 5, "fact_count": 99,
        "fun_facts": [
            {"label": "Smokiness", "value": "High", "percent": 85},
            {"label": "Sweetness", "value": "Perfect", "percent": 90},
        ],
        "tags": ["sweet", "savory", "bbq"], "weapon": "Smoker"
    },
    {
        "id": 7, "slug": "member-7",
        "name": "Garlic Butter", "role": "Classic Comfort",
        "color": "#fada5e", "grade": "New Flavor",
        "image": "images/members/garlic-butter.png",
        "bio": "Rich, creamy, and undeniably garlicky.",
        "long_bio": "For the garlic lovers out there, this flavor is a rich, buttery dream that coats every kernel perfectly.",
        "stars": 4, "fact_count": 120,
        "fun_facts": [
            {"label": "Garlic Level", "value": "Extreme", "percent": 95},
            {"label": "Butteriness", "value": "Melt-in-mouth", "percent": 100},
        ],
        "tags": ["garlic", "butter", "classic"], "weapon": "Garlic Press"
    },
    {
        "id": 8, "slug": "member-8",
        "name": "Matcha Green Tea", "role": "Earthy & Zen",
        "color": "#8a9a5b", "grade": "New Flavor",
        "image": "images/members/matcha-green-tea.png",
        "bio": "An earthy, slightly sweet journey with every bite.",
        "long_bio": "Made with real matcha powder, this subtly sweet popcorn is perfect for someone looking for a unique, zen-like snacking experience.",
        "stars": 5, "fact_count": 42,
        "fun_facts": [
            {"label": "Antioxidants", "value": "High", "percent": 92},
            {"label": "Zen Mode", "value": "Activated", "percent": 100},
        ],
        "tags": ["matcha", "earthy", "green tea"], "weapon": "Whisk"
    },
]

CTX = dict(school=SCHOOL, org=ORG, team=TEAM_NAME, year=YEAR)

@app.route('/')
def index():
    return render_template('index.html', members=MEMBERS[:3], **CTX)

@app.route('/team')
def team():
    return render_template('team.html', members=MEMBERS, **CTX)

@app.route('/member/<slug>')
def member_detail(slug):
    member = next((m for m in MEMBERS if m['slug'] == slug), None)
    if not member:
        return redirect(url_for('team'))
    related = [m for m in MEMBERS if m['slug'] != slug][:3]
    return render_template('member_detail.html', member=member, related=related, **CTX)

@app.route('/about')
def about():
    return render_template('about.html', **CTX)

@app.route('/mepham')
def mepham():
    return render_template('mepham.html', **CTX)

@app.route('/hackathon')
def hackathon():
    return render_template('hackathon.html', **CTX)

if __name__ == '__main__':
    app.run(debug=True)
