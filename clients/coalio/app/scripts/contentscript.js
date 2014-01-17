'use strict';

chrome.runtime.sendMessage({ action: "show" });

$(function () {
    //Code for displaying <extensionDir>/images/myimage.png:
    var imgURL = chrome.extension.getURL("images/no_icon.gif");
    //$(".tweet").css("border", "13px solid red");
    var imgLink = "<img onclick='no_Icon_Clicked()' class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>";
    $(".time").after(imgLink);
    $(".UFILikeLink").after(imgLink);
    $(".lea").after(imgLink);
});