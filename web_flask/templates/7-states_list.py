!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL id="State">
        {% for item in State %}
            <LI>"{{ item.id  }}: "><B>"{{ item.name }}"</B></LI>
        {% endfor %}
        </UL>
    </BODY>
</HTML>

