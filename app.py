from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

TEAM_MEMBERS = [
    {
        "id": 1,
        "slug": "alex-chen",
        "name": "Alex Chen",
        "initials": "AC",
        "role": "Full Stack Engineer",
        "color": "#C63B2F",
        "tag_color": "red",
        "bio": "Alex bridges the gap between beautiful interfaces and rock-solid backends. A hackathon veteran who ships fast and ships clean.",
        "long_bio": "With deep experience in React, Node.js, and cloud infrastructure, Alex loves building products that are both elegant and performant. Known for turning wild hackathon ideas into working prototypes overnight, Alex is the engine of the team.",
        "fun_fact": "Can spin up a full-stack app before their coffee goes cold.",
        "skills": ["React", "Node.js", "TypeScript", "PostgreSQL", "AWS"],
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
    },
    {
        "id": 2,
        "slug": "jamie-rivera",
        "name": "Jamie Rivera",
        "initials": "JR",
        "role": "Frontend Developer",
        "color": "#C4742A",
        "tag_color": "orange",
        "bio": "Jamie crafts interfaces that feel intuitive and look stunning. If it's on the screen, Jamie made it worth looking at.",
        "long_bio": "A self-described design engineer, Jamie blurs the line between code and creativity. Proficient in modern CSS, animation, and accessibility, Jamie ensures every user interaction feels polished. Their eye for detail has saved the team from countless UX disasters.",
        "fun_fact": "Maintains a personal CSS snippet library with over 300 entries.",
        "skills": ["Vue.js", "CSS / Tailwind", "Figma", "a11y", "Animation"],
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
    },
    {
        "id": 3,
        "slug": "sam-patel",
        "name": "Sam Patel",
        "initials": "SP",
        "role": "Backend Engineer",
        "color": "#1B3A6B",
        "tag_color": "blue",
        "bio": "Sam architects the systems that keep everything running. APIs, databases, queues — Sam makes the invisible magic happen.",
        "long_bio": "Sam specialises in scalable distributed systems and API design. From zero-downtime deployments to complex data pipelines, Sam brings engineering rigour to every project. At hackathons, Sam is the one who already has a working backend before everyone else has finished planning.",
        "fun_fact": "Once wrote a Redis cache layer in 20 minutes on a train.",
        "skills": ["Python", "FastAPI", "Redis", "Docker", "Kubernetes"],
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
    },
    {
        "id": 4,
        "slug": "jordan-kim",
        "name": "Jordan Kim",
        "initials": "JK",
        "role": "ML / AI Engineer",
        "color": "#2F6B5A",
        "tag_color": "green",
        "bio": "Jordan makes machines think. From NLP to computer vision, Jordan brings intelligent features that make projects truly stand out.",
        "long_bio": "Jordan has a knack for taking cutting-edge research and making it production-ready in record time. Whether it's fine-tuning a language model or building a recommendation engine from scratch, Jordan finds creative ways to make AI a core part of every build.",
        "fun_fact": "Trained a model on their own commit history to predict when they'll push bugs.",
        "skills": ["Python", "PyTorch", "LLMs", "scikit-learn", "Jupyter"],
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
    },
    {
        "id": 5,
        "slug": "taylor-okonkwo",
        "name": "Taylor Okonkwo",
        "initials": "TO",
        "role": "DevOps & Cloud",
        "color": "#8B2020",
        "tag_color": "red",
        "bio": "Taylor keeps the team's code alive and the servers happy. Infrastructure as code, CI/CD, and cloud wizardry — that's Taylor's domain.",
        "long_bio": "Taylor is the reason the team's demos never crash. With deep expertise in CI/CD pipelines, cloud platforms, and container orchestration, Taylor ensures that whatever the team builds can actually be deployed reliably. An advocate for infrastructure as code and automated everything.",
        "fun_fact": "Has never manually deployed to production. Has always had a pipeline for it.",
        "skills": ["Terraform", "GitHub Actions", "GCP", "Linux", "Monitoring"],
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
    },
]

@app.route('/')
def index():
    featured = TEAM_MEMBERS[:3]
    return render_template('index.html', members=featured)

@app.route('/team')
def team():
    return render_template('team.html', members=TEAM_MEMBERS)

@app.route('/team/<slug>')
def member_detail(slug):
    member = next((m for m in TEAM_MEMBERS if m['slug'] == slug), None)
    if not member:
        return redirect(url_for('team'))
    others = [m for m in TEAM_MEMBERS if m['slug'] != slug][:3]
    return render_template('member_detail.html', member=member, others=others)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
    app.run(debug=True)
