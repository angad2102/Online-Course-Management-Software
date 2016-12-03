function addcomponent(){
	$("#saveM").css("visibility","hidden");
	var string = "<h4>Add New Component</h4>\
	<br/>\
	<div class='row'>\
		<div class='col-lg-6 col-xs-12'>\
			<input class='form-control' id='n-name' type='text' placeholder='Component Name'>\
			<br/>\
			<select class='form-control' id='type'>\
			<option value='0'>\
			Select Type\
			</option>\
				<option value='TX'>\
					Text\
				</option>\
				<option value='IM'>\
					Image\
				</option>\
				<option value='VD'>\
					Video\
				</option>\
				<option value='FL'>\
					File\
				</option>\
			</select>\
			<br/>\
			<textarea placeholder='Content/link' rows=5 id='content' class='form-control'></textarea> \
				Sequence : \
				<br/>\
			</div>\
			<br>\
		</div>\
	</div>";

	string += "<div class='row'>\
		<div class='col-lg-6 col-xs-12'>\
		<br/>\
		<button class='btn btn-primary'>\
		Save Component\
		</button>\
		<button onclick='backtoModule()' class='btn btn-danger pull-right'>\
		Cancel\
		</button>\
		<div>\
		</div>\
	"
	$("#newComp").html(string);
    
}

function backtoModule(){
	$("#newComp").html("");
	$("#saveM").css("visibility","visible");
}

function newmodule() {
	$("#modules").css("display","none");
	string = '<div class="row">\
                    <div class="col-lg-6 col-xs-12">\
                        <h1 class="page-header"><input type="text" placeholder="New Module Name" id="new-name" class="form-control"></h1>\
                    </div>\
                </div>\
                <div class="panel-body">';

    string += "Sequence: <br><div class='row'><div class='col-lg-6 col-xs-12'><button class='btn btn-primary'>Save New Module</button><button class='btn btn-danger pull-right' onclick='cancelnewmodule()'>Cancel</button></div></div>"
    string += "</div>";
	$("#newmodule").html(string);
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
}

function saveCname(courseID){
	$("#CName").css("display","block");
	$("#EditCName").css("display","none");
}

function saveCDesc(courseID){
	$("#CDesc").css("display","block");
	$("#EditCDesc").css("display","none");
}