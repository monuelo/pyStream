const fileReader = new FileReader()

function fetchImage() {
  new Promise((res, rej) => {
    const url = "/screen.png?random=" + new Date().getTime()
    axios.get(url, { responseType: 'blob' })
      .then(function (response) {
        document.images["screen"].src = URL.createObjectURL(response.data)
        res(fetchImage())
      })
      .catch(function (error) { console.log(error) })
  })
}

document.addEventListener("DOMContentLoaded", fetchImage)

function toggleFullScreen() {
  if ((document.fullScreenElement && document.fullScreenElement !== null) ||    
   (!document.mozFullScreen && !document.webkitIsFullScreen)) {
    if (document.documentElement.requestFullScreen) {  
      document.documentElement.requestFullScreen();  
    } else if (document.documentElement.mozRequestFullScreen) {  
      document.documentElement.mozRequestFullScreen();  
    } else if (document.documentElement.webkitRequestFullScreen) {  
      document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);  
    }  
  } else {  
    if (document.cancelFullScreen) {  
      document.cancelFullScreen();  
    } else if (document.mozCancelFullScreen) {  
      document.mozCancelFullScreen();  
    } else if (document.webkitCancelFullScreen) {  
      document.webkitCancelFullScreen();  
    }  
  }

}