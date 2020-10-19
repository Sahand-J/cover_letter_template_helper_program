#!/usr/bin/env python
# coding: utf-8

# @author Sahand-J
# easy version
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


# This method takes in the text file (or string text) of Cover Letter template 
# and formats it as with {} for .format method to work 
def file_converter(s):
    pars = s.split(']')
    reg = re.compile(r'\[[\s\S]*')
    empty = []
    for i in pars:
        empty.append(re.sub(reg,'{}',i))
    result = ''.join(empty)
    return result
     
# returns array of requirements between []    
def generate_list_of_req(s):
    res = re.findall(r"\[[^\]]*\]",s)
    return res


# formed_text = formatted text with {}
# sample_list = list of new user values
def input_new_values(formed_text, sample_list):
    return formed_text.format(*sample_list)

#helper method to show template with numbered brackets
def just_show_brackets_with_index(f):
    smod = replace_brackets(f)
    pars = smod.split(')')
    reg = re.compile(r'\([\s\S]*')
    empty = []
    counter = 1
    for i in pars:
        empty.append(re.sub(reg,'{'+ str(counter) + '}', i))
        counter+=1
    return ''.join(empty)
    
    
#replacing method - from stackOverflow
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

#replacing [] with {} for formatting reason
def replace_brackets(string_data):
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