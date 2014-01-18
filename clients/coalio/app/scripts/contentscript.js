'use strict';

chrome.runtime.sendMessage({ action: "show" });

//chrome.runtime.sendMessage({ action: 'report' });

$(function () {
    //Code for displaying <extensionDir>/images/myimage.png:
	var imgURL = chrome.extension.getURL("images/no_icon.gif");
	var imgLink = "<img class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>";
 
    $(".UFILikeLink").after(imgLink);
    $(".lea").after(imgLink);
	$('.js-stream-item').each(function(){
		var tweetID = $(this).attr('data-item-id');
		var tweetText = $($(this).find("p.tweet-text")[0]).html();
		var tweetAuthor = $(this).attr('data-screen-name');
		var post =  new Posting(tweetAuthor, tweetID, tweetText, 'twitter.com');
		#console.log(post);

    //$(".tweet").css("border", "13px solid red");
    	
   		$(this).find(".time").after(imgLink);
   		    $(this).find('.CoalioNo_Icon').balloon({
  			contents: '<a href="#'+tweetID+'">Block</a> <a href="#'+tweetID+'">Report</a> <a href="#'+tweetID+'">Talk</a>'
		});
	});
});

function Posting(username,id,text,domain)
{
this.username=username;
this.id=id;
this.text=text;
this.domain=domain;
}

function myAlerter() {
    alert('Why would you say that?');
}