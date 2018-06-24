# Code Jam 2: Mythology API

Welcome to the second [Python Discord code jam](https://pythondiscord.com/jams)!

The theme for this code jam will be **mythology**. That means you're going to be creating a **RESTful API in Flask with 
a mythology theme**.

For example, you might create the **The Mimír API**, an API used to look up information about norse gods and godesses.

If you send it a POST request with {"name": "kvasir"}, it might respond with 
```json
{
    "name": "Kvasir",
    "parents": "Born from the saliva of the Æsir and the Vanir",
    "type": "A god of wisdom and knowledge"
}
```

The API must respond with json data, but this is not limited to text. It could respond with byte data, with a URL to an 
image, a video or some audio, or with any other form of data you deem interesting.

The API should accept *at least* a GET or a POST request with JSON data. You are allowed to use any third party 
libraries you want - don't forget to add them to the project's requirements!

# Where Do I Begin?

You should start by forking this repo. Then all the members of your team should clone your fork. You should then make 
a merge request from your master branch into this repos master branch. We recommend that you all make branches for each 
feature and then merge those feature branches into your master. As you make changes to your master, the merge request 
will update and we will be able to see what you've been working on. It is therefore important that these changes are 
merged into master frequently, because the staff will be looking through the merge requests and making helpful comments 
and suggestions that you should be paying attention to.

Remember, creativity counts. Try to have fun with it. We're not necessarily looking for dead serious solutions only, 
and it's okay if your solution is only tangentially related to the theme, so long as there's a relationship of some 
sort.

Good luck - and if you get stuck, feel free to grab a staff member and ask for help. We'll be answering your 
questions all week!

# Project Structure

Please ensure that your project code is placed within the `proj` module. We've included an empty module with that name
in this repository for you - while this is optional, you'll have much less trouble from our linter if you stick with
it.

Due to the issues some users had with Pipenv in the last jam, we're sticking with a simple `requirements.txt` file
this time - something many of you should already be familiar with. We do recommend that you use a virtualenv for
while you work on your project, but how you set up your development environment is - of course - up to you.

If you're not familiar with `requirements.txt`, you can install it using `python -m pip install requirements.txt`.

# Code Formatting

As in our previous code jam, we recommend everyone follows the well-known PEP8 style guide. To that effect, we've
included a `tox.ini` and a `requirements-dev.txt` that will help you to keep your code clean and orderly.

Install the development requirements with `python -m pip install -r requirements-dev.txt`. When you want to check
whether your code is styled correctly, simply run `flake8` from within the project folder. Please note that we are
also automatically checking your code when you submit it as part of your merge request - you can look at your
merge request at any point to check whether your code is styled correctly. The testing procedure is known as
Continuous Integration, and your code is checked within a "Pipeline" - your merge request will show the status
of the last Pipeline run. If it failed, check that your code is styled correctly!

The included `tox.ini` is set up as follows:

* [Import ordering style](https://github.com/PyCQA/flake8-import-order#styles) of `pycharm`
* Maximum line length of **120 characters**
* Project module name of `proj`
* The following ignored errors:
    * `B311`: Possibly insecure use of pseudo-random number generator
    * `E226`: Missing whitespace around arithmetic operator
    * `P102`: Docstring contains unindexed parameters
    * `S311`: Older version of `B311`
    * `W503`: Line break before binary operator
