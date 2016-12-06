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
	if($("#editModuleName").val()==""||$("#editModuleName").val()==null){
		alert("Please enter the module name");
		return;
	}
	$("#head").css("display","block");
	$("#edit-head").css("display","none");
	$("form#editmodulename").submit();
}
function editcomp(ComponentID){
	$("#"+ComponentID).css("display","none");
	$("#edit_"+ComponentID).css("display","block");
}



function updatecomponent(ComponentID){
	if($("#edit_"+ComponentID+"_name").val()==""||$("#edit_"+ComponentID+"_name").val()==null){
		alert("Please enter the component name");
		return;
	}
	if($("#edit_"+ComponentID+"_content").val()==""||$("#edit_"+ComponentID+"_content").val()==null){
		alert("Please enter the component content");
		return;
	}
	$("#"+ComponentID).css("display","block");
	$("#edit_"+ComponentID).css("display","none");
	$("form#editcomponent_"+ComponentID).submit();
}
function saveCname(courseID){
	if($("#newCourseName").val()==""||$("#newCourseName").val()==null){
		alert("Please enter the course name");
		return;
	}else {
		$("#CName").css("display","block");
		$("#EditCName").css("display","none");

		$("form#editcname").submit();
	}
	
}

function saveCDesc(courseID){
	if($("#newCourseDesc").val()==""||$("#newCourseDesc").val()==null){
		alert("Please enter the course description");
		return;
	}
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

function createnewcourse(){
	if($("#course-name").val()==""||$("#course-name").val()==null){
		alert("Please enter the course name");
		return;
	}
	if($("textarea#c-desc").val()==""||$("textarea#c-desc").val()==null){
		alert("Please enter the course description");
		return;
	}
	if($("#cat").val()==""||$("#cat").val()==null){
		alert("Please choosa a category");
		return;
	}
	if($("#module-name").val()==""||$("#module-name").val()==null){
		alert("Please enter the name of the first module");
		return;
	}

	$("form#new-course-ass").submit();
}

function addnewComponent(){
	if($("#n-name").val()==""||$("#n-name").val()==null){
		alert("Please enter the component name");
		return;
	}
	if($("#type").val()==""||$("#type").val()==null){
		alert("Please choose component type");
		return;
	}
	if($("#content").val()==""||$("#content").val()==null){
		alert("Please Enter component content");
		return;
	}

	$("form#new-comp").submit();
}
