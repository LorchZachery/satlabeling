

var canvas, ctx, flag = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false,
		colorLayerData,
		canvasWidth,
		canvasHeight;


    var x = "opaque",
        y = 5;

var colorMask = {
	r: 255,
	g: 255,
	b: 255,
	a: .5
}
var startX = -1;
var startY = -1;
function getCursorPosition(event) {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
	startX = x;
	startY = y;
}

    function init() {
        canvas = document.getElementById('can');
        ctx = canvas.getContext("2d");
        
        
        //loads image to make canvas same size as image to be marked
        imageObj = new Image();
        imageObj.src= "/static/image.jpeg";
        canvas.width = imageObj.width;
        canvas.height = imageObj.height;
		canvasWidth = canvas.width;
		canvasHeight = canvas.height;
        colorLayerData = ctx.getImageData(0, 0, canvasWidth, canvasHeight);
		
		
        //tracks mouse movement
        canvas.addEventListener("mousemove", function (e) {
            findxy('move', e)
        }, false);
        canvas.addEventListener("mousedown", function (e) {
            findxy('down', e);
			
			
			
        }, false);
        canvas.addEventListener("mouseup", function (e) {
            findxy('up', e)
        }, false);
        canvas.addEventListener("mouseout", function (e) {
            findxy('out', e)
        }, false);
    }
      

   
    //draws on canvas
    function draw() {
        ctx.strokeStyle = 'rgba(255, 255, 255, .5)';
        ctx.lineWidth = 5;
        
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.stroke();
        ctx.closePath();
        
    }
    
    function erase() {
        var m = confirm("Want to clear");
        if (m) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
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
        
    }

    function erasePen() {
        alert("time to erase");
        ctx.lineWidth = 50;
        ctx.globalCompositeOperation = "destination-out";
        ctx.strokeStyle = "rgba(0, 0, 0, 1.0)";
    }
    
    function pen() {
        alert("back to pen");
        
        ctx.lineWidth = 5;
        ctx.globalCompositeOperation = "source-over";
        ctx.strokeStyle = 'rgba(255, 255, 255, .5)';
    }

    function mask(){
        alert("mask being made");
           var dataURL = canvas.toDataURL( "image/png" );
        //alert(dataURL);
      $.post( "/get_post_json", {
        canvas_data: dataURL
      }, function(err, reg, resp) {
          
      });
        
    }

function startFlood(){
	window.addEventListener('click', function(e){
	getCursorPosition(e);
	floodfill();
});
}
function floodfill() {
alert(startX);
if (startX  > 0){	
			var newPos,
				x,
				y,
				pixelPos,
				reachLeft,
				reachRight,
				drawingBoundLeft = 0, 
				drawingBoundTop = canvas.height,
				drawingBoundRight = canvas.width,
				drawingBoundBottom = 0,
				startR = 0,
				startG = 0,
				startB = 0,
				startA = 0,
				pixelStack = [[startX, startY]];	
	
pixelStack = [[startX, startY]];

while(pixelStack.length)
{
  
  var newPos, x, y, pixelPos, reachLeft, reachRight;
  newPos = pixelStack.pop();
  x = newPos[0];
  y = newPos[1];
 
  pixelPos = Math.floor((y*canvasWidth + x) * 4);
  
  while(y-- >= drawingBoundTop && matchStartColor(pixelPos))
  {
	
    pixelPos -= canvasWidth * 4;
  }
  pixelPos += canvasWidth * 4;
  ++y;
  reachLeft = false;
  reachRight = false;
  while(y++ < canvasHeight-1 && matchStartColor(pixelPos))
  {
	
    colorPixel(pixelPos);

    if(x > 0)
    {
      if(matchStartColor(pixelPos - 4))
      {
        if(!reachLeft){
          pixelStack.push([x - 1, y]);
          reachLeft = true;
        }
      }
      else if(reachLeft)
      {
        reachLeft = false;
      }
    }
	
    if(x < canvasWidth-1)
    {
      if(matchStartColor(pixelPos + 4))
      {
        if(!reachRight)
        {
          pixelStack.push([x + 1, y]);
          reachRight = true;
        }
      }
      else if(reachRight)
      {
        reachRight = false;
      }
    }
			
    pixelPos += canvasWidth * 4;
  }
  
}

ctx.putImageData(colorLayerData, 0, 0);
}
window.removeEventListener('click',floodfill);
function matchStartColor(pixelPos)
{
  
  var r = colorLayerData.data[pixelPos];	
  var g = colorLayerData.data[pixelPos+1];	
  var b = colorLayerData.data[pixelPos+2];
  var a = colorLayerData.data[pixelPos+3];
  
  return (r == startR && g == startG && b == startB && startA == a);
}

function colorPixel(pixelPos)
{
  colorLayerData.data[pixelPos] = 255;//colorMask.r;
  colorLayerData.data[pixelPos+1] = 255;//colorMask.g;
  colorLayerData.data[pixelPos+2] = .5;//colorMask.b;
  colorLayerData.data[pixelPos+3] = colorMask.a;
}
}