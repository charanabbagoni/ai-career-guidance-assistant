html_data = """
[!DOCTYPE html]
[html lang="en"]
[head]
    [meta charset="UTF-8"]
    [title]AI Career Guidance Assistant[/title]
    [style]
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; padding: 20px; }
        .container { max-width: 800px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        label { font-weight: bold; margin-top: 10px; display: block; }
        input { width: 100%; padding: 10px; margin: 8px 0 20px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background-color: #007bff; color: white; padding: 12px 20px; border: none; border-radius: 5px; cursor: pointer; width: 100%; font-size: 16px; }
        .result-box { margin-top: 20px; padding: 15px; background-color: #e9ecef; border-radius: 5px; display: none; white-space: pre-wrap; line-height: 1.6; }
    [/style]
[/head]
[body]
    [div class="container"]
        [h2]AI Career Guidance Assistant[/h2]
        [form id="profileForm"]
            [label]Education & Academic Details:[/label]
            [input type="text" id="education" required]
            
            [label]Technical & Soft Skills:[/label]
            [input type="text" id="skills" required]
            
            [label]Interests:[/label]
            [input type="text" id="interests" required]
            
            [label]Career Goals:[/label]
            [input type="text" id="goals" required]
            
            [button type="submit"]Analyze Profile & Get Guidance[/button]
        [/form]
        [div id="result" class="result-box"][/div]
    [/div]

    [script]
        document.getElementById('profileForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const resultBox = document.getElementById('result');
            resultBox.style.display = 'block';
            resultBox.innerText = "Analyzing your profile using AI... please wait.";

            const formData = new FormData();
            formData.append('education', document.getElementById('education').value);
            formData.append('skills', document.getElementById('skills').value);
            formData.append('interests', document.getElementById('interests').value);
            formData.append('goals', document.getElementById('goals').value);

            try {
                const response = await fetch('/generate/', {
                    method: 'POST',
                    body: formData,
                    headers: { 'X-CSRFToken': '{{ csrf_token }}' }
                });
                const data = await response.json();
                resultBox.innerText = data.guidance;
            } catch (error) {
                resultBox.innerText = "An error occurred. Please try again.";
            }
        });
    [/script]
[/body]
[/html]
"""

# This automatically converts the brackets back to proper HTML tags and saves the file
final_html = html_data.replace("[", "<").replace("]", ">")

with open("guidance/templates/guidance/dashboard.html", "w") as f:
    f.write(final_html.strip())
    
print("SUCCESS! The HTML file is now generated correctly.")