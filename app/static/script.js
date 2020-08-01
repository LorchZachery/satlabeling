
//hot keys
document.onkeyup = function(e) {
  var key = e.which || e.keyCode;
  //set band to 10 with 0 and ctrl
  if( e.ctrlKey && key ==48){
	  document.getElementById('band_num').value=10;
  }
  //set band to 11 with 1 and ctrl
  else if(key ==49 && e.ctrlKey){
	  document.getElementById('band_num').value=11;
  }
  //set band to 12 with 2 and ctrl
  else if(key ==50 && e.ctrlKey){
	  document.getElementById('band_num').value=12;
  }
  //set band to 13 with 3 and ctrl
  else if(key ==51 && e.ctrlKey){
	  document.getElementById('band_num').value=13;
  }
  //set band to 0 with 0
  else if (key == 48) {
	document.getElementById('band_num').value=0;
  } 
  //set band to 1 with 1 
  else if(key ==49){
	  document.getElementById('band_num').value=1;
  } 
  //set band to 2 with 2
  else if(key ==50){
	  document.getElementById('band_num').value=2;
  } 
  //set  band to 3 with 3
  else if(key ==51){
	  document.getElementById('band_num').value=3;
  }
  //set band to 4 with 4
  else if(key ==52){
	  document.getElementById('band_num').value=4;
  }
  //set band to 5 with 5
  else if(key ==53){
	  document.getElementById('band_num').value=5;
  }
  //set band to 6 with 6
  else if(key ==54){
	  document.getElementById('band_num').value=6;
  }
  //set band to 7 with 7
  else if(key ==55){
	  document.getElementById('band_num').value=7;
  }
  //ste band to 8 with 8
  else if(key ==56){
	  document.getElementById('band_num').value=8;
  }
  //set band to 9 with 9
  else if(key ==57){
	  document.getElementById('band_num').value=9;
  }
  
  //go to next image with shift + n
  else if(key==78){
	var base_url = window.location.origin;
	var host = window.location.host;
	var url = window.location.href;
	var slash = "/";
	var list = url.split("/");
	var x = list.length;
	var number = list[x -2];
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
  //go to prev with shift + p
    else if(key==80){
		var base_url = window.location.origin;
		var host = window.location.host;
		var url = window.location.href;
		var slash = "/";
		var list = url.split("/");
		var x = list.length;
		var number = list[x -2];
		var command = 'prev';
		//var labels = document.getElementsByName('label');
		var label = "None";
		//for( i= 0; i < labels.length; i++) {
		//	if(labels[i].checked)
		//		label = labels[i].value;
		//}
		var redirect = base_url.concat(slash,command,slash,number,slash,label);
		window.location.href = redirect;
  }
  //checked "clouds" with shift + a
  else if(key== 65){
	document.getElementById("clouds").checked = true;
	document.getElementById("semi-clouds").checked = false;
	document.getElementById("no-clouds").checked = false;
  }
  //checked "semi-clouds" with shift + s
  else if(key== 83){
	document.getElementById("clouds").checked = false;
	document.getElementById("semi-clouds").checked = true;
	document.getElementById("no-clouds").checked = false;
  }
  //checked "no clouds" with shift + d
  else if(key== 68){
	document.getElementById("clouds").checked = false;
	document.getElementById("semi-clouds").checked = false;
	document.getElementById("no-clouds").checked = true;
  }
  //checked rgb box with shift +r
  else if(key==82){
	document.getElementById("rgb").checked=true;
  }
  //change band with b FIXME
  else if(key==66){
	document.getElementById("bandForm").submit()
  }
};