<HTML><HEAD>
<TITLE> Router Password Recovery</TITLE>
<META charset="utf-8">
<LINK rel="stylesheet" href="/style/form.css">
<STYLE type="text/css">
TR{ FONT-FAMILY: Arial;}
html, body{ margin: 0; border:none; background-color:#120203;background-image: url(../images/svg/bg.svg); background-attachment: fixed; background-size: cover; background-repeat: no-repeat; width:100%; height:100%}
</STYLE>
<script>
var quest1_1="$quest1_1";
var quest1_2="$quest1_2";
var quest1_3="$quest1_3";
var quest1_4="$quest1_4";
var quest1_5="$quest1_5";
var quest1_6="$quest1_6";
var quest1_7="$quest1_7";
var quest1_8="$quest1_8";
var quest1_9="$quest1_9";
var quest2_1="$quest2_1";
var quest2_2="$quest2_2";
var quest2_3="$quest2_3";
var quest2_4="$quest2_4";
var quest2_5="$quest2_5";
var quest2_6="$quest2_6";
var quest2_7="$quest2_7";
var quest2_8="$quest2_8";
var last_error_ans1="<% cfg_sed_xss("last_error_ans1") %>";
var last_error_ans2="<% cfg_sed_xss("last_error_ans2") %>";
var answer_again="<% cfg_get("enter_answer_again") %>";
function loadvalue()
{

	<% cfg_set("enter_answer_again","0") %>
	<% commit() %>

	if( answer_again == "1" )
		alert("$answer_not_match");
}
</script>
</HEAD>
<BODY onLoad="loadvalue()">
<div id="page_container">

<div class="wizard_body_container">
<div class="wizard_words_div">
<form method="post" action="/recover.cgi?/securityquestions.cgi">
<INPUT type=hidden name=submit_flag value="security_question">

<TABLE width="100%" border=0 cellpadding=0 cellspacing=3>
<TR><TD colSpan=2><H1>$router_password_recovery</H1></TD></TR>
<TR><TD colSpan=2></TD></TR>

<TR><TD colSpan=2>$complete_security_answers</TD></TR>
<TR><TD colSpan=2>&nbsp;</TD></TR>
<TR>
	<TD nowrap align="right" style="width: 250px;">$security_question_1*:</TD>
	<TD nowrap align="left">
	<script>
		var ques1="<% cfg_sed_xss("PWD_question1") %>";
		var ques1_str = eval('quest1_' + ques1);
		document.write(ques1_str);
	</script>
	</TD>
</TR>
<TR>
        <TD nowrap align="right">$answer *:</TD>
        <TD nowrap align="left">
        
        <script>
			if(answer_again == "1")
				document.write('<input type="text" maxLength="64" autocomplete="off" size="30" name="answer1" value="'+last_error_ans1+'" onFocus="this.select();" >');
			else
				document.write('<input type="text" maxLength="64" autocomplete="off" size="30" name="answer1" onFocus="this.select();" >');
		</script>
        </TD>
</TR>
<TR>
        <TD nowrap align="right">$security_question_2*:</TD>
        <TD nowrap align="left">
        <script>
                var ques2="<% cfg_sed_xss("PWD_question2") %>";
                var ques2_str = eval('quest2_' + ques2);
                document.write(ques2_str);
        </script>
        </TD>
</TR>
<TR>
        <TD nowrap align="right">$answer *:</TD>
        
        <TD nowrap align="left">                
		<script>
			if(answer_again == "1")
				document.write('<input type="text" maxLength="64" autocomplete="off" size="30" name="answer2" value="'+last_error_ans2+'" onFocus="this.select();" >');
			else
				document.write('<input type="text" maxLength="64" autocomplete="off" size="30" name="answer2" onFocus="this.select();" >');
		</script>
</TD>
</TR>
<TR><TD align="right">$required_information </TD> <TD></TR></TR>
<TR><TD colSpan=2>&nbsp;</TD></TR>
<TR> <TD colSpan=2>
<p><input class="cancel_bt" type='reset' name="Cancel" value=' $cancel_mark ' onClick='location.href="securityquestions.cgi";'>&nbsp;&nbsp;
<input class="apply_bt" type="submit" name="continue" value=" $continue_mark "></p>
</TD></TR>
</TABLE>
</form>
</div>
</div>
<div class="bottom_margin"></div>
</div>
</BODY>
</HTML>

