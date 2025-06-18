import pandas as pd
import json
from langchain.schema import HumanMessage
from langchain_groq import ChatGroq

# Load your info from JSON
with open("my_info.json", "r") as file:
    my_info = json.load(file)

# Initialize LLaMA model (Groq)
llm = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192",
    api_key="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"
)

def generate_email(first_name, job_title, company, industry, website, city, country, linkedin_profile):
    prompt = f"""
Prompt


hey  act as a salesperson for Cad & Cart when writing emails. Emails should be: 
- Focused and goal-oriented
- Conversational yet formal
- Personalized with uncommon commonalities
- Concise and easy to read
- Credible (include useful data or connections)
- Reader-centric (address their problems)
- Respectful of the recipient's time (no demands)
- Include a clear call to action.



i will give you sumaary of the compny that we want to connect from this summary write mail to that company , also add lines for our previous clients reference , also tell them i have attaced our company profile plz check it. ok ?

et me know we got my point or not 


ChatGPT said:
Got it! Share the company summary, and I’ll craft a well-structured sales email incorporating:

A personalized introduction
A connection to their company’s work
References to our previous clients
A mention of the attached company profile
A clear and respectful call to action
Send over the details, and I’ll get started!






You said:
addl lines for we have as  ISO 9001, AS 9100 which required for arespace sectore also  we provide  details documentations like CMM Inspection Report
Full Dimensional Inspections
Material Test Reports
Material Certificates
Certificates of Conformance
First Article Inspectionsnot only in cnc we are in 3d printing , injection moulding , sheet metal
ChatGPT said:
Understood! When you send the company summary, I’ll draft an email that:

Highlights Cad & Cart’s certifications (ISO 9001, AS 9100), making us a reliable choice for the aerospace sector
Emphasizes our ability to provide detailed documentation (CMM Inspection Report, Full Dimensional Inspections, Material Test Reports, Certificates of Conformance, etc.)
Showcases our broad manufacturing capabilities, including CNC machining, 3D printing, injection molding, and sheet metal fabrication
References our previous clients
Mentions the attached company profile and invites them to check it
Send over the summary, and I’ll craft the perfect email!


also 

first let me tell you one thing we have manufacturing and we need orders from the companies so focus on how we have help them in manufacturing through instant quote to manufacturing to quality to delivery 

give reference of previous compines we worked with 
If  automation and robotics companies Unbox Robotics, Yantrana Systems, Uno Minda, and Plexware Automation 

if aerospace, defence, drone then sagar defence , drdo, ikran aerospace , etherealx  , manstu aerospace , tmpl  


if industrial machineries then - Proarc , kirloskar pnumatics , yazaki , v-tech engineering ,  zimmer group, warade pactech , rigbetel labs , hyrovert , tritium motors 


if automobile and green energy then - octarange techanology , hyrovert , trirtum motor, ground mobile, navnit motors , clean electric , jit solution 




write only body of mail dont write regards and subject only focus on body , main body in 1800 characters also use bullet point in somewhere , use ✓  for bullet points

i will share companies website search about company , gothrought website and then write personlized mail ,


- **Recipient Name:** {first_name}
- **Recipient Job Title:** {job_title}
- **Recipient Company:** {company}
- **Industry:** {industry}
- **Website:** {website}
- **Location:** {city}, {country}
- **LinkedIn:** {linkedin_profile}

Include the following sender details in the sign-off:
- **Sender Name:** {my_info['your_name']}
- **Sender Title:** {my_info['your_title']}
- **Sender Company:** {my_info['your_company']}
- **Sender Email:** {my_info['your_email']}
- **Sender Phone:** {my_info['your_phone']}

The email should:
- Begin with "Dear [First Name],"
- Mention the recipient's company and role positively.
- Invite them for a potential collaboration.
- Keep the tone human and under 150 words.
    """

    response = llm([HumanMessage(content=prompt)])
    return response.content

def main():
    df = pd.read_csv("test.csv")[:2]
    df.columns = df.columns.str.strip()

    email_texts = []
    for _, row in df.iterrows():
        email = generate_email(
            first_name=row['First Name'],
            job_title=row['Title'],
            company=row['Company'],
            industry=row['Industry'],
            website=row['Website'],
            city=row['City'],
            country=row['Country'],
            linkedin_profile=row['Person Linkedin Url']
        )
        email_texts.append(email)

    df["Generated Email"] = email_texts
    df.to_excel("emailscomapny2.xlsx", index=False)
    print("✅ Personalized emails generated and saved!")

if __name__ == "__main__":
    main()
