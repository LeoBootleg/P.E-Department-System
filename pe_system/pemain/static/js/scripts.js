//REGISTRATION
function signup(){
    var name = document.getElementById('fullname').value;
    var user = document.getElementById('username').value;
    var password1 = document.getElementById('password').value;
    var password2 = document.getElementById('re-password').value;

    if (password1 != password2){
        xdialog.alert("Password does not match!");
    }else if (name == "" || user == "" || password1 == "" || password2 == ""){
        xdialog.alert("Please Input all the Neccessary Information Needed!");
    }
    else{
        location.href = "login.html";
    }
}

//BUY FORM
function buy(){
    var first = document.getElementById('firstname').value
    var last = document.getElementById('lastname').value
    var courses = document.getElementById('course').value
    var id = document.getElementById('idnum').value
    var contacts = document.getElementById('contact').value
    var emails = document.getElementById('email').value
    var quants  = document.getElementById('quantity').value
    
    if (first == "" || last == "" || courses == "" || id == "" || contacts == "" || emails == "" || quants == ""){
        xdialog.alert("Please Input all the Neccessary Information Needed!");
    }else{
        xdialog.alert("Successfully Submitted your information");
        document.getElementById('firstname').value = "";
        document.getElementById('lastname').value = "";
        document.getElementById('course').value = "";
        document.getElementById('idnum').value = "";
        document.getElementById('contact').value = "";
        document.getElementById('email').value = "";
        document.getElementById('quantity').value = "";
    }
}

//RESERVE FORM
function reserve(){
    var first = document.getElementById('firsts').value
    var last = document.getElementById('lasts').value
    var courses = document.getElementById('cours').value
    var id = document.getElementById('idnums').value
    var contacts = document.getElementById('conts').value
    var emails = document.getElementById('mail').value
    var ress = document.getElementById('res').value
    var date1 = document.getElementById('dateB').value
    var date2 = document.getElementById('dateC').value
    
     
    if (first == "" || last == "" || courses == "" || id == "" || contacts == "" || emails == "" || ress == "" || date1 == "" || date2 == ""){
        xdialog.alert("Please Input all the Neccessary Information Needed!");
    }else{
        xdialog.alert("Successfully Submitted your information");
        document.getElementById('firsts').value = "";
        document.getElementById('lasts').value = "";
        document.getElementById('cours').value = "";
        document.getElementById('idnums').value = "";
        document.getElementById('conts').value = "";
        document.getElementById('mail').value = "";
        document.getElementById('res').value = "";
        document.getElementById('dateB').value = "";
        document.getElementById('dateC').value = "";

    }
}

//BORROW FORM
function borrow(){
    var firsts = document.getElementById('f1').value
    var lasts = document.getElementById('l1').value
    var courses = document.getElementById('c1').value
    var id = document.getElementById('i1').value
    var contacts = document.getElementById('c2').value
    var mails = document.getElementById('e1').value
    var d1 = document.getElementById('date1').value
    var d2 = document.getElementById('date2').value


     if (firsts == "" || lasts == "" || courses == "" || id == "" || contacts == "" || mails == "" || d1 == "" || d2 == ""){
        xdialog.alert("Please Input all the Neccessary Information Needed!");
    }else{
        xdialog.alert("Successfully Submitted your information");
        document.getElementById('f1').value = "";
        document.getElementById('l1').value = "";
        document.getElementById('c1').value = "";
        document.getElementById('i1').value = "";
        document.getElementById('c2').value = "";
        document.getElementById('e1').value = "";
        document.getElementById('date1').value = "";
        document.getElementById('date2').value = "";

    }

}

//BLACKLISTED
function unblock(){
    xdialog.alert("Successfully Updated the Status");
    document.getElementById('block').innerText = 'Block';
}






