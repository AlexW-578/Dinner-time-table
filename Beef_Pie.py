from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True
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


@app.route("/", methods=["GET", "POST"])
def adder_page():
    return'''
    <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/Main.html">Click here to calculate again</a>
                    </body>
                </html>
    '''


For the mashed potatoes

    1kg medium, floury potatoes
    Potato

    , preferably Maris Piper or Desirée, quartered
    50g unsalted butter
    100ml milk
