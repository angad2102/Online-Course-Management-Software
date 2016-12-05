function addcomponent(){
	$("#saveM").css("display","none");
	$("#newComp").css("display","block");
    
}

function backtoModule(){
	$("#newComp").css("display","none");
	$("#saveM").css("display","block");
}

function newmodule() {
	$("#modules").css("display","none");

	$("#newmodule").css("display","block");
}

function cancelnewmodule() {
	$("#modules").css("display","block");
	$("#newmodule").html("");
}

function editCourseName(courseID) {
	$("#CName").css("display","none");
	$("#EditCName").css("display","block");
}

function closeeditname(){
	$("#CName").css("display","block");
	$("#EditCName").css("display","none");
}

function editCourseDetails(courseID) {
	$("#CDesc").css("display","none");
	$("#EditCDesc").css("display","block");
}

function editModuleName(moduleID){
	$("#head").css("display","none");
	$("#edit-head").css("display","block");
}

function saveModuleName(moduleID){
	$("#head").css("display","block");
	$("#edit-head").css("display","none");
	$("form#editmodulename").submit();
}
function editcomp(ComponentID){
	$("#"+ComponentID).css("display","none");
	$("#edit_"+ComponentID).css("display","block");
}



function updatecomponent(ComponentID){
	$("#"+ComponentID).css("display","block");
	$("#edit_"+ComponentID).css("display","none");
	$("form#editcomponent_"+ComponentID).submit();
}
function saveCname(courseID){
	$("#CName").css("display","block");
	$("#EditCName").css("display","none");

	$("form#editcname").submit();
}

function saveCDesc(courseID){
	$("#CDesc").css("display","block");
	$("#EditCDesc").css("display","none");

	$("form#editcdesc").submit();

}

function editCourseCategory(courseID){
	$("#CCat").css("display","none");
	$("#editCCat").css("display","block");
	
}

function saveCCat(courseID){
	$("#CCat").css("display","block");
	$("#editCCat").css("display","none");
	$("form#editcat").submit();

}
