#!/usr/bin/python
import cgi, template
import cgitb
import bleach
import string
cgitb.enable()


print ("X-XSS-Protection: 0;")
print ("Content-Type: text/html; charset=utf-8\r\n")
print
print template.header()

print template.navbar()

form = cgi.FieldStorage()
message = form.getvalue("message", "")
inputform = "<input type=\"text\" value=\""

print ("""

  <script>
    function myFrame() {
        var x = document.createElement("IFRAME");
        x.setAttribute("src", "http://www.bing.com/search?q=%s");
        x.setAttribute("class","embed-responsive-item");
        document.getElementById("demo").appendChild(x);
    }
    </script>

  """ % message)

print ("""

    <div class="page-header">
      <h1>XSS: <small>In JavaScript</small></h1>
    </div>
	""")

print("""
  <form action="xss3.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Bing search"  name="message" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">Search</button>
		</span>
	</div>
  </form>
  <hr>
""")

if message != "":

  print ("""
    <div class ="panel panel-default">
      <div class="panel-heading"><h3>Results</h3></div>
      <div class="panel-body">
        <div id="alert" class="alert alert-danger" role="alert" style="display:none;">Oh snap! Change a few things up and try submitting again.</div>
        <div id="demo" class="embed-responsive embed-responsive-16by9 demoframe">
        <script>
        try{
        myFrame();
        }
        catch(err){
        document.getElementById("demo").style.display = "none";
        document.getElementById("alert").style.display = "block";
        }
        </script>
        </div>
      </div>
    </div>
    """)

  cleanmessage = bleach.clean(message)
  l = [bleach.clean(s) for s in cleanmessage]
  cleanmessage2 = string.join(l,"")

  script1 = bleach.clean("""
  <script>
    function myFrame() {
        var x = document.createElement("IFRAME");
        x.setAttribute("src", "http://www.bing.com/search?q=""")
  script2 = """<i>%s</i>""" % cleanmessage
  script3 = bleach.clean("""");
        x.setAttribute("class","embed-responsive-item");
        document.getElementById("demo").appendChild(x);
    }
    </script>
    """)

  print (
    """

    <hr>

    <p>
      <div class="panel panel-danger">
       <div class="panel-heading">
        Incerted input incorrectly escaped.
       </div>
        <div class="panel-body">
         <pre>%s<i>%s</i>%s</pre>
        </div>
      </div>

    """ % (script1, script2, script3))

  script2 = """<i>%s</i>""" % cleanmessage2 

  print(
    """
      <div class="panel panel-success">
       <div class="panel-heading">
        Incerted input correctly escaped.
       </div>
        <div class="panel-body">
         <pre> %s<i>%s</i>%s</pre>
       </div>
      </div>
    </p>
    """ % (script1, script2, script3))

print template.footer()