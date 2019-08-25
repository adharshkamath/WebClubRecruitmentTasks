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
    selectedOption = (e.target.id); 
    responseData[question]["Choice"] = selectedOption;  
    console.log(responseData); 
});

$('a[data-toggle="tab"').on('click', function(e){
    question = (e.target.id);    
});

$('#form').submit(function(){ 
    $.each(responseData, function(i,responseData){
        var QuestionID = i +'q';
        $('<input />').attr('Question_ID', QuestionID)
            .attr('Choice', responseData[i]["Choice"])
            .appendTo(this);
    });
    return true;
}); 