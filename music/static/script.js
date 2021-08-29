// JS function to play the audio file
var audio = {    
    init: function() {        
    var $that = this;        
        $(function() {            
            $that.components.media();        
        });    
    },
    components: {        
        media: function(target) {            
            var media = $('audio.fc-media', (target !== undefined) ? target : 'body');            
            if (media.length) {                
                media.mediaelementplayer({                    
                    audioHeight: 400,
                    features : ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks'],
                    alwaysShowControls      : true,
                    timeAndDurationSeparator: '',
                    //iPadUseNativeControls: true,
                    //iPhoneUseNativeControls: true,
                    //AndroidUseNativeControls: true                
                });            
            }            
        },
            
    },
};
audio.init();

// JS function to create the visualisations
window.onload = function() {
    // varibles which is thakeing the aoudi input
    // and maping it with the bitrate  
    var audio = document.getElementById("audio_html5")
    
    var context = new AudioContext()
    var src = context.createMediaElementSource(audio)
    var analyser = context.createAnalyser()

    var canvas = document.getElementById("canvas")
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
    var ctx = canvas.getContext("2d")

    src.connect(analyser)
    analyser.connect(context.destination)

    analyser.fftSize = 256

    var bufferLength = analyser.frequencyBinCount
    console.log(bufferLength)

    var dataArray = new Uint8Array(bufferLength)

    var WIDTH = canvas.width;
    var HEIGHT = canvas.height;

    var barWidth = (WIDTH / bufferLength) * 1.3;
    var barHeight;
    var x = 0;

    // function for creating canvas bars 
    function renderFrame() {
        requestAnimationFrame(renderFrame);
  
        x = 0;
  
        analyser.getByteFrequencyData(dataArray);
  
        ctx.fillStyle = "#000";
        ctx.fillRect(0, 0, WIDTH, HEIGHT);
  
        for (var i = 0; i < bufferLength; i++) {
          barHeight = dataArray[i];
          
          var r = barHeight + (25 * (i/bufferLength));
          var g = 250 * (i/bufferLength);
          var b = 50;
  
          ctx.fillStyle = "rgb(" + r + "," + g + "," + b + ")";
          // displays the top canvas bars
          ctx.fillRect(x, 0, barWidth, barHeight);
          // displais bottom canvas bars
          ctx.fillRect(x, HEIGHT - barHeight, barWidth, barHeight)
            
          x += barWidth + 1;
        }
      }
      renderFrame()   

}