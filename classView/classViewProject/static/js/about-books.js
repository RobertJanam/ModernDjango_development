function myfunction(id){
    var x = document.getElementById('content-'+id); // targets the list container using the passed ID var

    var currentDisplay = window.getComputedStyle(x).display; // reads the style even if it was placed in an external css

    if (x.style.display === "none"){
        x.style.display = "block";
    }
    else{
        x.style.display = "none";
    }
}