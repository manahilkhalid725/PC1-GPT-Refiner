import openai
import os

openai.api_key = "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"  # Replace if needed

def refine_pc1_objectives(user_input):
    prompt = f"""
    You are an AI assistant specializing in PC-1 form documentation. Your task is to refine and structure the given project objectives. Ensure that:
    - The objectives are clear, well-detailed, and formatted professionally.
    - Any incorrect or incomplete details are corrected.
    - Objectives are aligned with the sector’s five-year plan.
    - The refined output includes feasibility, governance, and sustainability aspects.
    - Each point is expanded with subpoints for clarity.
    
    **User Input Objectives:**  
    {user_input}  

    **Refined and Detailed Objectives:**  
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in reviewing and refining official PC-1 documents."},
                {"role": "user", "content": prompt}
            ]
        )

        refined_text = response.choices[0].message.content
        return refined_text

    except openai.OpenAIError as e:
        return f"Error: {str(e)}"
    
#main
user_input = "Develop transport system for city. Improve roads. Less traffic issues."
refined_output = refine_pc1_objectives(user_input)
print("Refined Objectives:\n", refined_output)
