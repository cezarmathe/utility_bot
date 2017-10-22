

import re


def args_array(text):
    return re.compile('\w+').findall(text[1:])

def args_text(text):
	x = args_array(text)
	output = ""
	y = len(x)-1
	for i in range(y):
		output = output + " " + x[i+1]
	return output

