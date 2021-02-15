#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    
    if html == '':
        return True
    tags = _extract_tags(html)
    stack = []
    for tag in tags:
        text = tag[1:-1]
        if text[0] == '/':
            if len(stack) == 0:
                return False
            if text[1:] in stack:
                stack.pop()
        else: 
            stack.append(tag[1:-1])
    if tags and len(stack) == 0:
        return True
    else:
        return False

def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tag_list = []
    tag = ''
    is_tag = False

    for item in html:
        if item == '<':
            is_tag = True
        if item == '>':
            is_tag = False
            tag += item
            tag_split = tag.split(' ')
            if len(tag_split) > 1:
                tag = tag_split[0] + '>'
            tag_list.append(tag)
            tag = ''
        if is_tag == True:
            tag += item

    return tag_list
