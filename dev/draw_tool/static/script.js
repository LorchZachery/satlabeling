
var canvas, ctx, flag = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;

var x = "opaque",
       y = 5;
var fill_value = true;
   
       
   
function init() {
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    
    
    //loads image to make canvas same size as image to be marked
    imageObj = new Image();
    imageObj.src= "/static/image.jpeg";
    canvas.width =imageObj.width;
    canvas.height =imageObj.height;
    

    //tracks mouse movement
    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
};


/*
 //used to make white eraser ... need to change erase function
 function color(obj) {
    switch (obj.id) {
        case "green":
            x = "green";
            break;
        case "blue":
            x = "blue";
            break;
        case "red":
            x = "red";
            break;
        case "yellow":
            x = "yellow";
            break;
        case "orange":
            x = "orange";
            break;
        case "black":
            x = "black";
            break;
        case "white":
            x = "white";
            break;
    }
    if (x == "white") y = 14;
    else y = 30;
}
*/

function fill(){
  fill_value = true;
  
};

function color(color_value){
  ctx.strokeStyle = color_value;
  ctx.fillStyle = color_value;
};

//draws on canvas
function draw() {
    ctx.strokeStyle = 'rgba(255, 255, 255, .3)';
    ctx.lineWidth = 5;
    
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.stroke();
    if(fill_value){
        ctx.fill();
        fill_value = false;
    }
    
    
    //ctx.closePath();
};

function erase() {
    var m = confirm("Want to clear");
    if (m) {
        ctx.clearRect(0, 0, imageObj.width, imageObj.height);
    }
}

function findxy(res, e) {
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 2, 2);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw();
        }
    }
    
};

function mask() {
    
    var img = canvas.toDataURL();
    
    alert(img);
    
    var base_url = window.location.origin;
    alert(base_url);
    var slash = "/";
    var redirect = base_url.concat(slash,img);
    window.location.href = redirect;
    
    document.getElementById('can').src = img;
    alert("time to figure out how to make a mask");
    
    
    //how to make mask in python opencv
    //Wmask =(img[:, :, 0:3] == [255, 255, 255]).all(2);
    //cv.imwrite('result.png', (Wmask*255).astype(np.uint8));
    

}

function mask(){
	var dataURL = canvas.toDataURL( "image/png" );
	alert(dataURL);
    $.post( "/get_post_json", {
       canvas_data: dataURL
	}, function(err, reg, resp) {
	  
	});
	
}
	
	
	
	
	
	
	
	
	