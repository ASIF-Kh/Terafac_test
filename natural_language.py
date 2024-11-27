import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def code_to_natural(code):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    prompt = f"""
    You are an expert code translator. Your task is to convert the given code into a clear and concise natural language description.
    Focus on explaining the purpose, functionality, and key components of the code.

    Code to translate:
    {code}

    Provide a natural language description of this code:
    """
    
    response = model.generate_content(prompt)
    return response.text

def natural_to_code(description, language="Python"):
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    prompt = f"""
    You are an expert code generator with deep knowledge of multiple programming languages and best practices. Your task is to translate the following natural language description into precise, executable code. Follow these guidelines:

    1. Language: {language}
    2. Purpose: Generate a function based on the given description
    3. Requirements: Ensure the code is efficient, readable, and follows best practices
    4. Input/Output: Determine appropriate inputs and outputs based on the description
    5. Additional Context: This is a standalone function that should be fully functional

    Natural Language Description:
    {description}

    Please generate the exact code that fulfills this description. Ensure the code follows best practices for readability and efficiency. If any part of the description is ambiguous, make reasonable assumptions.
    """
    
    response = model.generate_content(prompt)
    return response.text


if __name__ == "__main__":
    code_example = """
    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * calculate_factorial(n - 1)
    """

    natural_language = translate_code_to_natural_language(code_example)
    print("Natural Language Description:")
    print(natural_language)

    # Example 2: Natural Language to Code
    description = "Create a function that takes a list of numbers and returns the average of those numbers, handling empty lists and rounding the result to two decimal places."
    generated_function = generate_function_from_natural_language(description)
    print("\nGenerated Function:")
    print(generated_function)