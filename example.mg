LANGUAGE MARKGO
'This is a template of this language'
'A language code such as "LANGUAGE MARKGO" is
required to explain this language'

'!HEAD is the <head> tag in html'

!HEAD.set.title:"Test doc";
'set title by set'

!HEAD.import.js:"./script.js";
!HEAD.import.css:"./style.css";
'import is used to import files'

'!CREATE can be used to create variables'
#CREATE.a;

'? can be used to read and set the variables'
?a = "5";

#CREATE.p;

'Setting variable p to a <p> element'
?p = <NEW-ELEMENT p>;

'Use < operator to insert the texts'
?p < Hello, world!;

#CREATE.b;

?b = <NEW-ELEMENT b>;

?b < Bold Text.;

?p < ?b;

!BODY.add.child:?p;
