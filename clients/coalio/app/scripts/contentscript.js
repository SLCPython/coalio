'use strict';

chrome.runtime.sendMessage({ action: "show" });

//chrome.runtime.sendMessage({ action: 'report' });

$(function () {
    //Code for displaying <extensionDir>/images/myimage.png:
    var imgURL = chrome.extension.getURL("images/no_icon.gif");
    //$(".tweet").css("border", "13px solid red");
    var imgLink = "<img onClick='myAlert()' class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>";
    $(".time").after(imgLink);
    $(".UFILikeLink").after(imgLink);
    $(".lea").after(imgLink);
});

function myAlert() {
    alert('Why would you say that?');
}