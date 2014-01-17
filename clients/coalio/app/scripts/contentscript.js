'use strict';

$(function () {
    //Code for displaying <extensionDir>/images/myimage.png:
    var imgURL = chrome.extension.getURL("images/no_icon.gif");
    //$(".tweet").css("border", "13px solid red");
    $(".time").after("<img onclick='no_Icon_Clicked()' class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>");
    $(".UFILikeLink").after("<img onclick='no_Icon_Clicked()' class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>");
});