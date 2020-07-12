from flask import Flask,request
import random
Dinners = []
Lunches = []
with open("/home/DarkShadow578/Menu/Dinners.txt", "r") as f:
    for item in f:
        h=item.replace("\n","")
        Dinners.append(h)
with open("/home/DarkShadow578/Menu/Lunches.txt", "r") as g:
    for item in g:
        j=item.replace("\n","")
        Lunches.append(j)

app = Flask(__name__)

@app.route('/')
def Main_Menu():
    return """<input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="Dinner" onclick="window.location.href='/Dinner_Menu'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="Lunch" onclick="window.location.href='/Lunch_Menu'"
                    />"""

@app.route('/Dinner_Menu')
def Dinner_Menu():
    return """<input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="One" onclick="window.location.href='/Dinner/One'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="A Week" onclick="window.location.href='/Dinner/Week'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="A Month" onclick="window.location.href='/Dinner/Month'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="Add New Dinner" onclick="window.location.href='/Dinner/New'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="View all Dinners" onclick="window.location.href='/Dinners.txt'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="View all Dinner Recipes" onclick="window.location.href='/Dinner/Recipe'"
                    />"""


@app.route('/Lunch_Menu')
def Lunch_Menu():
    return """<input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="One" onclick="window.location.href='/Lunch/One'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="A Week" onclick="window.location.href='/Lunch/Week'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="A Month" onclick="window.location.href='/Lunch/Month'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="Add New Lunch" onclick="window.location.href='/Lunch/New'"
                    /><input
                        style="width: 300px;
                        padding: 20px;
                        cursor: pointer;
                        box-shadow: 6px 6px 5px;
                        #999;
                        -webkit-box-shadow: 6px 6px 5px #999;
                        -moz-box-shadow: 6px 6px 5px #999;
                        font-weight: bold;
                        background: #fa0000;
                        color: #000;
                        border-radius: 10px;
                        border: 1px solid #999;
                        font-size: 150%;
                        " type="button" value="View all Lunches" onclick="window.location.href='/Lunches.txt'"
                    />"""


@app.route('/Dinner/One', methods=["GET", "POST"])
def Dinner_One():
    d = random.randint(0,len(Dinners)-1)
    result =(Dinners[d].replace("_"," "))
    return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(result=result)

@app.route('/Lunch/One', methods=["GET", "POST"])
def Lunch_One():
    d = random.randint(0,len(Lunches)-1)
    result =(Lunches[d].replace("_"," "))
    return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(result=result)



@app.route('/Dinner/Week', methods=["GET", "POST"])
def Dinner_Week():
    week=["","","","","","","",""]
    for x in range(7):
        d = random.randint(0,len(Dinners)-1)
        week[x]=Dinners[d]
    monday=(week[0])
    tuesday=(week[1])
    wednesday=(week[2])
    thursday=(week[3])
    friday=(week[4])
    saturday=(week[5])
    sunday=(week[6])
    return '''<html>
                    <body>
                        <p>{monday}</p>
                        <p>{tuesday}</p>
                        <p>{wednesday}</p>
                        <p>{thursday}</p>
                        <p>{friday}</p>
                        <p>{saturday}</p>
                        <p>{sunday}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,friday=friday,saturday=saturday,sunday=sunday)

@app.route('/Lunch/Week', methods=["GET", "POST"])
def Lunches_Week():
    week=["","","","","","","",""]
    for x in range(7):
        d = random.randint(0,len(Lunches)-1)
        week[x]=Lunches[d]
    monday=(week[0])
    tuesday=(week[1])
    wednesday=(week[2])
    thursday=(week[3])
    friday=(week[4])
    saturday=(week[5])
    sunday=(week[6])
    return '''<html>
                    <body>
                        <p>{monday}</p>
                        <p>{tuesday}</p>
                        <p>{wednesday}</p>
                        <p>{thursday}</p>
                        <p>{friday}</p>
                        <p>{saturday}</p>
                        <p>{sunday}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,friday=friday,saturday=saturday,sunday=sunday)

@app.route('/Dinner/Month', methods=["GET", "POST"])
def Dinner_Month():
    month=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    for x in range(32):
        d = random.randint(0,len(Dinners)-1)
        month[x]=Dinners[d]
    one=month[0]
    two=month[1]
    three=month[2]
    four=month[3]
    five=month[4]
    six=month[5]
    seven=month[6]
    eight=month[7]
    nine=month[8]
    ten=month[9]
    eleven=month[10]
    twelve=month[11]
    therteen=month[12]
    fourteen=month[13]
    fifteen=month[14]
    sixteen=month[15]
    seventeen=month[16]
    eighteen=month[17]
    nighteen=month[18]
    twenty=month[19]
    twentyone=month[20]
    twentytwo=month[21]
    twentythree=month[22]
    twentyfour=month[23]
    twentyfive=month[24]
    twentysix=month[25]
    twentyseven=month[26]
    twentyeight=month[27]
    twentynine=month[28]
    thirty=month[29]
    thirtyone=month[30]
    thirtytwo=month[31]

    return '''<html>
                    <body>
                        <p>{one}</p>
                        <p>{two}</p>
                        <p>{three}</p>
                        <p>{four}</p>
                        <p>{five}</p>
                        <p>{six}</p>
                        <p>{seven}</p>
                        <p>{eight}</p>
                        <p>{nine}</p>
                        <p>{ten}</p>
                        <p>{eleven}</p>
                        <p>{twelve}</p>
                        <p>{therteen}</p>
                        <p>{fourteen}</p>
                        <p>{fifteen}</p>
                        <p>{sixteen}</p>
                        <p>{seventeen}</p>
                        <p>{eighteen}</p>
                        <p>{nighteen}</p>
                        <p>{twenty}</p>
                        <p>{twentyone}</p>
                        <p>{twentytwo}</p>
                        <p>{twentythree}</p>
                        <p>{twentyfour}</p>
                        <p>{twentyfive}</p>
                        <p>{twentysix}</p>
                        <p>{twentyseven}</p>
                        <p>{twentyeight}</p>
                        <p>{twentynine}</p>
                        <p>{thirty}</p>
                        <p>{thirtyone}</p>
                        <p>{thirtytwo}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(one = one,two = two,three = three,four = four,five = five,six = six,seven = seven,eight = eight,nine = nine,ten = ten,eleven = eleven,twelve = twelve,therteen = therteen,fourteen = fourteen,fifteen = fifteen,sixteen = sixteen,seventeen = seventeen,eighteen = eighteen,nighteen = nighteen,twenty = twenty,twentyone = twentyone,twentytwo = twentytwo,twentythree = twentythree,twentyfour = twentyfour,twentyfive = twentyfive,twentysix = twentysix,twentyseven = twentyseven,twentyeight = twentyeight,twentynine = twentynine,thirty = thirty,thirtyone = thirtyone,thirtytwo = thirtytwo)

@app.route('/Lunch/Month', methods=["GET", "POST"])
def Lunch_Month():
    month=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    for x in range(32):
        d = random.randint(0,len(Lunches)-1)
        month[x]=Lunches[d]
    one=month[0]
    two=month[1]
    three=month[2]
    four=month[3]
    five=month[4]
    six=month[5]
    seven=month[6]
    eight=month[7]
    nine=month[8]
    ten=month[9]
    eleven=month[10]
    twelve=month[11]
    therteen=month[12]
    fourteen=month[13]
    fifteen=month[14]
    sixteen=month[15]
    seventeen=month[16]
    eighteen=month[17]
    nighteen=month[18]
    twenty=month[19]
    twentyone=month[20]
    twentytwo=month[21]
    twentythree=month[22]
    twentyfour=month[23]
    twentyfive=month[24]
    twentysix=month[25]
    twentyseven=month[26]
    twentyeight=month[27]
    twentynine=month[28]
    thirty=month[29]
    thirtyone=month[30]
    thirtytwo=month[31]

    return '''<html>
                    <body>
                        <p>{one}</p>
                        <p>{two}</p>
                        <p>{three}</p>
                        <p>{four}</p>
                        <p>{five}</p>
                        <p>{six}</p>
                        <p>{seven}</p>
                        <p>{eight}</p>
                        <p>{nine}</p>
                        <p>{ten}</p>
                        <p>{eleven}</p>
                        <p>{twelve}</p>
                        <p>{therteen}</p>
                        <p>{fourteen}</p>
                        <p>{fifteen}</p>
                        <p>{sixteen}</p>
                        <p>{seventeen}</p>
                        <p>{eighteen}</p>
                        <p>{nighteen}</p>
                        <p>{twenty}</p>
                        <p>{twentyone}</p>
                        <p>{twentytwo}</p>
                        <p>{twentythree}</p>
                        <p>{twentyfour}</p>
                        <p>{twentyfive}</p>
                        <p>{twentysix}</p>
                        <p>{twentyseven}</p>
                        <p>{twentyeight}</p>
                        <p>{twentynine}</p>
                        <p>{thirty}</p>
                        <p>{thirtyone}</p>
                        <p>{thirtytwo}</p>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>
            '''.format(one = one,two = two,three = three,four = four,five = five,six = six,seven = seven,eight = eight,nine = nine,ten = ten,eleven = eleven,twelve = twelve,therteen = therteen,fourteen = fourteen,fifteen = fifteen,sixteen = sixteen,seventeen = seventeen,eighteen = eighteen,nighteen = nighteen,twenty = twenty,twentyone = twentyone,twentytwo = twentytwo,twentythree = twentythree,twentyfour = twentyfour,twentyfive = twentyfive,twentysix = twentysix,twentyseven = twentyseven,twentyeight = twentyeight,twentynine = twentynine,thirty = thirty,thirtyone = thirtyone,thirtytwo = thirtytwo)


@app.route('/Dinner/New', methods=["GET", "POST"])
def Add_Dinner():
    if request.method == "POST":
        New_D = request.form["Dinner"]
        New_D = New_D.replace(" ","_")
        with open("/home/DarkShadow578/Menu/Dinners.txt", "a") as u:
            u.write("\n"+New_D)
        return '''<html>
                    <body>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>'''
    return '''
        <html>
            <body>
                <p>Enter New Dinner:</p>
                <form method="post" action="/Dinner/New">
                    <p><input name="Dinner" /></p>
                    <p><input type="submit" value="Add Dinner" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/Lunch/New', methods=["GET", "POST"])
def Add_Lunch():
    if request.method == "POST":
        New_L = request.form["Lunch"]
        New_L = New_L.replace(" ","_")
        with open("/home/DarkShadow578/Menu/Lunches.txt","a")as o:
            o.write("\n"+New_L)
        return '''<html>
                    <body>
                        <p><a href="/">Click here to Start Again</a>
                    </body>
                </html>'''
    return '''
        <html>
            <body>
                <p>Enter New Lunch:</p>
                <form method="post" action="/Lunch/New">
                    <p><input name="Lunch" /></p>
                    <p><input type="submit" value="Add Lunch" /></p>
                </form>
            </body>
        </html>
    '''

#@app.route('/Lunch/Recipe', methods=["GET", "POST"])
#def Recipe_Lunch():

@app.route('/Dinner/Recipe', methods=["GET", "POST"])
def Recipe_Dinner():
    return '''
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_and_Rice"">Chicken and Rice</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Pizza"">Pizza</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Tuna_Napolitana"">Tuna Napolitana</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chilli"">Chilli</button></p>
     <p><p><button type="button" onclick="href="/Dinner/Recipe/Macaroni_Cheese"">Macaroni Cheese</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_Casserole"">Chicken Casserole</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Sausage_Casserole"">Sausage Casserole</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Burgers"">Burgers</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Sausage_and_Mash"">Sausage and Mash</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Enchiladers"">Enchiladers</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Stir-Fri"">Stir-Fri</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Spagetii_and_MeatBall"">Spagetii and MeatBall</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Spagetii"">Spagetii</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Tuna_Pasta_Bake"">Tuna Pasta Bake</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_Pasta_Bake"">Chicken Pasta Bake</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Soup"">Soup</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_Kievs"">Chicken Kievs</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_Carbenara"">Chicken Carbenara</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Roast_Pork"">Roast Pork</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Roast_Chicken"">Roast Chicken</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Pulled_Pork"">Pulled Pork</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Meatloaf"">Meatloaf</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Fajitas"">Fajitas</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Lasagne"">Lasagne</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Cottage_Pie"">Cottage Pie</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Fish_Pie"">Fish Pie</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Chicken_Pie"">Chicken Pie</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Beef_Pie"">Beef Pie</button></p>
     <p><button type="button" onclick="href="/Dinner/Recipe/Pork_Chops"">Pork Chops</button></p>


    '''









@app.route('/Dinner/Recipe/Beef_Pie', methods=["GET", "POST"])
def Beef_Pie():
    tbsp_to_ml=14.7868

    Sunflower = 14.7868/6 #ml
    bacon = 200/6 #grams
    steak = 900/6 #grams
    mushroom = 225/6 #grams
    onions = 225/6 #grams
    shallot = 1/6
    garlic = 2/6 #cloves
    suger = 14.7868/6 # tbsp
    wine = 600/6 #ml
    beef = 400/6 #grams
    stock = 400/6 #ml
    cornflour = 22.1802/6 #ml

    For the mashed potatoes

        1kg medium, floury potatoes
        Potato

        , preferably Maris Piper or Desirée, quartered
        50g unsalted butter
        100ml milk

    if request.method == "POST":
        return '''<html>
                    <body>
                        <p><a> </a>
                    </body>
                </html>'''
    return '''
        <html>
            <body>
                <p>Enter Amount of people eating:</p>
                <form method="post" action="/Dinner/Recipe/Beef_Pie">
                    <p><input name="Lunch" /></p>
                    <p><input type="submit" value="Select Number of people" /></p>
                </form>
            </body>
        </html>
    '''











