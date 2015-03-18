#!/usr/bin/python
import cgi, string
import template
import cgitb
import bleach
cgitb.enable()

print ("X-XSS-Protection: 0;")
print ("Content-Type: text/html; charset=utf-8\r\n")
print

# form = cgi.FieldStorage()

# hola = form.getvalue("cheo")

# print ("hola")
print template.header()

print template.navbar()

print("""
    <div class="page-header">
  <h1>XSS: <small>In attributes</small></h1>
</div>
	""")

form = cgi.FieldStorage()
message = form.getvalue("message", "")

print("""
 <form action="test.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Input text"  name="message" aria-describedby="basic-addon1" value="%s">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">Search</button>
		</span>
	</div>
</form>

""" % message)

if message != "":
  print (
    """
    <p>
      <div class="panel panel-danger">
       <div class="panel-heading">
        Incerted input incorrectly escaped.
       </div>
        <div class="panel-body">
         <pre> &lt;input type=\"text\" value=\"<i>%s</i>\"&gt;</pre>
        </div>
      </div>

    """ % str(bleach.clean(message)) 
    )
  cleanmessage = bleach.clean(message)
  l = [bleach.clean(s) for s in cleanmessage]
  cleanmessage2 = string.join(l,"")
  print(
    """
      <div class="panel panel-success">
       <div class="panel-heading">
        Incerted input correctly escaped.
       </div>
        <div class="panel-body">
         <pre> &lt;input type=\"text\" value=\"<i>%s</i>\"&gt;</pre>
       </div>
      </div>
    </p>
    """ % cleanmessage2
    )


print template.footer()