"""
Created on 
@author: Sahand-j
"""

import re

# template from Indeed.com
template = '''[Your name]
[Your full address]
[Your city, state and zip code]
[Your phone number]
[Your email address]
[Date: _________________]
[Hiring manager’s name]
[Company name]
[Company address]
[Company city, state and zip code]
Dear hiring manager [Use their name if you know it]:
My name is [Your name] and I am writing to express my interest in the [Name of position] with [Company name]. I am excited for the opportunity to work for [Company name] because [Provide specific reason]. I would be the perfect candidate for the [Name of position] because [Provide specific reason]. This position aligns perfectly with my goal of [Your career goal].
As a recent graduate from [University or College name] with a [Type of degree] I have the required training needed for the [Name of position] at [Company name]. Relevant course work included [Names of courses]. I graduated with Honors and as a member of [Name of associations]. My prior experience in [Name of position] in the [Name of industry] also gave me the [Relevant skills / experience] needed for [Specific job responsibility from job posting].
One thing that attracted me most to [Name of company] is [Specific thing you like about the company]. I am also passionate about [Related skill] and volunteer regularly for [List relevant volunteer experience]. I look forward to meeting you in person during an interview to further discuss my qualifications and how I will be an asset to [Company name]. Thank you for your time and consideration.

Sincerely,

[Your name printed]

'''

def file_converter(s):
    """
    s: text file (or string text) of Cover Letter template 
    formats input with {} for .format method to work
    @return(String) formatted string 
    """
    pars = s.split(']')
    reg = re.compile(r'\[[\s\S]*')
    empty = []
    for i in pars:
        empty.append(re.sub(reg,'{}',i))
    result = ''.join(empty)
    return result
     
def generate_list_of_req(s):
    """
    s: string template
    generates list of requirements in template
    :@return(Array): returns of requirements between brackets [] 
    """
    res = re.findall(r"\[[^\]]*\]",s)
    return res

def input_new_values(formed_text, sample_list):
    """
    formed_text: formatted text with {}
    sample_list: list of new user values
    formats text with user values
    :@return(String) Re-formatted version of  
    """
    return formed_text.format(*sample_list)

def just_show_brackets_with_index(f):
    """
    f: 
    helper method to show template with numbered brackets
    :@return(String) Re-formatted version of  
    """
    
    smod = replace_brackets(f)
    pars = smod.split(')')
    reg = re.compile(r'\([\s\S]*')
    empty = []
    counter = 1
    for i in pars:
        empty.append(re.sub(reg,'{'+ str(counter) + '}', i))
        counter+=1
    return ''.join(empty)
    
def replace_all(text, dic):
    """
    text: input string of template
    dic: 
    replacing method - from stackOverflow
    :@return(String) with replaced parens for brackets
    """
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def replace_brackets(string_data):
    """
    string_data: string template
    replacing [] with {} for formatting reason, uses replace_all method
    :@return(String) with repalced brackets with parens
    """
    d = { '[': '(', ']': ')'}
    return replace_all(string_data, d)


#Main Program
running = True
array_of_inputs = []
counter = 1
while running:
    
    print('Enter paramters here!')
    print('\n')
    
    generated_reqs = generate_list_of_req(template)
    
    # display of template before user inputs
    print('Display of text: \n'+ just_show_brackets_with_index(template))
    print('\n')
    
    for i in generated_reqs:
        temp_element = input(str(counter) + ": Enter " + i + '   :')
        array_of_inputs.append(temp_element)
        counter+=1
    
    # list display of user inputs
    print('\n')    
    print('your input values: '+','.join(array_of_inputs))
    print('\n')
   
    print(input_new_values(file_converter(template), array_of_inputs))
    
    
    #File IO; creates a new text file with user inputs
    out_file = open('cover_letter_output_file_from_python.txt','w+')
    out_file.write(input_new_values(file_converter(template), array_of_inputs))
    out_file.close()    
    running = False