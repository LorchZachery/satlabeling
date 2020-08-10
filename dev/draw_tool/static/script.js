

var canvas, ctx, flag = false,
        prevX = 0,
        currX = 0,
        prevY = 0,
        currY = 0,
        dot_flag = false;

    var x = "opaque",
        y = 5;

    function init() {
        canvas = document.getElementById('can');
        ctx = canvas.getContext("2d");
        
        
        //loads image to make canvas same size as image to be marked
        imageObj = new Image();
        imageObj.src= "/static/image.jpeg";
        canvas.width = imageObj.width;
        canvas.height = imageObj.height;
        
    
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
    
    function clear() {
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
    
    
    
