
function breakchain(){
        let chain = document.getElementById('tach')
        chain.innerHTML = "&#xf62d";
    
        setTimeout(function(){
            chain.innerHTML = "&#xf62c"
        }, 1000)
        setTimeout(function(){
            chain.innerHTML = "&#xf629"
        }, 2000)
        setTimeout(function(){
            chain.innerHTML = "&#xf62a"
        }, 3000)
        setTimeout(function(){
            chain.innerHTML = "&#xf62b"
        }, 4000)

        breakchain();
        setInterval(breakchain , 5000);
        
    }
    
    



