import google.generativeai as genai
import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()

def ai_query(prompt):
    genai.configure(api_key=os.getenv('GEMINIAPI'))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    # print("Gemini response:")
    return("Gemini says: " + response.text)


def main():
    root = tk.Tk()
    root.title("AI Interaction Tool")
    
    prompt_label = tk.Label(root, text="Enter your prompt for Gemini:")
    prompt_label.pack(pady=5)
    
    prompt_entry = tk.Entry(root, width = 40)
    prompt_entry.pack(pady=5)

    response_text = tk.Text(root, height = 10, width = 50)
    response_text.pack(pady=5)
    
    def run_gemini():
        prompt = prompt_entry.get()
        response = ai_query(prompt)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response)
    
    def on_enter(event):
        run_gemini()

    prompt_entry.bind('<Return>', on_enter)

    gemini_button = tk.Button(root, text="Ask Gemini", command=run_gemini)
    gemini_button.pack(pady=5)

    root.mainloop()# if __name__ == "__main__":
main()

