
//hot keys
document.onkeyup = function(e) {
  var key = e.which || e.keyCode;
  
  var base_url = window.location.origin;
  var host = window.location.host;
  var url = window.location.href;
  var slash = "/";
  var list = url.split("/");
  var x = list.length;
  var number = list[x -3];
  
  
  
  //set band to 10 with 0 and ctrl
  if( e.ctrlKey && key ==48){
	  var band = 10
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 11 with 1 and ctrl
  else if(key ==49 && e.ctrlKey){
	 var band = 11
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 12 with 2 and ctrl
  else if(key ==50 && e.ctrlKey){
	  var band = 12
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 13 with 3 and ctrl
  else if(key ==51 && e.ctrlKey){
	  var band = 13
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 0 with 0
  else if (key == 48 && e.altKey) {
	var band = 0
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  } 
  //set band to 1 with 1 
  else if(key ==49 && e.altKey){
	  var band = 1
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  } 
  //set band to 2 with 2
  else if(key ==50 && e.altKey){
	  var band = 2
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  } 
  //set  band to 3 with 3
  else if(key ==51 && e.altKey){
	  var band = 3
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 4 with 4
  else if(key ==52 && e.altKey){
	  var band = 4
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 5 with 5
  else if(key ==53 && e.altKey){
	  var band = 5
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 6 with 6
  else if(key ==54 && e.altKey){
	  var band = 6
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 7 with 7
  else if(key ==55 && e.altKey){
	  var band = 7
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //ste band to 8 with 8
  else if(key ==56 && e.altKey){
	  var band = 8
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  //set band to 9 with 9
  else if(key ==57 && e.altKey){
	  var band = 9
	  var redirect = base_url.concat(slash,number,slash,band);
	  window.location.href = redirect;
  }
  
  //go to next image with shift + n
  else if(key==78){
	var command = 'next';
	var labels = document.getElementsByName('label');
	var label = "None";
	for( i= 0; i < labels.length; i++) {
		if(labels[i].checked)
			label = labels[i].value;
	}
	var redirect = base_url.concat(slash,command,slash,number,slash,label);
	window.location.href = redirect;
  }
  //go to prev with p
    else if(key==80){
		
		var command = 'prev';
		var labels = document.getElementsByName('label');
		var label = "None";
		for( i= 0; i < labels.length; i++) {
			if(labels[i].checked)
				label = labels[i].value;
		}
		var redirect = base_url.concat(slash,command,slash,number,slash,label);
		window.location.href = redirect;
  }
  //checked "clouds" with  a
  else if(key== 67){
	document.getElementById("clouds").checked = true;
	document.getElementById("semi-clouds").checked = false;
	document.getElementById("no-clouds").checked = false;
  }
  //checked "semi-clouds" with  s
  else if(key== 83){
	document.getElementById("clouds").checked = false;
	document.getElementById("semi-clouds").checked = true;
	document.getElementById("no-clouds").checked = false;
  }
  //checked "no clouds" with d
  else if(key== 79){
	document.getElementById("clouds").checked = false;
	document.getElementById("semi-clouds").checked = false;
	document.getElementById("no-clouds").checked = true;
  }
  //checked rgb box with r
  else if(key==82){
	document.getElementById("rgb").checked=true;
  }
  
}

function labels(){
	var label = document.getElementById("currentlabel").innerHTML;
	
	var clouds = "clouds";
	var semi = "semi-clouds";
	var no = "no-clouds"
	if (label == clouds){
		document.getElementById("clouds").checked = true;
		document.getElementById("semi-clouds").checked = false;
		document.getElementById("no-clouds").checked = false;
	}
	else if(label == semi){
		document.getElementById("clouds").checked = false;
		document.getElementById("semi-clouds").checked = true;
		document.getElementById("no-clouds").checked = false;
	}
	else if(label == no ){
		document.getElementById("clouds").checked = false;
		document.getElementById("semi-clouds").checked = false;
		document.getElementById("no-clouds").checked = true;
	}
}


