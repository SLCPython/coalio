'use strict';

chrome.runtime.sendMessage({ action: "show" });

//chrome.runtime.sendMessage({ action: 'report' });

function reportTweet(post){
	console.log(post);
	
	    	$.ajax({
            url: 'https://coalio.metacogni.tv/api/tagged_post/?format=json&username=schart%40gmail.com&api_key=b6c56543a805dca901829d834554e987ab15bdce',
            type: 'POST',
            dataType: 'json',
            contentType:"application/json",
            success: function (data) {
                console.log(data);
            },
            error:function(  jqXHR,  textStatus,  errorThrown ){
            	console.log(jqXHR);
            	console.log(textStatus);
            	console.log(errorThrown)
            },
            data: JSON.stringify(post)
        });

}

$(function () {

    //Code for displaying <extensionDir>/images/myimage.png:
	var imgURL = chrome.extension.getURL("images/no_icon.gif");
	var imgLink = "<img class='CoalioNo_Icon' src='" + imgURL + "' alt='no'>";
 
    $(".UFILikeLink").after(imgLink);
    $(".lea").after(imgLink);
	$('.js-stream-item').each(function(){
		var tweetobj = $(this).find("div.tweet")[0];
		var tweetAuthor = $(tweetobj).attr('data-screen-name');
		var tweetID = $(this).attr('data-item-id');
		var tweetText = $($(this).find("p.tweet-text")[0]).html();
		
		var post =  new Posting(tweetAuthor, tweetID, tweetText, 'https://twitter.com/'+tweetAuthor+'/status/'+tweetID);
		   //console.log(this);
   		   $(this).find(".time").after(imgLink);
   		    $(this).find('.CoalioNo_Icon').balloon({
  				contents: '<span>Click to report bullying behavior.</span>'
			});

   		    $(this).find('.CoalioNo_Icon').on("click", function(){
			reportTweet(post)
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