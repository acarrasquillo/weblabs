#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi, template, cgitb, bleach, urllib
cgitb.enable()

print ("X-XSS-Protection: 0;")
print ("Content-Type: text/html; charset=utf-8\r\n")
print
print template.header()
print template.navbar()

form = cgi.FieldStorage()
query = bleach.clean(form.getvalue("query",""))
font = form.getvalue("font","100%")

font = urllib.unquote(font)

print ("""
    <div class="page-header">
      <h1>XSS: <small>On CSS</small></h1>
    </div>
	""")

print ("""
	<div class="btn-group btn-group-lg" role="group" aria-label="...">
  <button type="button" class="btn btn-default"><a href="?query=%(text)s&font=110%%">Bigger font</a></button>
  <button type="button" class="btn btn-default"><a href="?query=%(text)s&font=100%%">Normal font</a></button>
  <button type="button" class="btn btn-default"><a href="?query=%(text)s&font=90%%">Smaller font</a></button>
</div>
<hr>
""" % {'text':query})

print ("""
	<style>
		.cssSearch {font-size:""")

print 	font

print (""";
	</style>
	<div class="cssSearch">
	<form method="get">
		<div class="input-group">
		    <input type="text" class="form-control" name="query" aria-describedby="basic-addon1">
		    <span class="input-group-btn">
		    	<button class="btn btn-default" type="submit">Search</button>
		    </span>
		    <input type="hidden" name="font" value = \"""")
print font

print ("""\">
		</div>
		</form>
	<div class ="panel panel-default">
			<div class="panel-heading"><h3>Search results</h3></div>
			<div class="panel-body">
			Searched for""")

print query

print ("""
			</div>
		</div>

	<div class="panel panel-primary">
		<div class="panel-heading">
			<h5 class="panel-tittle">URL Encoding</h5>
		</div>
		<div class="panel-body">
			<p>	Hints:
				<ul>
				<li>URLs can only be sent over the Internet using the ASCII character-set.</li>
				<li>Since URLs often contain characters outside the ASCII set, the URL has to be converted into a valid ASCII format.</li>
				<li>URL encoding replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits.</li>
				<li>URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20.</li>
				</ul>
				<a href="http://www.w3schools.com/tags/ref_urlencode.asp">Reference</a>

			</p>
		</div>
	</div>
	</div>
	""")

#text1 = bleach.clean("<style>\n") + ".cssSearch {font-size:<i>%s</i>;}\n" % font + bleach.clean("</style>")
#text2 = bleach.clean("<style>\n") + ".cssSearch {font-size:<i>%s</i>;}\n" % font + bleach.clean("</style>")

print("""
	 <div class="panel panel-danger">
       <div class="panel-heading">
        Incerted input incorrectly escaped.
       </div>
        <div class="panel-body">
         <pre>""")

print bleach.clean("<style>")
print "    .cssSearch {font-size:<i>", font, "</i>;}"
print bleach.clean("</style>")

print ("""</pre>
        </div>
      </div>

	<div class="panel panel-success">
       <div class="panel-heading">
        Incerted input correctly escaped.
       </div>
        <div class="panel-body">
         <pre>""")

print bleach.clean("<style>")
print "    .cssSearch {font-size:<i>", font, "</i>;}"
print bleach.clean("</style>")

print ("""</pre>
       </div>
      </div>
	""")
print template.footer()
