# comments
A tool to download the comments on a Youtube video.

#### Video Demo: [https://youtu.be/oF1toVFdgEY](https://youtu.be/oF1toVFdgEY)

#### Description

This is a tool to download the youtube comments on a video.

Let's take a look at the imports

```py
import re
from os import path
from colorama import Fore as c
from googleapiclient.discovery import build
from tqdm import tqdm
import csv
from sys import exit
```
Nothing noteable in these epart from the googleapiclient.discovery module.
I'm importing this to access the youtube api v3.


From the top of the project.py let's take a look at all the functions.

### ValidateApi()
This function as the name suggests is responsible for validating the api that a user has provided. To accomplish this it takes the user's input and makes a dummy request to the google api requesting for 0 comments.

If the request executes successfully then we can be sure that user has input the valid api key , if it does not then we raise an exception saying the api key is invalid and exit the program.

### getKey()
This function is used to prompt the user to input their api key.
While designing this program i had to choose how to store the api key that user enters in the best way possible. I ended up choosing to make a `.env` file as it is a dot file it's hidden by default in unix systems and also conventionally used to store environment variables such as api keys.

So the get key function prompts the user to input their api key , validates the key and then saves it inside the `.env` file.
Now if the getKey function is called any other time it just checks the existence of the `.env` file and if the file exists then it means that user has aleady input and validated their api key once so it does not prompt them for it again.


### URL validation and getting the video id from a given url
in a typical youtube url as `https://youtu.be/oF1toVFdgEY` or `https://www.youtube.com/watch?v=oF1toVFdgEY` the `oF1toVFdgEY` part is considered as the video id and is required while making a request to the api.
I have used regex to accomplish this , there's nothing much to explain as the regex is write once and forget kind of a deal , if i ever need to maintain / modify it in the future i'm just going to start wrting it from scratch.

### Exiting the program
I have also written a function called `exitProg` which is basically a wrapper over the existing exit function. This is what it looks like.

```py

def exitProg(reason="", code=0):
    if reason:
        print(c.RED + reason)

    print(c.RED + "\nExiting the Program . . " + c.WHITE + ".")
    exit(code)
```
This is mainly because while writing the code for this project i found myself exiting the program due to several exceptions and decided to make a function out of it that i can call whenever i needed to do the same.


### Actually getting the comments
So the function `getComments` is responsible for making the request to the google api and then formatting the response into a csv file.

While deciding what data to request from the google api i have decided to not get the replies to a comment.
That is because the purpose of this program is to get the comments upon which we are going to perform sentiment analysis.

In a case where a youtube vide is positive but the comment to that youtube video is a negative one and then the there might be replies to that negative comment which may further be negative as they might argue with the comment poster.
If i consider all these replies as comments to the youtube video it would skew the result of the sentiment analysis program.
This is what i mean

```
Top level comment [negative]
    Subcomment [negative]
    subcomment [negative]
```
When the api returns the data and after formatting it it would look like

```
Top level comment [negative]
Subcomment [negative]
subcomment [negative]
```
Due to the way data can be stored in csv files the subcommment also essentially becomes a top comment and it appears as if it is replying to the youtube video itself instead of another comment.

---
Another limitation with the youtube api is that at a time you can only request up to a 100 comments from the api.

So if i want to collect all the comments on a youtube video , the response has a field called nextPageToken and i have to use that token to perform continous requests to the api until there's no nextPageToken field in the response.

That is why inside the getComments function there's two inner functions
one is called `getSomeComments` and the other one is `getAllComments`.

The function names are pretty self explainatory in that getsomecomments is called when the user is requesting less than 100 comments and getAllComments is used when all the comments are required.

### main

This is about it , there's nothing special about the main function it is just calling all the other functions in the desired order.

---

# TODO
The project is still incomplete as the functionality is implemented but i am not happy with the way it's designed , i want to use OOP and design this program in a better way and then upload it to pypi as a python package.
Will be working on that in the fututre but for now this is fine.
