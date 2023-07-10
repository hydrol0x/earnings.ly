from flask import Flask, render_template, request
import asyncio
from EDGAR_api import run_sec_API
from palm import handle_chat
from clean_text import remove_stopwords
import json
import prompts

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/', methods=['POST'])
def process_query():
    global messages
    user_prompt = request.form['user_prompt']
    messages.append({'sender': 'user', 'content': user_prompt})

    try:
        data = asyncio.run(get_company_ids(user_prompt))

        valid = True
        if data["Form"] == "10-K":
            if data["Section"] not in prompts.ten_k_items:
                valid = False 
        elif data["Form"] == "8-K":
            if data["Section"] not in prompts.eight_k_items:
                valid = False
        elif data["Form"] == "10-Q":
            if data["Section"] not in prompts.ten_q_items:
                valid = False

        if not valid:
            data = asyncio.run(verify_sec_section(data))

        sec_data = run_sec_API(**data)
        sec_data_clean = remove_stopwords(sec_data[:4000])
        answer = asyncio.run(get_palm_response(user_prompt, sec_data_clean))
        messages.append({'sender': 'bot', 'content': answer})
    except:
        error_message = "Sorry, I couldn't find what you're looking for."
        messages.append({'sender': 'bot', 'content': error_message, 'error': True})

    return render_template('index.html', messages=messages)
async def get_company_ids(user_prompt)->dict:
    # Identation is on purpose otherwise formatting bad
    prompt = f"""
You are a language model specially trained to understand and interpret financial queries about stocks. Your main task is to extract and return the name of the company and relevant SEC earnings document and section to the query made by the user. The output should be in the form of a list if there is more than one company mentioned. Your responses will be used as input to another program that automatically searches for the company's stock ticker symbol on Google. The questions you receive will be primarily financial and related to stocks, bonds, and investment strategy. Your focus is on identifying the company or companies mentioned, not providing financial advice or information.
The company may not be explicitly mentioned and instead might be mentioned by its ticker symbol. Try to indetify ticker symbols or common abbreviations as that company.
If the user does not reference a real company or does not reference a company at all, set the companyName field to a blank string and output as normal.
The form section referenced should relate to the users query as closely as possible. Always pick a section even if it does not match the users request exactly.
Remember, you are not responding to the users question, you are only providing the SEC document and section that would most likely contan the answer to the users query. Do not attempt to directly answer the users query.

The examples below do not represent all companies, return the company name that best matches what the user asked.

{prompts.company_info_prompt}
    
User: {user_prompt}

PALM:
    """

    resp = await handle_chat(prompt)
    response = resp["response"]
    # print(response)
    data = json.loads(response)

    return data

async def verify_sec_section(company_info):
    prompt = f"""
I want you to verify that the following dictionary has valid information. It contains a 'Form' and a 'Section'. Below, I will provide you with several dictionaries for each for type. The keys of these dictionaries have all the valid section names for that form. If the dictionary you are validating has an invalid section name, I want you to return that dictionary with a new section name that is as close as possible to the original while being valid.
Only return a dictionary in the format {{"companyName": "NAME OF COMPANY", "Form": "SAME AS THE DICTIONARY GIVEN", "Section": "NAME OF VALID SECTION"}}, never return any plain text.
Only use the name of the section, not the corresponding number. Once again, never use a number for the output of the section name. 
Never put a number for values in the dictionary.
Only use the keys of the dictionary as the section name.
Do not use the dictionary values as a section name.

Valid Section Types:
10-K Form: {prompts.ten_k_items}

10-Q Form: {prompts.ten_q_items}

8-K Form: {prompts.eight_k_items}

Possibly Invalid Dictionary: {company_info}

Validated Dictionary:
    """

    resp = await handle_chat(prompt)
    response = resp["response"]
    # print(response)
    data = json.loads(response.replace("'", '"'))

    return data

async def get_palm_response(user_prompt, sec_data):
    prompt = f"""
    You are a financial assistant that advises users on their inquiries and questions concerning finance. Specifically, you answer questions involving companies listed on the stock exchange. You should inform your responses with data from the SEC filing and you are encouraged to cite relevant data or sections.
    Your answer should be concise but informative. Don't respond in long paragraphs. Give a clear conclusion and answer to the users query.
    Your job is to simplify the process of understanding long SEC filings by extracting the most important and relevant information to the users question.
    Remember, the user doesn't have direct access to the SEC filing that you do. Your job is to parse the filing and provide the user with the relevant information from it to answer their query. You shouldn't tell the user to reference any other documents.
    You are not giving out explicit financial advice or trading advice, you are simply parsing the SEC filing and providing the user with information so that they can make their decision based on data. 

    SEC Data:
    ___________
    {sec_data}
    ___________

    User: {user_prompt}

    Financial Advisor: Based on the SEC data I could find,
    """
    
    resp = await handle_chat(prompt)
    response = resp["response"]
    return response
    # data = json.loads(response)

    # return data

if __name__ == "__main__":
    app.run()
