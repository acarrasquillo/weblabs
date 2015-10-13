# cyberlabs

---
author:
- |
    Abimael Carrasquillo-Ayala\
    `abimael.carrasquillo@gmail.com`\
    Ricardo De La Vega\
    **advisor**\
    José Ortiz-Ubarri\
    `cheo@hpcf.upr.edu`\
    University of Puerto Rico, Río Piedras\
    School of Natural Sciences\
    Department of Computer Science\
    Computer Security Lab (CSLab)
date: |
    **CCOM 4995 | Spring 2015**\
    Undergraduate Research\
title: '**CyberLabs**'
...

The Academics and Training for the Advancement of Cybersecurity
Knowledge in Puerto Rico (ATACK-PR) project at the University of Puerto
Rico, Río Piedras Campus focus on the education of the cybersecurity
field to the students at campus. This CyberLabs project by undergraduate
students is a work focused on the creation of cybersecurity laboratories
on the topics of SQL injection, Cross Site Scripting (XSS) and input
validation. This report will talk about XSS and input validation.

Introduction
============

This project provides different laboratories that students can utilize
for applying cybersecurity concepts. The topics developed are SQL
injection, Cross Site Scripting (XSS) and input validation. This report
will only discuss the last two. The laboratories were created as a web
aplication running a *CGI HTTP Server* usign *HTML* and *Python* and
Javascript programming languages. There are four Cross-Site scripting
laboratories and one lab on input validation.

Methodology
===========

This section will show some examples of the cross-site scripting (XSS)
laboratories as well as the input validation. It will discuss the idea
of the laboratories and how the unwanted behavior or functionality
should be prevented.

Cross-Site Scripting (XSS)
--------------------------

When designing a web applications, the developer must be carefull with
the inputs on any html form. If the developer doesn’t design a secure
web application it can create vulnerabilities that will allow users to
exploit them and inject code on the web page. Something that can change
the application original purpose and lead to unwanted behavior and
functionality. As an example on Figure \[fig:xsstags\], the html form
doesn’t escape correctly the inserted text on the html form. This
allowed the user to insert a image on the webpage, for this case this
type of behavior should not occur as the application purpose was to
display the text inserted by the user.

![XSS between html tags<span data-label="fig:xsstags"></span>](xsstags)

As show on Figure \[fig:xsstags\], the user input was:\
\
this input cointains *HTML* tags, that if are not correctly escaped, the
user web browser will interpret them and treat them as *HTML* code. This
type of behavior can be eliminated by correctly escaping the form input
text. On the last example the input could be changed to:\
\
what this does is escape the *HTML* tags inside the text inserted on the
form. This will encode the tags in a format that the web browser will
not interpret them as *HTML* code. As show on Figure
\[fig:correctxsstags\], if the correctly escaped input is provided the
web browser will display it as text and the tags will no be interpreted.
To escape the inserted text on the form, *bleach* *Python* package was
installed utilizing the command `$ pip install bleach`. Here is an
example of how user input can be clean on a *Python* cgi script that
contais a form where the value of the input text is *message*:\
`bleach.clean(form.getvalue("message",""))`\
the `bleach.clean()` routine sanitize the input text, correctly escaping
the html tags providing security and eliminating unwanted behavior.\
XSS not only occurs in HTML tags, also inside HTML attributes, on CSS
and Javascript code can be found, figure \[fig:xssattributes\] show an
example of XSS on *HTML* attributes.

![XSS between html tags<span
data-label="fig:correctxsstags"></span>](correctxsstags)

![XSS on html attributes<span
data-label="fig:xssattributes"></span>](xssattributes)

Input Validation
----------------

The input validation laboratory allows the user to insert a student
number and see the student assigments. The student goes to the main page
and submits the student id, see figure \[fig:popensid\]. A list of
essays is shown and the user can open them for reading, see Figure
\[fig:essay\]. The problem here is that this application is using a
system call to the computer operating system using the *Python*
*popen()* routine. Because there is no input validation the input is
passed as a parameter to this routine without validation. This routine
allows to make more than one system call by separating them usign the
`';'` character. As an example the user can insert: and also read all
the files located at `/ect/`, see Figure \[fig:vulnerbility\].\
This can be solve validating the user input, the next code snippet shows
how the data inserted is managed in the *Python* script:

    1 stuid = form.getvalue("stuid", "")
    2 homeworks = os.popen("ls %s/" % stuid)

Here there is no input validation, so the user can use the input showed
earlier and exploit the application vulnerability. The next snippet
shows how to correctly validate the user input and eliminate the
vulnerability:

    1 stuid = form.getvalue("stuid", "")
    2 if is_int(stuid):
    3     homeworks = os.popen("ls %s/" % stuid)

Here the student id is checked to validate that it contains a valid
integer number, by this the user will not be able to use the `';'` and
make more than one system call or read directories that it should not be
allowed.

![Input validation laboratory student id form<span
data-label="fig:popensid"></span>](popensid)

![Input validation laboratory student essay<span
data-label="fig:essay"></span>](essay)

![Input valdation vulneravity<span
data-label="fig:vulnerbility"></span>](vulnerbility)

Conclusion
==========

CyberLabs is a project that will allow students that are on the
cybersecurity introductory course have a hands on experience with SQL
injection, input validation and cross-site scripting. Here the last two
were discussed, and some examples of the vulnerabilities created and the
aproach to solve them were provided. This secured the application of
allowing unwanted behavior that affected the main purpose and user
experience.

Acknowledgement {#acknowledgement .unnumbered}
===============

This work is supported by the scholarship Academics and Training for the
Advancement of Cybersecurity Knowledge in Puerto Rico (ATACK-PR)
suported by the National Science Foundation under Grant No. DUE-1438838.

<span>widestlabel</span> OWASP *Cross-Site Scripting*\
*source:* `https://www.owasp.org/index.php/Main_Page` Insecure Labs
*source:* `research.insecurelabs.org/xssmas/` Google Inc. *Cross-Site
Scripting – Application Security*\
*source:* `www.google.com/about/appsecurity/learning/xss/#BasicExample`
Google Inc. *Web Application Exploits and Defenses*\
*source:* `https://google-gruyere.appspot.com/part1`

