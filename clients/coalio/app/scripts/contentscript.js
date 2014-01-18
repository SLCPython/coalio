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
		//console.log(post);

    	 $.ajax({
            url: 'https://coalio.metacogni.tv/api/tagged_post/?format=json&username=schart%40gmail.com&api_key=b6c56543a805dca901829d834554e987ab15bdce',
            type: 'post',
            dataType: 'json',
            contentType:"application/json; charset=utf-8",
            success: function (data) {
                console.log(data);
            },
            data: JSON.stringify(post)
        });
    	
   		$(this).find(".time").after(imgLink);
   		    $(this).find('.CoalioNo_Icon').balloon({
  			contents: '<a href="#'+tweetID+'">Block</a> <a href="#'+tweetID+'">Report</a> <a href="#'+tweetID+'">Talk</a>'
		});
	});
});

function Posting(username,id,text,domain)
{
this.bully_social_id=username;
this.resource_url=id;
this.content=text;
this.ref_url=domain;
}

function myAlerter() {
    alert('Why would you say that?');
}