var responseData = {};
var noOfQuestions = $("li").length;
//console.log(noOfQuestions);
for (let index = 1; index <= noOfQuestions; index++) {
    responseData[index]={};
    responseData[index]["Choice"] = 0;
    //console.log(responseData);   
    //console.log($("form"));
  
}
var selectedOption = 1;
var question = 1;

$('button').on('click', function(e){
    var selString = 'button#'+selectedOption+".list-group-item.list-group-item-action";
    $(selString).css({"background-color":"#6930f6", "color":"#fff"});
    selectedOption = (e.target.id); 
    responseData[question]["Choice"] = selectedOption;  
    var selString1 = 'button#'+selectedOption+".list-group-item.list-group-item-action";
    $(selString1).css({"background-color":"#fff", "color":"#6930f6", "border":"2px solid #6930f6"});
    console.log(responseData); 
});

$('a[data-toggle="tab"').on('click', function(e){
    question = (e.target.id);
    var selString = 'button#'+selectedOption+".list-group-item.list-group-item-action";
    $(selString).css({"background-color":"#6930f6", "color":"#fff"});
    selectedOption = responseData[question]["Choice"];  
    var selString1 = 'button#'+selectedOption+".list-group-item.list-group-item-action";
    $(selString1).css({"background-color":"#fff", "color":"#6930f6", "border":"2px solid #6930f6"});
    console.log(responseData);     
    
});

/*
function addData(responseData, theForm) {

    for (let index = 0; index < responseData.length; index++) {
        var input = document.createElement('input');
        input.type = 'hidden';
        input.name = index;
        input.value = responseData[index]["Choice"];
        theForm.appendChild(input);    
    }

}


$('#form').submit(function(){ 
    addData(responseData, document.getElementById("form"));
    return true;
}); */