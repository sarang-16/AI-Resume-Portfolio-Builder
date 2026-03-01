import streamlit as st , google.generativeai as genai, json

# config

genai.configure(api_key=" ENTER YOUR API HERE <-- ")

def model ():
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            return genai.GenerativeModel(m.name)
    st.stop()

model_ = model()

st.set_page_config("AI Resume Builder 👷‍♂️ ", layout="wide")    

template = {
    "Classic Blue" : "#1f4fd8",
    "Strange Orange ": "#e74c3c",
    "Funky Yellow": "#e1ff00",
    "Corporate (Grey)": "#34495e"

}

#ai

def generate__resume(data):
    prompt = f"""
You are a professional resume writer and career expert.

Transform the provided user data into a polished, professional resume.

RULES:
- Use ONLY provided data
- Rephrase professionally
- Expand short entries
- Skip empty sections

Return STRICT JSON ONLY.

JSON FORMAT:
{{
 "summary":[], "skills":[], "education":[], "projects":[],
 "certifications":[], "awards":[], "languages":[], "contact":[]
}}

USER DATA:
{data}
"""
    r = model_.generate_content(prompt).text
    return json.loads(r[r.find("{"):r.rfind("}")+1])

# ---------- HTML ----------
def html__resume(name, r, accent):
    sec = lambda t,i: f"<div class='s'><h2>{t}</h2><ul>{''.join(f'<li>{x}</li>' for x in i)}</ul></div>" if i else ""
    return f"""
<!DOCTYPE html><html><head><style>
body{{font-family:Arial;background:#171c2a;padding:40px}}
.card{{background:#fff;padding:35px;border-radius:12px}}
.name{{font-size:40px;font-weight:800}}
h2{{border-bottom:3px solid {accent};margin-top:25px}}
li{{line-height:1.6}}
</style></head><body>
<div class=card>
<div class=name>{name}</div>
{sec("CONTACT",r.get("contact"))}
{sec("SUMMARY",r.get("summary"))}
{sec("SKILLS",r.get("skills"))}
{sec("EDUCATION",r.get("education"))}
{sec("PROJECTS",r.get("projects"))}
{sec("CERTIFICATIONS",r.get("certifications"))}
{sec("AWARDS",r.get("awards"))}
{sec("LANGUAGES",r.get("languages"))}
</div></body></html>
"""

#ui 

st.title("🧠 AI Resume Builder")

with st.form("f"):
    name = st.text_input("full name")
    ed = st.text_area("education")
    skill = st.text_area("skills")
    project = st.text_area("projects")
    certi = st.text_area("Certifications")
    award = st.text_area("Awards")
    language = st.text_area("Languages")
    contact = st.text_area("Contact Details")
    theme = st.selectbox("Template", template)
    go = st.form_submit_button("Generate")

if go :
    if not name or not ed or not skill:
        st.error("name, education & skills required"); st.stop()

    data = f"""
name : {name}
education : {ed}
skills:{skill}
projects: {project}
certifications:{certi}
awards:{award}
languages:{language}
contact : {contact}
"""
    resume = generate__resume(data)
    html = html__resume(name,resume, template[theme])

    st.components.v1.html(html, height=1000,scrolling=True)
    st.download_button("⬇ download resume (HTML)", html,
        f"{name.replace(' ','_')}_resume.html","text/html")
        