# Haiku Poem Generator

![](assets/images/haiku.png)

### Table of Contents

<!-- TOC -->
* [Haiku Poem Generator](#haiku-poem-generator)
    * [Table of Contents](#table-of-contents)
    * [What is a Haiku](#what-is-a-haiku)
    * [How to Run the Program (For Beginners)](#how-to-run-the-program-for-beginners)
        * [How to use the Program](#how-to-use-the-program)
            * [Interviewing Logic](#interviewing-logic)
<!-- TOC -->

### What is a Haiku

For people who don't know what a Haiku is, a Haiku is one type of japanese
poetry. This Haiku generator can generate random haiku poems for you to 
get an idea of what poem to write, sing it out loud to someone or just
read it yourself for fun when you're bored!

### How to Run the Program (For Beginners)

If you're using the Pycharm IDE and you're new to it, you probably might 
not know how to run the .py files. Well, it's pretty simple. Firstly, go
to the main.py file. You can select the button below to open it straight
away.

[Open main.py File](main.py)

Next, in the toolbar, find a green lay button. Then select it and the
program should just basically run the program in the IDE's console.

#### How to use the Program

This program isn't very complicated. Once you've ran the program in the
console, it'll ask you your name. If it's your first time using the
program, it'll interview you. 

##### Interviewing Logic

But how would it know if it's your first
time using it. Well, in the config.py file, I created a constant (a
variable) called TIMES_USED that contains a number which is 1 or 0. You 
can open the config.py file by selecting the button below.

[View config.py](config.py)

If it's you're first time using the program, set the variable to 0. After
you've finished using the program, go back to the config.py file and set
that exact same variable to 1. Now here's how the main.py uses that and
checks if you've used it once. I added 2 if statements  from line 59 to 
line 64. Now, the first if statement means that if the TIME_USED variable
is = to 1, it'll just use the `ask_name()` function. This `ask_name()`
function contains the following code:

`def ask_name():
    name = input("What's your name? ")
    print("Hello " + name + " !")
`

Now for the 2nd if statement means that if the TIMES_USED variable is = to
0, it'll use the `ask_name()` function and also the `interview()` function.
Now we know what the `ask_name()` function does but what about the `interview()`
function. This `interview()` function contains the following code:

`def interview():
    print("Since you are new to this, we'd like to interview you.")
    reason_for_using_this = input("Why are you using this?\n[Write a poem]\n[Just listen to a poem]\n[Other]\n")
    do_you_know_haiku = input("Do you know what a haiku is?\n[y]es\n[n]o\n")
    how_did_you_find_this = input("Where did you find this?\n[Github]\n[Rudy's Tech Website]\n")`


### Author

You can read more about me, RudhraPNerd in the author.md file. Select the
button down below to view the author.md file.

[View author.md](author.md)

### Feedback

Think there's something else to be added or fixed?
Complete and submit the Haiku Poem Generator Feedback
form to give me feedback on what to change for the
project to make it even better and more enjoyable for
the user to use. Your feedback can make a huge
difference. Select the button down below to open up
the feedback form in Microsoft Forms in your browser.

<a href="https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAa__TyDYVtUNEUxVTFZUk5SOVZVTkM3UTNQMkhJTjRCVy4u" class="button">Go to Form</a>

<style>
.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #4CAF50; /* Green */
  border: none;
  border-radius: 8px;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}

.button:hover {
  background-color: #45a049;
}
</style>

