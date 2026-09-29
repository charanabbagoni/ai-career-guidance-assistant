code_string = """from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai

# Using your provided API key
genai.configure(api_key="AQ.Ab8RN6JNioKTBJTaiUtyAMI3gSoBTrw9olj29UQF221EBZ9eyg")

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
            # Dynamically ask the API which models are available and pick the first one that works
            valid_model_name = 'gemini-1.5-flash'
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    valid_model_name = m.name
                    break
                    
            model = genai.GenerativeModel(valid_model_name)
            response = model.generate_content(prompt)
            return JsonResponse({'guidance': response.text})
        except Exception as e:
            return JsonResponse({'guidance': f"API Error: {str(e)}"}, status=500)
"""

with open("guidance/views.py", "w") as f:
    f.write(code_string)
    
print("SUCCESS! views.py has been securely updated with the dynamic model selector.")