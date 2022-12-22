# BusinessHelper
<h3>Highly recommended to run it through Docker</h3>
<h6>Steps:</h6>
<ul>
<li>docker-compose up</li>
<li>Port 8000 should be open in your localhost. Type 127.0.0.0:8000 on the browser to access the project</li>
</ul>
<pre>Potential errors (if NOT run through Docker):</pre>
<ul>
<li>no such table : /sec/user -> solution: py manage.py migrate --run-syncdb</li>
</ul>
