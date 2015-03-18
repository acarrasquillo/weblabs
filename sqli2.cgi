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
print """<p><font size="3">The following box asks the user for an input. The developer, again, forgot to sanitize the inputs.
          We need to show him that input validation is important, so I have a task for you. You need to get the information of
          all the students and professors."""

print """<p><font size="2">Hint: The Professor and the User table have the same amount of columns and the same types maybe you can
          make a compund query.<font></p>"""

print("""
 <form action="sqli2.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="sudent number"  name="num_estudiante" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">LogIn</button>
		</span>
	</div>
</form>""")

if form.has_key("num_estudiante"):
  # Try to do an injection here with Union to show the data of all students and professors
  query = """SELECT * FROM User WHERE num_estudiante = "%s" """ % stuNum

  c.execute(query)
  result = c.fetchall()

  print """<div class="panel panel-danger">
    <div class="panel-heading">
    The query:
    </div>
    <div class="panel-body">
      <pre>SELECT * FROM User WHERE num_estudiante = "<font color="red">%s</font>"</pre>
    </div>
        
    </div>""" % stuNum

  print ("""
    <p><font size="3">Your Information: </font></p>
    """)
  print """<table class="table table-condensed">"""
  print """<tr><th>Name</th><th>Username</th><th>Email</th><th>Direction</th><th>Password</th><th>Age</th><th>Student Number</th></tr>"""
  for e in result:
    print """<tr>"""
    for i in range(1,len(e)-1):
      print """<td>%s</td>""" % e[i]
    print """</tr>"""
  print """</table>"""


print template.footer()

c.close()
