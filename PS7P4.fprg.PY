<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="PhotonUser"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2024-04-10 01:27:10 PM"/>
        <attribute name="created" value="UGhvdG9uVXNlcjtFQzJBTUFaLUxPOFEzRjQ7MjAyNC0wNC0wOTswOTo1MToyNiBQTTszMzI4"/>
        <attribute name="edited" value="UGhvdG9uVXNlcjtFQzJBTUFaLUxPOFEzRjQ7MjAyNC0wNC0wOTsxMDozMDo0NCBQTTszOzM0Mjc="/>
        <attribute name="edited" value="UGhvdG9uVXNlcjtFQzJBTUFaLU5KMU9LTTk7MjAyNC0wNC0xMDswMToyNzoxMCBQTTsxOzM0NDA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="response, response2, yes, name" type="String" array="False" size=""/>
            <declare name="rate, hours, totalpays, totalemployees, gross" type="Real" array="False" size=""/>
            <declare name="empcount" type="Integer" array="False" size=""/>
            <assign variable="totalpays" expression="0"/>
            <assign variable="totalemployees" expression="0"/>
            <output expression="&quot;Do you want to continue? Enter 'yes' to continue:&quot;" newline="True"/>
            <input variable="response"/>
            <while expression="response = &quot;yes&quot;">
                <output expression="&quot;Enter employee last name&quot;" newline="True"/>
                <input variable="name"/>
                <output expression="&quot;Enter employee rate of pay:&quot;" newline="True"/>
                <input variable="rate"/>
                <output expression="&quot;How many hours did the employee work?&quot;" newline="True"/>
                <input variable="hours"/>
                <if expression="hours &gt; 40">
                    <then>
                        <assign variable="gross" expression="gross + (hours-40) * rate * 0.5"/>
                    </then>
                    <else>
                        <assign variable="gross" expression="hours*rate"/>
                    </else>
                </if>
                <output expression="name" newline="True"/>
                <output expression="&quot;Your gross pay is $ &quot; &amp; gross" newline="True"/>
                <assign variable="totalpays" expression="totalpays+gross"/>
                <assign variable="totalemployees" expression="totalemployees+1"/>
                <output expression="&quot;Do you want to enter another employee? yes or no?&quot;" newline="True"/>
                <input variable="response"/>
            </while>
            <output expression="&quot;The total gross pays is $&quot; &amp;totalpays" newline="True"/>
            <output expression="&quot;Totoal number of employees entered&quot; &amp; totalemployees" newline="True"/>
        </body>
    </function>
</flowgorithm>
