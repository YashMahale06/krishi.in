
print "Content- type: text/html\n\n";
import cgi
form=cgi.FieldStorage()
name=form.getvalue("name")
password=form.getvalue("password")
print name+"From python"