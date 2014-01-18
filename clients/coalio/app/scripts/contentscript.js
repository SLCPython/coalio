'use strict';

chrome.runtime.sendMessage({ action: "show" });

//chrome.runtime.sendMessage({ action: 'report' });

function reportTweet(post){
	console.log(post);
	
	    	$.ajax({
            url: 'http://coalio.metacogni.tv/api/tagged_post/?format=json&username=schart%40gmail.com&api_key=b6c56543a805dca901829d834554e987ab15bdce',
            type: 'POST',
            dataType: 'json',
            contentType:"application/json",
            success: function (XMLHttpRequest, textStatus) {
    			var headers = XMLHttpRequest.getAllResponseHeaders();
    			//console.log(headers);
            },
            complete: function(  jqXHR,  textStatus,  errorThrown ){
            	var headers = jqXHR.getAllResponseHeaders();
            	headers = headers.split("\n");
            	var gourl = null;
            	headers.forEach(function(h) {
            		//console.log(h);
            		//console.log(h.search("Location:"));
    				if(h.search("Location:") > -1 && gourl == null)
    				{

    					gourl = h.replace("Location: ", "");
    				}
				});
				gourl = gourl.replace("api/tagged_post", "taggedposts");
				console.log(gourl);
				if(gourl != null)
				{

					  var win=window.open(gourl, '_blank');
  						win.focus();
				}
					///chrome.tabs.create({ url: gourl });
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