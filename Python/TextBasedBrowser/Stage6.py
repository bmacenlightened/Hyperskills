import sys
import os
from bs4 import BeautifulSoup
import requests as requests
import colorama

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    tag_list = ['p', 'a', 'h1', 'h2', 'h3', 'h3', 'h4', 'h5', 'h6', 'h7', 'ul', 'ol', 'li']
    tags = soup.findAll(tag_list)
    for el in tags:
        if el.name == "a":
            print(colorama.Fore.BLUE + el.get_text())
        else:
            print('\033[39m' + el.get_text())
    return [el.get_text() for el in tags]

def main(directory_name):
    saved_files = []
    history = []
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    command = input()
    while True:
        if command == "exit":
            break
        elif command == "back":
            if len(history) != 0:
                history.pop()
                page = history[len(history)-1]
                with open(f'./{directory_name}/{page[:-4] + ".txt"}', 'r') as f:
                    print(f.readlines())
        elif command in saved_files:
            with open(f'./{directory_name}/{command}.txt') as f:
                print(f.readlines())
        elif '.' not in command:
            print("Error: Incorrect URL")
        elif "https://" not in command:
            url = "https://" + command
            with open(f'./{directory_name}/{command[:-4]+".txt"}', 'w') as f:
                r = requests.get(url)
                content = parse(r.text)
                f.writelines(content)
                saved_files.append(command[:-4])
                history.append(command)
        else:
            print("Error: Incorrect URL")
        command = input()




if __name__ == "__main__":
    directory_name = sys.argv[1]
    main(directory_name)
