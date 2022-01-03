/*
This file is meant to house all javascript code that is shared 
across multiple files. The description of each function can be
found at the start of each function.

@author Noah Garcia-Galan
*/


/*
This function is responsible for setting the cookie
*@param {string} cname  - Cookie name
*@param {string} cvalue - Value of the cookie name
*@param {int}    exdays - Days until cookie will expire
*/
function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

/*
This function provides a fake captcha to bypass itsd issue
prompts the user to get the correct number to avoid auto
submissions
*/
function captch_impers(){

    //create random interval
    let randint = Math.floor(Math.random() * 10)

    //get guess from the user
    var guess = prompt(`Enter the number seen here: ${randint}`)

    //return based on what the user guessed
    if(guess == randint){return true;}
    else{return false;}
}

/*
This function will retrieve a cookie based on the cookie name
@param {string} cname - Name of cookie to check
*/
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

/*
This function will determine the validity of a input/form field
as defined by a css object
*@param {obj} obj - object to check validity of
*/ 
function valid(obj) {
    if (obj.validity && !obj.validity.valid) {
        return false;
    }
    else { return true; }
}

/*
Checks if a cookie exists or not
Redirects to message board if cookie exists
*/
function checkCookie() {
    let user = getCookie("UserPass");
    if (user != "") {
        window.location.assign("./messageboard.html");
    }
    
}

/*
Prevents access to pages not meant to be accessed without
first logging in. For the purposes of this project, this was
made specifically for message board
Redirects to login page if no cookie 
*/
function preventWithCookie() {
    let user = getCookie("UserPass");
    if (user == "") {
        window.location.assign("./loginpage.html");
    }
    
}