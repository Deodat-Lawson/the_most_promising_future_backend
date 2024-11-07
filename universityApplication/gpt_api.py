from django.shortcuts import render
import openai, os, json
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from django.http import JsonResponse
from openai import OpenAI
from universityApplication.models import personalStatusForm
from universityApplication.serializers import personalStatusFormSerializer

load_dotenv()
api_key = os.getenv("OPENAI_KEY", None)


def chatbot(data: personalStatusForm):
  chatbot_response = None

  if api_key is not None:
    openai.api_key = api_key
    prompt = f"""
    `Analyze the following student profile to assess their academic strengths, potential for university admission, and offer specific university recommendations. Additionally, suggest actionable steps the student can take to strengthen their application further. Here are the profile details:
    
    - Full Name: {data.fullName}
    - Current Grade Level: {data.currentGradeLevel}
    - Location of Residence: {data.locationOfResidence}
    - Citizenship: {data.citizenship}
    - Current School System: {data.currentSchoolSystem}
    - GPA: {data.GPA}
    - SAT Score: {data.SAT}
    - ACT Score: {data.ACT}
    - Honors and Awards: {data.honorsAndAwards}
    - Fields of Interest: {data.fieldsOfInterest}
    - Geographic Preferences for University: {data.geographicPreferences}
    - Preferred University Size: {data.sizeOfUniversity}
    - Prestige Factor: {data.prestigeFactor}
    - Application Type Preferences:
        - Early Action (EA): {data.EA}
        - Early Decision (ED): {data.ED}
        - Regular Decision (RD): {data.RD}
    - Number of Schools Interested In: {data.numberOfSchools}
    
    Based on this information, provide:
    1. A skill level overview, highlighting areas of academic strength and readiness for university-level studies.
    2. University suggestions that align with the student’s geographic preferences, interests, preferred size, and prestige factor.
    3. Recommendations to strengthen the student’s application, such as enhancing academic scores, expanding extracurricular activities, or pursuing additional honors.
    
    Structure your response as follows:
    Skill Level Overview: Briefly summarize the student's academic profile and highlight areas of strength or uniqueness.
    University Suggestions: Provide a list of 3-5 universities that match the student's profile and explain why each would be a good fit.
    Improvement Recommendations: Offer actionable suggestions for improvement, including ways to enhance academic metrics, gain relevant experiences, or make the application more competitive.
    """

    client = OpenAI(
      # do .env later
      api_key='sk-g5P1Ja9GHKrh1vxJQkMwlCytZQsDGXcrIP5fZDDoQ4T3BlbkFJ_cAAHxYX2-tSzh_ZCqzYJyGq2-vTHxjal3VxhdQeYA',
    )

    chat_completion = client.chat.completions.create(
      messages=[
        {
          "role": "user",
          "content": prompt,
        }
      ],
      model="gpt-3.5-turbo",
    )

    chatbot_response = chat_completion.choices[0].message.content
    print(chatbot_response)

  return chatbot_response
