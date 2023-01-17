from flask import Flask, redirect, url_for, render_template, request
from FINALCODERECIPE import recommend, match_name

app = Flask(__name__, template_folder = "templates")

@app.route("/")
def home():
	return render_template("Home.html")

@app.route("/grocery")
def grocery():
	return render_template("grocery.html")

@app.route("/Search")
def Search():
	return render_template("Search.html")

def final_out(ingredient):
	name_str = []
	ing_str = []
	rec_str = []
	link_str = []
	ingre_id = match_name(ingredient)
	name_list, ing_list, rec_list, link_list = recommend(ingre_id, 5)

	name0 = name_list[0]
	name1 = name_list[1]
	name2 = name_list[2]
	name3 = name_list[3]
	name4 = name_list[4]

	ing0 = ing_list[0]
	ing1 = ing_list[1]
	ing2 = ing_list[2]
	ing3 = ing_list[3]
	ing4 = ing_list[4]

	rec0 = rec_list[0]
	rec1 = rec_list[1]
	rec2 = rec_list[2]
	rec3 = rec_list[3]
	rec4 = rec_list[4]

	link0 = link_list[0]
	link1 = link_list[1]
	link2 = link_list[2]
	link3 = link_list[3]
	link4 = link_list[4]

	return name0, name1, name2, name3, name4, ing0, ing1, ing2, ing3, ing4, rec0, rec1, rec2, rec3, rec4, link0, link1, link2, link3, link4

@app.route("/K",methods=['GET'])
def K():
	result = []
	ingredient = request.args.get('name')
	name0, name1, name2, name3, name4, ing0, ing1, ing2, ing3, ing4, rec0, rec1, rec2, rec3, rec4, link0, link1, link2, link3, link4 = final_out(ingredient)
	return render_template("displayrec.html",dname0=name0, dname1=name1, dname2=name2, dname3=name3, dname4=name4, ding0=ing0, ding1=ing1, ding2=ing2, ding3=ing3, ding4=ing4, drec0=rec0, drec1=rec1, drec2=rec2, drec3=rec3, drec4=rec4, dlink0=link0, dlink1=link1, dlink2=link2, dlink3=link3, dlink4=link4)

if __name__=="__main__":
	app.run(debug=True)

