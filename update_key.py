code_string = """import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai

# Securely fetch the API key from environment variables
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def dashboard(request):
    return render(request, 'guidance/dashboard.html')

@csrf_exempt
def generate_guidance(request):
    if request.method == "POST":
        education = request.POST.get('education', '')
        skills = request.POST.get('skills', '')
        interests = request.POST.get('interests', '')
        goals = request.POST.get('goals', '')

        prompt = f"Act as an AI Career Guidance Assistant. Based on the following profile:\\nEducation: {education}\\nSkills: {skills}\\nInterests: {interests}\\nGoals: {goals}\\n\\nProvide a structured response containing:\\n1. Career Recommendation\\n2. Skill Gap Analysis\\n3. Learning Path Recommendation"

        try:
            model = genai.GenerativeModel('gemini-3.8-flash')
            response = model.generate_content(prompt)
            return JsonResponse({'guidance': response.text})
        except Exception as e:
            return JsonResponse({'guidance': f"API Error: {str(e)}"}, status=500)
"""

with open("guidance/views.py", "w") as f:
    f.write(code_string)

print("SUCCESS! views.py has been updated to use environment variables.")