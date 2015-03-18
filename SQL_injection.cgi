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
user = form.getvalue("username", "(no username)")
passw = form.getvalue("password", "(no password)")

print """<H3><u>Instructions</u>:</H3>"""
print """<p><font size="3">The following boxes asks the user for inputs. Unfortunatley the developer of the web page didn't sanitize the input, so
            the web page is vulnerable to SQL injections. A bad person, <b>NOT YOU GUYS</b>, can use this to get the information of all the
            students and the professors in the database. Try to get out the information of all the students with a SQL Injection.<font></p><br>"""

print """<p><font size="2">Hint: The query is made by 2 parts. To make the query true you have to make both inputs true.<font></p>"""

print("""
 <form action="SQL_injection.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="username"  name="username" aria-describedby="basic-addon1">
    <input type="password" class="form-control" placeholder="password"  name="password" aria-describedby="basic-addon1">
		<div class="btn-group">
			<button type="submit" class="btn btn-default">LogIn</button>
		</div>
	</div>
</form>""")

if form.has_key("username") & form.has_key("password"):
  # The injection can be made by making username and password true
  query = """SELECT * FROM User WHERE username = "%s" AND password = "%s" """ % (user, passw)

  c.execute(query)
  result =  c.fetchall()

  print """<div class="panel panel-danger">
    <div class="panel-heading">
    The query:
    </div>
    <div class="panel-body">
      <pre>SELECT * FROM User WHERE username = "<font color="red">%s</font>" AND password = "<font color="red">%s</font>"</pre>
    </div>
        
    </div>""" % (user, passw)

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
