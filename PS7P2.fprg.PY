<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="PhotonUser"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2024-04-09 09:51:02 PM"/>
        <attribute name="created" value="UGhvdG9uVXNlcjtFQzJBTUFaLUxPOFEzRjQ7MjAyNC0wNC0wOTswOTozODo1MyBQTTszMzMz"/>
        <attribute name="edited" value="UGhvdG9uVXNlcjtFQzJBTUFaLUxPOFEzRjQ7MjAyNC0wNC0wOTswOTo1MTowMiBQTTsxOzM0MzA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, stop, inc" type="Integer" array="False" size=""/>
            <output expression="&quot;enter start value&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;enter stop value&quot;" newline="True"/>
            <input variable="stop"/>
            <output expression="&quot;Enter increment value&quot;" newline="True"/>
            <input variable="inc"/>
            <while expression="start &lt;= stop">
                <assign variable="start" expression="start+inc"/>
                <output expression="start" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>
