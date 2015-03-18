#!/usr/bin/python
# This program is for lab purposes only. This isnt a secure way to implement
# querys in a application because it is open to atacks by SQL Injection

import cgi
import cgitb
cgitb.enable()
import MySQLdb
import template

print """Content-Type: text/html"""
print

print template.header()

print template.navbar()

# First we create a connection object (db) that represents the database
db = MySQLdb.connect("localhost", "jdelavega", "6TsseuXp", "atackpr_sqlin")

# Once we have a connection with the database, we can create a cursor object (c)
# this cursor will let us use the execute() method to perform SQL commands
c = db.cursor()

form = cgi.FieldStorage()
stuNum = form.getvalue("num_estudiante", "(no student number)")

print """<H3><u>Instructions</u>:</H3>"""
print """<p><font size="3">The following box asks the user for an input. Only students can that are members of this club can see the 
            essays in this page. Try to insert a new user in the database with the member value set to 1 so that you have access to the 
            essays. Once you insert a user try again using that user."""

print("""
 <form action="sqli3.cgi" method="post">
  <div class="input-group">
    <input type="text" class="form-control" placeholder="sudent number"  name="num_estudiante" aria-describedby="basic-addon1">
    <span class="input-group-btn">
      <button class="btn btn-default" type="submit">LogIn</button>
    </span>
  </div>
</form>""")

if form.has_key("num_estudiante"):
  # Try to do an injection here with Union to show the data of all students and professors
  query = """SELECT member FROM User WHERE num_estudiante = "%s" """ % stuNum

  c.execute(query)
  result = c.fetchall()

  print """<div class="panel panel-danger">
    <div class="panel-heading">
    The query:
    </div>
    <div class="panel-body">
      <pre>SELECT member FROM User WHERE num_estudiante = "<font color="red">%s</font>"</pre>
    </div>
        
    </div>""" % stuNum

  if len(result) > 0:
    if result[0][0] == 1:
      query = """SELECT * FROM Essay"""
      c.execute(query)
      result = c.fetchall()
      for e in result:
        print """<div class="jumbotron">"""
        print """<h3>%s</h3>""" % e[1]
        print """<p>%s</p>""" % e[3]
        print """<p>Author: %s</p>""" % e[2]
        print """</div>"""
        print """<br>"""


print template.footer()

try:
  c.close()
except:
  pass